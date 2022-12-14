os: windows
# app.exe: /UE4Editor/
app: unreal
# app: UE4Editor.exe
# app.exe: UE4Editor.exe
-
tag(): user.unreal_commands

file hunt [<user.text>]:
  user.find_file(text or "")
  # key(ctrl-p)
  # insert(text or "")

launch on device:
  key(alt-shift-p)

simulate:
  key(alt-s)

breakpoint:
  key(f9)
  
step into:
  key(f11)  

step over:
  key(f10)

tab close:
  key(ctrl-f4)

browse [to]:
  key(ctrl-b)

duplicate:
  key(ctrl-w)

blueprint open:
  key(ctrl-e)

rename:
  key(f2)

save all:
  key(ctrl-shift-s)
  sleep(200ms)
  key(ctrl-s)

toggle coordinate [space]: key(ctrl-`)

(reference viewer|go usage): key(alt-shift-r)

(commandline|console) [open]: key(`)  

actor to level: key(ctrl-m)
level to actor: key(m)

build lighting: key(ctrl-shift-;)

prefix {user.unreal_prefixes}: insert(user.unreal_prefixes)

# views
view perspective: key(alt-g)
view top: key(alt-j)
view bottom: key(alt-shift-j)
view left: key(alt-k)
view right: key(alt-shift-k)

# new blueprint plugin
blueprint assist menu: key(ctrl-shift-f1)

open window: key(ctrl-shift-k)

(node new|make node) [<phrase>]: 
  key(tab)
  sleep("150ms")
  insert(user.phrase or "")

[toggle] context sensitive: key(ctrl-t)

(link to pin|pin (connect|link)): key(ctrl-shift-q)
((link (in|to) wire)|(node connect)): key(ctrl-q)

node delete and link: key(shift-delete)

node disconnect: key(ctrl-d)
pin disconnect: key(d)
all pins disconnect: key(ctrl-shift-d)

zoom to tree: key(ctrl-=)

edit details: key(ctrl-shift-e)

symbol new: key(ctrl-shift-a)
symbol hunt: key(ctrl-g)

variable hunt: key(ctrl-shift-g)

pin context menu: key(ctrl-m)
node context menu: key(ctrl-shift-m)

pin split: key(alt-q)
pin recombine: key(ctrl-alt-q)

edit value: key(ctrl-e)

format: key(f)
format selection: key(shift-f)
format all: key(ctrl-r)

look <user.arrow_key>: key("shift-{arrow_key}")
node <user.arrow_key>: key("ctrl-{arrow_key}")
pin <user.arrow_key>: key("{arrow_key}")
swap <user.arrow_key>: key("ctrl-shift-{arrow_key}")

# material editor
material vector:
  key(3:down)
  sleep(200ms)
  mouse_click(0)
  key(3:up)

material scalar:
  key(1:down)
  sleep(200ms)
  mouse_click(0)
  key(1:up)