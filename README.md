# LazyDevHelper
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
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
- Auto-adds to `requirements.txt` if found
- Lua/Python hybrid

## Installation

```lua
{
  "Silletr/LazyDevHelper",
  config = function()
    require("LazyDevHelper.plugin.commands").commands()
  end,
}

Usage

    Enter :SuggestImports streamlit bs4 requests

    The plugin will check if the libraries are installed

    If not, it'll install them via pip

    It will also try to update requirements.txt if present
```

Example input:
![LazyDevHelper/images/command_example.png]  

Output:
[![LazyDevHelper/images/output_example.png]]

---
# Status
2025-06-26
Plugin is actively in development. Lua/Python hybrid. Feedback is welcome!
