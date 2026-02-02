-
audio (out|output) {user.audio_devices}:
  user.audio_set_default_out( user.audio_devices )

audio (sis|system) {user.audio_devices}:
  user.audio_set_default_in_out( user.audio_devices )
  
  
audio (in|input) {user.audio_devices}:
  user.audio_set_default_in( user.audio_devices )