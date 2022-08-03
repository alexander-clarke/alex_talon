mode: user.game
os: windows
and app.name: dota2.exe
os: windows
and app.exe: dota2.exe

-
stop: mouse_click(4)

parrot(cluck):key(k) 

parrot(oo): key(m)
parrot(shush): key(m)

self: key(z)

(sent|cent): 
  key(z)
  sleep(10ms)
  key(z)

(others|other): key(x)

donkey: key(f1)

(buy|by) (buy|by): key(f2)

deliver: key(f3)

shop: key(f5)
righty: mouse_click(1)
set quick: 
  key(shift:down)
  sleep(10ms)
  mouse_click(0)
  sleep(10ms)
  key(shift:up)
add quick: 
  key(shift:down)
  key(ctrl:down)
  sleep(10ms)
  mouse_click(0)
  sleep(10ms)
  key(shift:up)
  key(ctrl:up)

quench:
  key(alt-q)

whale:
  key(alt-w)

each:
  key(alt-e)

red:
  key(alt-r)

(tp|teepee): key(t)

<user.arrow_key>: 
  key("{arrow_key}:30")

big <user.arrow_key>: 
  key("{arrow_key}:90")

tiny <user.arrow_key>: 
  key("{arrow_key}:15")  
  # sleep(50ms)
  # key("{arrow_key}:up")

<phrase>:skip()


