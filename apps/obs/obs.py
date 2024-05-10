from talon import Module, actions, Context, app

mod = Module()
ctx = Context()

def call_obs_cli(arguments):
  print(f"obs-cli {arguments}")
  actions.user.system_command(f"obs-cli {arguments}")
  
@mod.action_class
class ObsActions:
  def start_recording():
    ''''''
    call_obs_cli("record start")
    
  def stop_recording():
    ''''''
    call_obs_cli("record stop")
  
  def toggle_recording():
    ''''''
    call_obs_cli("record toggle")
    
  def start_virtual_camera():    
    ''''''
    call_obs_cli("virtualcam start")

  def scene_switch(scene_name: str):
    ''''''
    call_obs_cli(f'scene switch "{scene_name}"')

  