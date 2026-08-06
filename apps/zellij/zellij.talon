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

pane right: key(alt-right)
pane left: key(alt-left)
pane up: key(alt-up)
pane down: key(alt-down)

resize right: key(ctrl-n right esc)
resize left: key(ctrl-n left esc)
resize up: key(ctrl-n up esc)
resize down: key(ctrl-n down esc)

session new: key(ctrl-o n)
session switch: key(ctrl-o w)
session detach: key(ctrl-o d)

zellij quit: key(ctrl-q)
