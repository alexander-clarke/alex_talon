mode: user.game
os: windows
and app.name: dota2.exe
os: windows
and app.exe: dota2.exe

-
stop: 
  # mouse_click()
  key(i) 

parrot(cluck):key(m) 

parrot(oo): mouse_click(4)
parrot(shush): key(m)

ping: 
  key(alt:down)
  sleep(16ms)
  mouse_click(0)
  sleep(16ms)
  key(alt:up)

self: key(z)

(sent|cent): 
  key(z)
  sleep(10ms)
  key(z)

follow:
  key(z:down)
  
(others|other): key(x)

donkey: key(f1)

(buy|by) (buy|by): key(f2)

deliver: key(f3)

shop: key(f5)
righty: mouse_click(1)
quick: 
  key(shift:down)
  sleep(10ms)
  mouse_click(0)
  sleep(10ms)
  key(shift:up)
quick add: 
  key(shift:down)
  key(ctrl:down)
  sleep(10ms)
  mouse_click(0)
  sleep(10ms)
  key(shift:up)
  key(ctrl:up)

quench:
  key(alt-q)

(whale|well):
  key(alt-w)

each:
  key(alt-e)

red:
  key(alt-r)

^one$:
  key(1)

(tp|teepee): key(t)

# skill: key(u)

<user.arrow_key>:
  user.key_hold("{arrow_key}", "320ms")

big <user.arrow_key>: 
  key("{arrow_key}:90")

tiny <user.arrow_key>: 
  key("{arrow_key}:15")  
  # sleep(50ms)
  # key("{arrow_key}:up")

(days|gaze):
  user.dota_toggle_gaze()

flame:
  key(shift-enter)
  sleep(10ms)
  insert("i'm not even touching the keyboard lol")
  sleep(10ms)
  key(enter)

voice:
  key(shift-enter)
  sleep(10ms)
  insert("i'm using voice controls")
  sleep(10ms)
  key(enter)

# fault:
#   key(shift-enter)
#   sleep(10ms)
#   insert("this doesn't even count + I'm disabled + I'm not touching my mouse + L + ratio")
#   sleep(10ms)
#   key(enter)

<phrase>:skip()
 
settings():
  speech.timeout = 0.05