### LazyDevHelper
[![Awesome](https://awesome.re/badge.svg)]
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Status](#status)

## Features
- Install Python libraries without leaving Neovim
- Check installed libraries
- Simple command interface
- Packer installation support

## Installation
```lua
use {
    'Silletr/LazyDevHelper',
    config = function()
        require("LazyDevHelper.plugin.commands").commands()
    end
}
```

## Usage
Entered command example:
![Input example](LazyDevHelper/images/command_example.png)
Output example:
![output](LazyDevHelper/images/output_example.png)

## Status
### 06/26/2025
This plugin is still in development. I'm a Python developer learning Lua and Neovim's API to provide the best possible user experience.

### 01/07/2025
First release day! The plugin is still in development, and I'm working on adding support for requirements.txt files. If you have any ideas about this feature, feel free to share them in the issues section.

If you spot any errors or want to help - feel free to create an issue or send a pull request. If it works (I'll test it), I'll definitely consider adding your version to the project!
