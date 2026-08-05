tag: user.zellij_scroll
-

exit scroll: user.zellij_exit_scroll()
scroll up: key(up)
scroll down: key(down)
page up: key(u)
page down: key(d)
scroll top: key(g)
scroll bottom: key(shift-g)

search <user.text>:
    key(s)
    sleep(50ms)
    insert(user.text)
    key(enter)

next result: key(n)
previous result: key(shift-n)
