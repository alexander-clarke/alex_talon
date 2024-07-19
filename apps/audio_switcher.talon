-
audio (out|output) wireless:
  user.audio_default_switch("Wireless Headset Output")
audio (sis|system) wireless: 
  user.audio_default_switch("Wireless Headset Output")
  user.audio_default_switch("Wireless Headset Mic")

audio (out|output) wired:
  user.audio_default_switch("Wired Interface Output")
audio (sis|system) wired: 
  user.audio_default_switch("Wired Interface Output")
  user.audio_default_switch("Wired Mic Interface")

audio (sis|system) index:
  user.audio_default_switch("Index Headset Output")
  user.audio_default_switch("Index Headset Mic")
audio (out|output) index:
  user.audio_default_switch("Index Headset Output")

audio (out|output) bows: 
  user.audio_default_switch("Bose Output")

audio (out|output) (surround|flat): 
  user.audio_default_switch("Speakers")  

audio input road: user.audio_default_switch("Rode Wireless Mic")