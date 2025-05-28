return {
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
    },
    config = function()
      require("mason").setup()
      require("mason-lspconfig").setup({
        ensure_installed = { "pyright" }, -- Install Python LSP
        automatic_installation = true,
      })

      local lspconfig = require("lspconfig")
      lspconfig.pyright.setup({})
    end,
  },
}

