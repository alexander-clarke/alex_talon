mode: user.game
os: windows
and app.name: Snowman.exe
os: windows
and app.exe: Snowman.exe
mod
-

<user.arrow_keys>: user.move_cursor(arrow_keys)

<number_small> <user.arrow_keys>: key("{user.arrow_keys}:{number_small}")

refresh:
  key(r)

wipe:
  key(backspace)

<phrase>:
  skip()

settings():
  key_hold = 20
  key_wait = 200