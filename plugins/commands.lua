local M = {}

M.commands = function()
  vim.api.nvim_create_user_command("IsWorking", function()
    print("Yep!")
    print("Command executed successfully")
  end, {})

  vim.api.nvim_create_user_command("SuggestImports", function(opts)
    local prefix = opts.args or ""

    local script_path = vim.fn.stdpath('config') .. '/lua/LazyDevHelper/python/pip_check.py'
    local cmd = string.format("python3 %s %s", script_path, prefix)

    local handle = io.popen(cmd)
    if handle then
      local result = handle:read("*a")
      handle:close()

      if result == "" then
        print("No matches 🤔")
      else
        print("Variants: \n" .. result)
      end
    else
      print("Error: Could not execute Python script")
    end
  end, { nargs = "?" })
end

return M

