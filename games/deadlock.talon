mode: user.game
mode: command
os: windows
and app.name: deadlock.exe
os: windows
and app.exe: /^deadlock\.exe$/i
-
(open shop)| (shop open)|((by|buy) menu): key(b)

deck(pedal_middle:down): user.mouse_drag(0)
deck(pedal_middle:up): user.mouse_drag_end()
deck(pedal_left): key(b)
deck(pedal_right): key(tab)

# deck(pedal_middle:down): key(t:down)
# deck(pedal_middle:up): key(t:up)

<phrase>:skip() 

# settings():