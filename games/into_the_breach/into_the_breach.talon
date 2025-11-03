# Not mine I think it was frons slack
mode: user.game
os: mac
and app.bundle: subset.Into-the-Breach

os: windows
and app.name: Breach.exe
os: windows
and app.exe: Breach.exe


-
^go <user.any_alphanumeric_key>+$:
    user.breach_go_to_tile(any_alphanumeric_key_list, "")

^click <user.any_alphanumeric_key>+$:
    user.breach_go_to_tile(any_alphanumeric_key_list, "click")

# parrot(tongue_click):
# 	# mouse_click(0)

parrot(cluck):
	mouse_click(0)

