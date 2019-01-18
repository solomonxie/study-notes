# VIM保存当前状态 [DRAFT]

## 保存当前的所有Tab/Window/Buffer的布局状态 (session)

```vim
function! AutoSaveSession()
    if bufnr('%') >= 3
        :mksession! /tmp/obsession.vim
    endif
endfunction

function! AutoLoadSession()
    if filereadable(expand('workspace.vim'))
        :source workspace.vim
    elseif filereadable(expand('/tmp/obsession.vim'))
        :source /tmp/obsession.vim
    endif
endfunction
autocmd VimLeave * call AutoSaveSession()
"autocmd VimEnter * call AutoLoadSession()

" Save session
noremap <leader>S :mksession! /tmp/obsession.vim<CR><ESC>
" Load session
"noremap <leader>R :source /tmp/obsession.vim<CR><ESC>
noremap <leader>R :call AutoLoadSession()<CR>
```

一个更好的实践（保存在当前项目的.git目录下且不会被追踪）：
```vim
"[Session]----------------------------------{
    function! AutoSaveSession()
        if bufnr('%') >= 3
            if isdirectory('.git')
                :mksession! .git/workspace.vim
            elseif isdirectory('../.git')
                :mksession! ../.git/workspace.vim
            elseif isdirectory(expand('~/.vim'))
                :mksession! ~/.vim/session.vim
            endif
        endif
    endfunction

    function! AutoLoadSession()
        if filereadable(expand('workspace.vim'))
            :source workspace.vim
        elseif filereadable(expand('.git/workspace.vim'))
            :source .git/workspace.vim
        elseif filereadable(expand('../.git/workspace.vim'))
            :source ../.git/workspace.vim
        elseif filereadable(expand('~/.vim/session.vim'))
            :source ~/.vim/session.vim
        endif
    endfunction
    autocmd VimLeave * call AutoSaveSession()
    "autocmd VimEnter * call AutoLoadSession()

    " Save session
    noremap <Leader>S :mksession! ~/.vim/session.vim<CR><ESC>
    " Load session
    "noremap <Leader>R :source ~/.vim/session.vim<CR><ESC>
    noremap <Leader>R :call AutoLoadSession()<CR>
" }
```

## 全屏Split后恢复原先布局

```vim
Plug 'dhruvasagar/vim-zoom'
```

键盘映射：
```vim
nmap mm <Plug>(zoom-toggle)
```

## 保存当前所有Buffer的编辑历史

默认下，VIM重新打开后，就不能Undo恢复上一步操作了。
但是我们可以利用VIM的原生功能实现：

```vim
" [  Persistent undo  ]--------{
    set undofile "Maintain UNDO history between sessions
    set undodir=/tmp/
" }
```
