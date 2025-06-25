local M = {}

M.commands = function()
    vim.api.nvim_create_user_command("IsWorking", function()
        print("Yep!")
        print("Command executed successfully")
    end, {})

    vim.api.nvim_create_user_command("SuggestImports", function(opts)
        local args = opts.fargs
        local script_path = 'home/silletr/.config/nvim/lua/LazyDevHelper/python/pip_install.py'
        local result = vim.fn.system(cmd)

        for _, lib in ipairs(args) do
            local result = vim.system({ "python3", script_path, lib }, { text = true }):wait()
            -- local output = vim.fn.system(result)
            print("📦 Result for: " .. lib)
            print(output)
            if result.code == 0 then
                print(result.stdout)
            else
                print("❌ Error:")
                print(result.stderr)
            end
        end
end, { nargs = "+" })

return M
