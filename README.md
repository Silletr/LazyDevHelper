# Lazy Developer Helper

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

### Table of Contents

- [Introduction](#introduction)
- [Errors](#errors)
- [Installation Requirements](#installation-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Status](#status)

### Introduction

*Have you ever been in a situation like:*

> “I added 5 libs into my code before installing them, and now I need to write code with them, but I don’t wanna switch to the console and write the command. Fucking world and terminal.”

If yes — **Congratulations!** 🎉  
**You’ve found the Neovim plugin that helps you manage Python dependencies without leaving your editor.**

### Errors

Error status:  
<pre>
26/06/2025 – <b>ISSUE 7 – CLOSED</b>  
Cause – I fixed this error and now the plugin does its main function (installing libraries via pip)
</pre>  

If you have any suggestions, feel free to open an issue or submit a pull request. I’ll review it and merge if it works.

### Installation Requirements
- Neovim 0.9+
- Python 3.10+
### Installation

With Packer:
```lua
use {
  'Silletr/LazyDevHelper',
  config = function()
    require('LazyDevHelper.plugin.commands').commands()
  end
}
```
### Usage
![Input example](LazyDevHelper/images/command_example.png)  

Output example:
![Output](LazyDevHelper/images/output_example.png)
### Status
Status as of 01/07/2025:
Thinking about adding requirements.txt support. If you have ideas or spot bugs, open an issue or PR—if it works, I will merge it.
