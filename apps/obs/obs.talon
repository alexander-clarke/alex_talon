os: windows
and app.name: OBS Studio
os: windows
and app.exe: obs64.exe
-
deck(pedal_left): user.stop_recording()
recording stop: user.stop_recording()

deck(pedal_right): user.start_recording()
recording start: user.start_recording()

tic tock scene: user.scene_switch("TikTokVertical")

virtual camera start: 
  user.start_virtual_camera()

virtual camera stop:
  user.stop_virtual_camera()