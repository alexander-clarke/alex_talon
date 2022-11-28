mode: user.game
os: windows
and app.name: dota2.exe
os: windows
and app.exe: dota2.exe

-
stop: 
  mouse_click(3) 

parrot(shush): mouse_click(3)
parrot(ch): mouse_click(3)

parrot(cluck): key(q)

parrot(oo): mouse_click(4)
parrot(buzz): mouse_click(1)

ping: 
  key(alt:down)
  sleep(32ms)
  mouse_click(0)
  sleep(16ms)
  key(alt:up)

self: key(z)

(sent|cent): 
  key(z:up)
  key(z)
  sleep(16ms)
  key(z)

follow:
  key(z:up)
  key(z)
  sleep(16ms)
  key(z:down)
  
(others|other): key(x)

(tote|tot|tort): key(c)

donkey:   key(f1)

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
quick (add|ad|at): 
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

parrot(tut):
  key(w)

parrot(hmm):
  key(e) 

each:
  key(alt-e)

red:
  key(alt-r)

drum:
  key(d)

fine:
  key(f)

vest:
  key(v)

^one$:
  key(1)

^one one$:
  key(1)
  key(1)

^two$:
  key(alt-2)

space:
  key(space)

arch: key(a)

sun: key(s)

taunt:
  key(f10)

# line:
#   user.key_hold("k", "1000ms")

(tp|teepee|tippy): key(t)

score: user.key_hold("`", "2000ms")

sticky: key(f7)

# skill: key(u)

drag: user.mouse_drag(0)
(dragend|dragon): user.mouse_drag_end(0)

curse:
  # mouse_click(2, down = True)
  user.hold_middle_mouse()
  sleep(16ms)
  user.center_cursor_position()
  sleep(16ms)
  user.release_middle_mouse()
  # mouse_click(2, down = False)

<user.arrow_key>:
  user.key_hold("{arrow_key}", "96ms")

# <user.arrow_key> er:
#   user.key_hold("{arrow_key}", "640ms")

be <user.arrow_key>: 
  user.key_hold("{arrow_key}", "256ms")

be <user.arrow_key> <user.arrow_key>: 
  user.key_hold("{arrow_key_1}", "256ms")
  user.key_hold("{arrow_key_2}", "256ms")

keyboard:
  user.dota_send_chat_message("i'm not even touching the keyboard lol", 1)

voice:
  user.dota_send_chat_message("i'm using voice controls!", 1)

ge ge:
  user.dota_send_chat_message("gg", 1)

injury explain:
  user.dota_send_chat_message("hi due to rsi I am unable to use my hands to play and instead use a mixture of eye tracking and voice commands, which doesn't always work so apologies in advance")

how I play:
  user.dota_send_chat_message("due to rsi I am unable to use my hands to play and instead use a mixture of eye tracking and voice commands", 1)

(geback|get back|ge back): 
  key(b)

(push):
  key([)

well played:
  key(,)

hero missing:
  key(.)

laugh:
  user.dota_send_chat_message("/laugh")

# fault:
#   key(shift-enter)
#   sleep(10ms)
#   insert("this doesn't even count + I'm disabled + I'm not touching my mouse + L + ratio")
#   sleep(10ms)
#   key(enter)

<phrase>:skip()
 
settings():
  speech.timeout = 0.020