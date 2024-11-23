os: windows
and win.title: /Ziggy/

os: windows
and app.name: Ziggys Cosmic Adventure
os: windows
and app.exe: ZiggyGame-Win64-Shipping.exe

-

toggle camera:
  # key(ctrl-shift-x)
  key(shift:down)
  key(ctrl:down)
  sleep(20ms)
  key(x)
  sleep(20ms)
  key(shift:up)
  key(ctrl:up)

calibrate position:
  key(ctrl-shift-k)

calibrate height:
  key(ctrl-shift-h)

settings():
  key_hold = 0.3
  key_wait = 0.2
