# LazyDevHelper
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

---
### First Release! 🍾
<b>At 1/07/2025 i released my first release version that plugin - and maybe this will be a slep into the future of NeoVim plugins, but - i dont know</b>
---
<b>Thats plugin can help Python-developers manage dependencies directly from their editor. Currently handles pip installations and library checks, with requirements.txt support planned.</b>

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

## Introduction
Have you ever been in a situation like:

> "I added 5 libs into my code before installing them, and now I need to write code with them... but I don't wanna switch to the console and write command. fucking world and terminal."

If yes — **Congratulations!** 🎉  
**You've found the Neovim plugin that can help you with both coding and installing Python libraries.**

## Errors
Error status:
```markdown
26/06/2025 - ISSUE 7 - CLOSED
Cause - Fixed pip installation functionality
```
If you have any suggestions or find issues, feel free to create an issue or send a pull request. If it works (I'll test it), I'll definitely consider adding your changes to the project!

## Installation Requirements
- Neovim 0.9+
- Python 3.10+

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

If you spot any errors or want to help — feel free to create an issue or send a pull request. If it works (I'll test it), I'll definitely consider adding your version to the project!
