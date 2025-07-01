## LazyDevHelper
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

---
### ⚠️ WARNING:
Still cooking... 🍳  
Right now, the plugin can only <b>check for libraries and installing</b> via pip list && pip install ...   
Adding to requirements.txt support coming soon.
---
A Neovim plugin that helps Python developers manage dependencies directly from their editor. Currently handles pip installations and library checks, with requirements.txt support planned.

### Features
- Install Python libraries without leaving Neovim
- Check installed libraries
- Simple command interface
- Packer installation support
```lua
use {
    'Silletr/LazyDevHelper',
    config = function()
        require("LazyDevHelper.plugin.commands").commands()
    end
}
```


---
<h1>Introduction</h1>

*Have you ever been in a situation like:*

> "I added 5 libs into my code before installing them, and now I need to write code with them... but I don't wanna switch to the console and write command. fucking world and terminal."

If yes — **Congratulations!** 🎉  
**You've found the Neovim plugin that can help you with both coding and installing Python libraries.**
---
# ❌ Errors
Error status: 
<pre>
  26/06/2025 - <b>ISSUE 7 - CLOSED</b>
    Cause - i fixed this error and now plugin doing main functional (installing library to pip)
</pre>    
If u have any suggest - or send comment to issue, or send push request, <b>i`ll check it and add to main branch if your variant working
---

### Installation Requirements
- Neovim 0.7+
- Python 3.10+
---
### ❓ Usage
### Usage
`:SuggestImports {lib_names}` - Install and import Python libraries directly from your editor.
Output example:

![output](LazyDevHelper/images/output_example.png)
---
### 📊 Status of plugin
<h3>Status of 06/26/2025:</h3>
<b>This plugin is still in development. It's being built by a Python developer (me), who's learning Lua and Neovim's API to provide the best possible user experience.</b>

<p>If you spot any errors or want to help — feel free to create a Issua and Push Request.  
If it works (I will test it), I’ll definitely consider adding your version to the project!</p>

