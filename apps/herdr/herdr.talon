app: herdr
win.title: /herdr/i
-

copy mode: user.herdr_enter_copy()
scrollback edit: key(ctrl-b e)
resize mode: key(ctrl-b r)

pane <user.arrow_key>: user.herdr_focus(arrow_key)
pane move <user.arrow_key>: user.herdr_move(arrow_key)
pane zoom: key(ctrl-b z)
pane cycle: key(ctrl-b tab)

pane rename: key(ctrl-b shift-p)
pane rename <user.text>:
    key(ctrl-b shift-p)
    sleep(50ms)
    insert(user.text)
    key(enter)

tab rename: key(ctrl-b shift-t)
tab rename <user.text>:
    key(ctrl-b shift-t)
    sleep(50ms)
    insert(user.text)
    key(enter)

tab move left: key(ctrl-b [)
tab move right: key(ctrl-b ])

workspace new: key(ctrl-b shift-n)
workspace switch: key(ctrl-b w)
workspace rename: key(ctrl-b shift-w)
workspace close: key(ctrl-b shift-d)
worktree new: key(ctrl-b shift-g)

sidebar toggle: key(ctrl-b b)
navigator: key(ctrl-b g)
notifications: key(ctrl-b o)
herdr reload: key(ctrl-b shift-r)
herdr detach: key(ctrl-b q)
