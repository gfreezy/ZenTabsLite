## [ZenTabsLite](https://github.com/gfreezy/ZenTabsLite)
Zen Tabs Lite is a fork of [ZenTabs](https://github.com/travmik/ZenTabs), fixing the multiple group bugs, removing the tab explorer.

Zen Tabs is a [Sublime Text 2](http://www.sublimetext.com/2)/[3](http://www.sublimetext.com/3) plugin that helps you to keep you tab bar in Zen.
How often do you see something like this? It is useless pice of sh... Isn't it?
![FFFFUUUUUU](https://dl.dropboxusercontent.com/u/22258694/ZenTabs/ZenTabs-FFUUU.jpg)
Now it stops!
Now you can be in Zen when you are working with Sublime Text.
Focused and with peace in mind.

Your tab bar can always have a look like this:
![Zen](https://dl.dropboxusercontent.com/u/22258694/ZenTabs/ZenTabs-10.jpg)
Or even like this:
![Zeeeeeeeeen](https://dl.dropboxusercontent.com/u/22258694/ZenTabs/ZenTabs-Zen.jpg)
You have to do nothing for this. You just need to install this package, set opened tabs limit(default 10) and enjoy.
When you will open 11th tab the oldest one will be closed. And don't worry __it will never close any tab with unsaved work__. If you have nothing but tabs with unsaved work, it will just ignore the limit and create a new tab anyway.

## Installation
To install this plugin, you have three options:
1. If you have [Sublime Package Control](http://wbond.net/sublime_packages/package_control) installed, simply search for `Zen Tabs` to install.
2. Clone source code to Sublime Text packages folder *Sublime Text 2/Packages*.
3. Download archive with the latest [release](https://github.com/gfreezy/ZenTabsLite/releases) and unpack it to Sublime Text packages folder *Sublime Text 2/Packages*.

*OSX*

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    git clone git://github.com/gfreezy/ZenTabsLite.git

*Linux*

    cd ~/.config/sublime-text-2/Packages
    git clone git://github.com/gfreezy/ZenTabsLite.git

*Windows*

    cd "%APPDATA%\Sublime Text 2\Packages"
    git clone git://github.com/gfreezy/ZenTabsLite.git

## Settings
`Preferences > Package Settings > Zen Tabs > Settings`
* __open_tab_limit__: Controls the maximum allowed number of tabs.
Note that edited or draft tabs are not count towards this limit. The default is 10.

## Contribution
You can contribute on [github](https://github.com/gfreezy/ZenTabsLite).
I always welcome pull requests. Here's some general rules for pull requests to be accepted:
- [PEP8](http://www.python.org/dev/peps/pep-0008/) is our coding style guide.
- Please create a branch before sending pull requests.
- Your pull request should be atomic. That is, fix a bug or implementing a feature in one commit instead of multiple commit.    This is a recommendation, not a requirement.

Copyright 2011-2013 [Stanislav Parfeniuk](http://www.linkedin.com/in/stanislavparfeniuk). Licensed under the MIT License
