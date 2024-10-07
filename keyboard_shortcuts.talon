mode:all
-

key(f10): speech.toggle()
key(f13:down):
  user.discord_global_mute()
  speech.toggle()
  
^talon switch$:
  user.discord_global_mute()
  speech.toggle()

gamepad(north:down): 
  speech.toggle()
  user.discord_global_mute()
  
key(ctrl-alt-shift-1):
  user.audio_default_switch("Wired Interface Output")
  user.audio_default_switch("Wired Mic Interface")

key(ctrl-alt-shift-2):
  user.audio_default_switch("Wireless Headset Output")
  user.audio_default_switch("Wireless Headset Mic")

key(ctrl-alt-shift-3):
  user.audio_default_switch("Index Headset Output")
  user.audio_default_switch("Index Headset Mic")
