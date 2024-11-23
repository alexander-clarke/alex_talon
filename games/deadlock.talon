mode: user.game
os: windows
and app.name: project8.exe
os: windows
and app.exe: /^project8\.exe$/i
-
(open shop)| (shop open)|((by|buy) menu): key(b)

deck(pedal_middle): mouse_click(0)
deck(pedal_left): key(b)
deck(pedal_right): key(tab)

deck(pedal_middle:down): key(t:down)
deck(pedal_middle:up): key(t:up)

<phrase>:skip() 