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

tab close [major]:
    key(ctrl-f4)

# not default shortcut
tab close minor:
    key(ctrl-shift-f4)

browse [to]:
    key(ctrl-b)

duplicate:
    #   key(ctrl-w) # Old duplicate key in unreal engine 4
    key(ctrl-d)

blueprint open:
    key(ctrl-e)

rename:
    key(f2)

save all:
    key(ctrl-shift-s)
    sleep(200ms)
    key(ctrl-s)

open level:
    key(ctrl-o)

toggle coordinate [space]: key(ctrl-`)

(reference viewer | go usage): key(alt-shift-r)

size map: key(alt-shift-m)

(commandline | console) [open]: key(`)

screenshot:
    key(`)
    insert("HighResShot 3840x2160\n")

actor to level: key(ctrl-m)
level to actor: key(m)

build lighting: key(ctrl-shift-;)

select all of class: key(ctrl-shift-a)

prefix {user.unreal_prefixes}: insert(unreal_prefixes)

# views
view perspective: key(alt-g)
view top: key(alt-j)
view bottom: key(alt-shift-j)
view left: key(alt-k)
view right: key(alt-shift-k)
view front: key(alt-h)
view back: key(alt-shift-h)

##########
# All commands below are from the blueprint assist plugin
##########
blueprint assist menu: key(ctrl-shift-f1)

tab open: key(ctrl-shift-tab)
[blueprint] tab forwards: key(alt-end)
[blueprint] tab backwards: key(alt-home)
open window: key(ctrl-shift-k)
switch workflow: key(alt-o)

[<phrase>] [search] hunt:
    key(ctrl-alt-f)
    sleep(100ms)
    insert(phrase or "")

(node new | make node) [<user.text>]:
    key(tab)
    sleep(100ms)
    insert(text or "")

node replace:
    key(ctrl-h)

[toggle] context sensitive: key(ctrl-t)

(link to pin | pin (connect | link)): key(ctrl-shift-q)
((link (in | to) wire) | (node (connect | link))): key(ctrl-q)
(connect | link) menu: key(ctrl-l)

[node] (chuck | delete) [and] keep: key(shift-delete)

[node] toggle (purity | pure): key(shift-alt-g)
[node] toggle [advanced] display: key(alt-ctrl-a)

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

variable split: key(ctrl-shift-v)
variable merge: key(alt-shift-m)

look <user.arrow_keys>: user.arrow_key_sequence_with_modifiers(arrow_keys, "shift-")
node <user.arrow_keys>: user.arrow_key_sequence_with_modifiers(arrow_keys, "ctrl-")
pin <user.arrow_keys>: user.arrow_key_sequence_with_modifiers(arrow_keys)
swap <user.arrow_keys>: user.arrow_key_sequence_with_modifiers(arrow_keys, "ctrl-shift-")

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

escape repeater:
    key(escape:500)
