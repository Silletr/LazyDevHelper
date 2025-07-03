# Lazy Developer Helper
[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

## Table of Contents
- [Introduction](#introduction)
- [Errors](#errors)
- [Installation Requirements](#installation-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Status](#status)

## Introduction

*Have you ever been in a situation like:*

> “I added 5 libs into my code before installing them, and now I need to write code with them, but I dont wanna switch to the console and write the command. Fucking world and terminal.”
If yes — **Congratulations!** 🎉  
**You have found the Neovim plugin that helps you manage Python dependencies without leaving your editor.**

## Errors
Error status:  
```text
26/06/2025 – ISSUE 7 – CLOSED
Cause – I fixed this error and now the plugin does its main function (installing libraries via pip)
```

## Installation Requirements
### Prerequisites
- Neovim 0.9+
- Python 3.10+

## Installation
With Packer:
```lua
use {
  'Silletr/LazyDevHelper',
  config = function()
    require('LazyDevHelper.plugin.commands').commands()
  end
}
```

## Usage
![Command example](LazyDevHelper/images/command_example.png "Input example")  
Output example:
![Output](LazyDevHelper/images/output_example.png "Output")

## Status
Status as of 01/07/2025:
Plugin released successfully.
If you have ideas or spot bugs, open an issue or PR—if it works, I will merge it.
