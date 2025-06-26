### ⌨ LazyDevHelper

[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
---
### ⚠️ WARNING:
Still cooking... 🍳  
Right now, the plugin can only <b>check for libraries and installing</b> via pip list && pip install ...   
Adding to requirements.txt support coming soon.
---

<h1>Introduction</h1>

*Have you ever been in a situation like:*

> "I added 5 libs into my code before installing them, and now I need to write code with them... but I don't wanna switch to the console and write command. fucking world and terminal."

If yes — **Congratulations!** 🎉  
**You've found the Neovim plugin that can help you with both coding and installing Python libraries.**
---
# ❌ Errors
Status to: 
<pre>
  26/06/2025 - <b>ISSUE 7 - CLOSED</b>
    Cause - i fixed this error and now plugin doing main functional (installing library to pip)
</pre>    
If u have any suggest - or send comment to issue, or send push request, <b>i`ll check it and add to main branch if your variant working

---
### ❓ How  to work 
Very simple:
### Installing:  
**For Packer:  
add to ur init.lua: use 'silletr/LazyDevHelper', then :PackerInstall**  
And thats all, what u need


Second step: 
use :SuggestImports {lib_names} in needed file (or just random file, does not matter)
---
<h3>Status of 06/26/2025:</h3>
**This plugin is still in development. It's being built by a Python developer (me), who's learning Lua and Neovim's API to provide the best possible user experience.**

<p>If you spot any errors or want to help — feel free to create a Issua and Push Request.  
If it works (I will test it), I’ll definitely consider adding your version to the project!</p>
