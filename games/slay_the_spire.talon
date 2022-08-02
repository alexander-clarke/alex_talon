mode: user.game

os: windows
and app.name: Java(TM) Platform SE binary
and win.title: Slay the Spire

os: windows
and app.exe: javaw.exe
and win.title: Slay the Spire

-

^[card] <number_small>$: insert(number_small)

end turn$: key(e)
parrot(cluck): key(e)

[view] deck: key(d)

[view] draw: key(a)

[view] map: key(m)

[view] (discord|discard): key(s)

[view] exhaust: key(x)

control mouse: tracking.control_toggle()

go <user.arrow_keys>: user.move_cursor(arrow_keys)

<phrase>: skip()