mode: user.game

os: windows
and app.name: Java(TM) Platform SE binary
and win.title: Slay the Spire

os: windows
and app.exe: javaw.exe
and win.title: Slay the Spire
-

^[card] <number_small>$: key("{number_small}")

confirm card: key(enter)

end turn$: key(e)
parrot(cluck): key(e)

[view] deck: key(d)

[view] draw: key(a)

[view] map: key(m)

[view] (discord|discard): key(s)

[view] exhaust: key(x)

# yes I know this is bad, but I couldn't be bothered to make a python file
# for looking up and down in the map
look up: 
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  sleep(50ms)
  user.mouse_scroll_up(100)
  
look down:   
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)
  sleep(50ms)
  user.mouse_scroll_down(100)

control mouse: tracking.control_toggle()

escape: key(escape)

go <user.arrow_keys>: user.move_cursor(arrow_keys)

# means I can talk while playing the game which is pretty cool
<phrase>: skip()
