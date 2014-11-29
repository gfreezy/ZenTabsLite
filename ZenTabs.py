import sys
import time
import sublime
import sublime_plugin


# temporary because ST2 doesn't have plugin_loaded event
def sublime_text_3():
    """Returns True if this is Sublime Text 3
    """
    try:
        return int(sublime.version()) >= 3000
    except ValueError:
        return sys.hexversion >= 0x030000F0


g_tabLimit = 50


def plugin_loaded():
    global g_tabLimit
    settings = sublime.load_settings('ZenTabs.sublime-settings')
    g_tabLimit = settings.get('open_tab_limit', g_tabLimit)


if not sublime_text_3():
    # because of plugin loaded earlier than preferences
    sublime.set_timeout(lambda: plugin_loaded(), 500)


def is_preview(view):
    return sublime.active_window().get_view_index(view)[1] == -1


def is_active(view):
    return view.id() == sublime.active_window().active_view().id()


def is_edited(view):
    return view.is_dirty() or view.is_scratch()


def is_closable(view):
    is_not_closable = is_edited(view) or is_preview(view) or is_active(view) or view.is_loading()
    return not(is_not_closable)


_to_be_closed_view = None
_to_be_open_view = None


def close_view(view, fallback):
    global _to_be_closed_view, _to_be_open_view
    _to_be_closed_view = view.id()
    _to_be_open_view = fallback.id()
    window = view.window()
    window.focus_view(view)
    window.run_command('close')
    window.focus_view(fallback)
    window = view.window()
    _to_be_open_view = _to_be_closed_view = None


class ViewGroup(object):
    def __init__(self, id, capacity=g_tabLimit):
        # id (window, group)
        self.id = id
        self.update_time = {}
        self.capacity = capacity

    def add(self, active_view):
        window = active_view.window()
        window = active_view.window()
        active_group = window.active_group()
        views = window.views_in_group(active_group)
        self.update_view_time(active_view)

        views_with_update_time = []
        for v in views:
            update_time = self.update_time.get(v.id())
            if not update_time:
                update_time = 0
            views_with_update_time.append((v, update_time))
        views_with_update_time.sort(key=lambda t: t[1])

        if len(views) <= self.capacity:
            return

        for i, (view, _) in enumerate(views_with_update_time):
            if is_closable(view):
                views_with_update_time.pop(i)
                close_view(view, active_view)
                break

        self.update_time = dict([(v.id(), update_time_) for v, update_time_ in views_with_update_time])

    def update_view_time(self, view):
        self.update_time[view.id()] = time.time()


class ZenTabsListener(sublime_plugin.EventListener):
    def __init__(self, *args, **kwargs):
        self.tabs = dict()
        return super(ZenTabsListener, self).__init__(*args, **kwargs)

    def on_activated(self, view):
        global _to_be_closed_view, _to_be_open_view
        if view.id() == _to_be_closed_view or view.id() == _to_be_open_view:
            return
        window = view.window()
        group_id, view_id = window.get_view_index(view)

        if group_id == -1 or view_id == -1:
            return
        window_id = window.id()
        id = (window_id, group_id)
        try:
            view_group = self.tabs[id]
        except KeyError:
            view_group = ViewGroup(id)
            self.tabs[id] = view_group

        view_group.add(view)
