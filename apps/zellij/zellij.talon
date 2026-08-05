app: zellij
-

scroll mode: user.zellij_enter_scroll()
float pane: key(ctrl-p w)
lock terminal: key(ctrl-g)

rename pane <user.text>:
    key(ctrl-p c)
    sleep(50ms)
    insert(user.text)
    key(enter)

rename tab <user.text>:
    key(ctrl-t r)
    sleep(50ms)
    insert(user.text)
    key(enter)

focus right: key(alt-right)
focus left: key(alt-left)
focus up: key(alt-up)
focus down: key(alt-down)

resize right: key(ctrl-n right esc)
resize left: key(ctrl-n left esc)
resize up: key(ctrl-n up esc)
resize down: key(ctrl-n down esc)

new session: key(ctrl-o n)
switch session: key(ctrl-o w)
detach: key(ctrl-o d)

quit zellij: key(ctrl-q)
