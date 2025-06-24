return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'

  -- Theme
  use 'navarasu/onedark.nvim'
  require('onedark').setup {
    style = 'darker'
  }
  require('onedark').load()

  -- Autocomplete
  use 'hrsh7th/nvim-cmp'
  use 'hrsh7th/cmp-nvim-lsp'
  use 'hrsh7th/cmp-buffer'
  use 'hrsh7th/cmp-path'

  use 'sheerun/vim-polyglot'
  use 'vim-airline/vim-airline'
  use 'vim-airline/vim-airline-themes'

  -- file tree
  require("nvim-tree").setup({
  update_focused_file = {
      enable = true,
      update_cwd = true,
    },
      view = {
      width = 30,
      side = "left",
      },
    })

end)

vim.keymap.set("n", "<C-b>", ":NvimTreeFindFileToggle<CR>", { noremap = true, silent = true } )
