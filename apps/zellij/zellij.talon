app: zellij
win.title: /zellij/i
-

scroll mode: user.zellij_enter_scroll()
float pane: key(ctrl-p w)
lock terminal: key(ctrl-g)

rename pane: key(ctrl-p c)
rename pane <user.text>:
    key(ctrl-p c)
    sleep(50ms)
    insert(user.text)
    key(enter)

rename tab: key(ctrl-t r)
rename tab <user.text>:
    key(ctrl-t r)
    sleep(50ms)
    insert(user.text)
    key(enter)

pane <user.arrow_key>: key("alt-{arrow_key}")
move pane <user.arrow_key>: key("ctrl-h {arrow_key} esc")
toggle frames: key(ctrl-p z)
embed pane: key(ctrl-p e)

resize <user.arrow_key>: key("ctrl-n {arrow_key} esc")

tab move left: key(ctrl-t [)
tab move right: key(ctrl-t ])
tab sync: key(ctrl-t s)

edit scrollback: key(ctrl-s e)

session new: key(ctrl-o n)
session switch: key(ctrl-o w)
session detach: key(ctrl-o d)

zellij quit: key(ctrl-q)
