local M = {}

M.commands = function()
    vim.api.nvim_create_user_command("IsWorking", function()
        print("Yep!")
        print("Command executed successfully")
    end, {})

    vim.api.nvim_create_user_command("SuggestImports", function(opts)
        local args = opts.fargs
        local script_path = vim.fn.stdpath("config") .. "/lua/LazyDevHelper/python/pip_install.py"

        for _, lib in ipairs(args) do
            local result = vim.system({ "python3", script_path, lib }, { text = true }):wait()
            print("📦 Result for: " .. lib)
            if result.code == 0 then
                print(result.stdout)
            else
                print("❌ Error:")
                print(result.stderr)
            end
        end
    end, { nargs = "+" })
end

M.commands()
return M

