app: zellij
win.title: /zellij/i
-

scroll mode: user.zellij_enter_scroll()
pane float: key(ctrl-p w)
terminal lock: key(ctrl-g)

pane rename: key(ctrl-p c)
pane rename <user.text>:
    key(ctrl-p c)
    sleep(50ms)
    insert(user.text)
    key(enter)

tab rename: key(ctrl-t r)
tab rename <user.text>:
    key(ctrl-t r)
    sleep(50ms)
    insert(user.text)
    key(enter)

pane <user.arrow_key>: user.zellij_focus(arrow_key)
pane move <user.arrow_key>: key("ctrl-h {arrow_key} esc")
frames toggle: key(ctrl-p z)
pane embed: key(ctrl-p e)

resize <user.arrow_key>: key("ctrl-n {arrow_key} esc")

tab move left: key(ctrl-t [)
tab move right: key(ctrl-t ])
tab sync: key(ctrl-t s)

scrollback edit: key(ctrl-s e)

session new: key(ctrl-o n)
session switch: key(ctrl-o w)
session detach: key(ctrl-o d)

zellij quit: key(ctrl-q)
