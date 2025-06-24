-- First command with debug
vim.api.nvim_create_user_command("IsWorking", function()
  print("Yep!")
  print("Command executed successfully")
end, {})

-- Second command with debug
vim.api.nvim_create_user_command("SuggestImports", function(opts)
    print("SuggestImports command started")
    local prefix = opts.args or ""
    print("Prefix:", prefix)
    
    local script_path = vim.fn.stdpath('config') .. '/lua/LazyDevHelper/python/pip_check.py'
    print("Script path:", script_path)
    
    local cmd = string.format("python3 %s %s", script_path, prefix)
    print("Command to execute:", cmd)
    
    local handle = io.popen(cmd)
    if handle then
        print("Python script executed successfully")
        local result = handle:read("*a")
        handle:close()
        
        if result == "" then
            print("No matches 🤔")
        else
            print("Variants: \n", result)
        end
    else
        print("Error: Could not execute Python script")
    end
end, { nargs = "?" })
