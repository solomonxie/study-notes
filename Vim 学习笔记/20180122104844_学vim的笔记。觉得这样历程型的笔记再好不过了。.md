## 学vim的笔记。觉得这样历程型的笔记再好不过了。


VIM TODO:
- [ ] https://github.com/devjoe/vim-codequery
- [ ] https://github.com/easymotion/vim-easymotion
- [ ] https://github.com/justinmk/vim-sneak
- [ ] https://github.com/sheerun/vim-polyglot
- [ ] https://github.com/wellle/targets.vim
- [ ] https://github.com/ajh17/VimCompletesMe
- [ ] https://github.com/SidOfc/mkdx
- [ ] Ctags jumps whole project (Save tag files to `.git/` to avoid tracking)


## Plugins

### UI

- [x] Start Screen
    - [x] `mhinz/vim-startify`
- [x] Theme
    - [x] `morhetz/gruvbox`
- [x] STATUS-BAR
    - [x] `vim-airline/vim-airline`
    - [x] `vim-airline/vim-airline-themes`
- [x] Syntax Highlighting
    - [x] `hdima/python-syntax`   "Most stable highlighting
- [x] Window
    - [x] `TaDaa/vimade`  "Dim inactive windows
    - [x] `vim-scripts/ZoomWin` "Zoom In/Out (Error)
    - [x] `dhruvasagar/vim-zoom`
    - [x] `junegunn/goyo.vim`  "Focus Mode



### EDIT

- [x] Autocomplete
    - [x] [Snippets]
        - [x] `SirVer/ultisnips`  " Track the engine.
        - [x] `honza/vim-snippets`  " Snippets are separated from the engine.
    - [x] [Deoplete]
        - [x] `Shougo/deoplete.nvim`
        - [x] `zchee/deoplete-jedi`    " Python completion source
        - [x] `Shougo/deoplete-clangx`   " C/C++ completion source
- [x] Comment
    - [x] `scrooloose/nerdcommenter`
- [x] Code Check
    - [x] `vim-syntastic/syntastic` "Static Code Check
- [x] Bracket Closing
    - [x] `jiangmiao/auto-pairs` "Smartest (bug:)
- [x] Indentation
    - [x] Plug  'Yggdroot/indentLine'    "Beautiful indent lines
- [x] Trailing Whitespace
    - [x] `bronson/vim-trailing-whitespace`



### Navigation

- [x] Fuzzy File Search
    - [x] fzf
        - [x] `junegunn/fzf`
        - [x] `junegunn/fzf.vim`
    - [x] NetRW
        - [x] `tpope/vim-vinegar`      "Netrw enhancement
- [x] NERDTREE
    - [x] `scrooloose/nerdtree`          " File tree manager
    - [x] `jistr/vim-nerdtree-tabs'      " enhance nerdtree`s tabs
    - [x] `ryanoasis/vim-devicons`       " add beautiful icons besides files
- [x] Bookmarks
    - [x] `MattesGroeger/vim-bookmarks`  "Manage bookmarks
- [x] nnn
    - [x] `mcchrish/nnn.vim`
- [x] Ranger
    - [x] `francoiscabrol/ranger.vim`
- [x] History
    - [x] `yegappan/mru`
- [x] Tags (ctags required)
    - [x] `majutsushi/tagbar`   "Display
    - [x] `ludovicchabant/vim-gutentags` "Manage tags (auto)
    - [x] `craigemery/vim-autotag`  "Navigate (manually gen tags)
- [x] Git
    - [x] `jreybert/vimagit`  "Much easier with Git
    - [x] `tpope/vim-fugitive` "work with fzf for :Commits
    - [x] `iberianpig/tig-explorer.vim` "faster/prettier (tig required)
- [x] Documentation
    - [x] `powerman/vim-plugin-viewdoc` "K-preview improvement


### MISC

- [x] `kassio/neoterm`
- [x] `tpope/vim-obsession`  "For Tmux to restore VIM sessions
- [x] `mbbill/undotree`
- [x] `tweekmonster/startuptime.vim`   "VIM loading analysis


### Discarded

- [x] Window
    - [x] `blueyed/vim-diminactive`  "not dim Indent lines
- [x] Folding
    - [x] `tmhedberg/SimpylFold`   "improving folding
- [x] Completion
    - [x] `valloric/youcompleteme`    "hard to build
    - [x] `neoclide/coc.nvim', {'do`: { -> coc#util#install()}}   "not working
    - [x] `rkulla/pydiction`   " not work as expected
    - [x] `ervandew/supertab`
    - [x] `davidhalter/jedi-vim`  "complicated
    - [x] `lifepillar/vim-mucomplete`  "tab. sources complicated
- [x] Indentation
    - [x] `nathanaelkane/vim-indent-guides`
- [x] Brackets
    - [x] `tpope/vim-surround`  "Barely working
    - [x] `Townk/vim-autoclose` "Fair, but not working for some files
- [x] Snippets
    - [x] `MarcWeber/vim-addon-mw-utils`
    - [x] `tomtom/tlib_vim`
    - [x] `garbas/vim-snipmate`
    - [x] `honza/vim-snippets` "some common snippets (python required)
- [x] Git
    - [x] `tpope/vim-fugitive`    "Commands to do Git
    - [x] `easymotion/vim-easymotion`
- [x] Markdown
    - [x] `JamshedVesuna/vim-markdown-preview` "Not live previewing
- [x] File Browsing
    - [x] `Xuyuanp/nerdtree-git-plugin`  " display git status within Nerdtree
    - [x] `tiagofumo/vim-nerdtree-syntax-highlight` " enhance devicons
    - [x] `wincent/command-t`    "VIM only (Ruby required)
    - [x] `justinmk/vim-dirvish`  "Netrw enhancement
- [x] Color Scheme
    - [x] `chriskempson/base16-vim`   "Ugly !!
    - [x] `jpo/vim-railscasts-theme`  "Ugly !
    - [x] `NLKNguyen/papercolor-theme`   "No python support
- [x] Status Bar
    - [x] `itchyny/lightline.vim` "beautiful status line
    - [x] `Lokaltog/vim-powerline` "fancy status line (python required)
- [x] Syntax Highlighting
    - [x] `vim-python/python-syntax`
    - [x] `vitiral/vim-python`  "Not working
    - [x] `numirias/semshi`    "Not working
    - [x] `pfdevilliers/Pretty-Vim-Python`   "not working
    - [x] `python-mode/python-mode`    "Deprecated

