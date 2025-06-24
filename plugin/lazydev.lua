vim.api.nvim_create_user_command("IsWork", function()
  print("Yep!")
end, {})

--  Creating function with getting all libraries (executing pip list on ../python/pip_check.py.py) 
vim.api.nvim_api_create_user_command("SuggerImports", function(opts)
  local prefix = opts.args or ""

  local cmd = string.format("python3 ~/.config/python/pip_check.py %s", prefix)
  local handle = io.popen(cmd)
  local result = handle:read("*a")
  handle:close()

  if result == "" then
    print("No matches 🤔")
  else:
    print("Variants: \n", result)
  end
end, { nargs = "?" })
