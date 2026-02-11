from talon import Module, app, actions, Context, settings
from talon.lib import cubeb

mod = Module()
ctx = cubeb.Context()

currently_connected = False

mod.list("audio_devices", desc="")

mod.setting(
  "nircmd_path",
  type = str,
  default = "G:\\Program Files\\nircmd\\nircmd.exe",
  desc = "Path to call nircmd"  
 )

@mod.action_class
class AudioDevices:
  def audio_default_switch(new_default: str):
    """"""
    print(new_default)
    print(settings.get("user.nircmd_path"))
    print(actions.user.system_command(f'"{settings.get("user.nircmd_path")}" setdefaultsounddevice "{new_default}" 1'))
    actions.user.system_command(f'"{settings.get( "user.nircmd_path")}" setdefaultsounddevice "{new_default}" 2')
    
    # https://www.nirsoft.net/articles/set_default_audio_device_command_line.html
    # http://www.nirsoft.net/utils/nircmd.html

  def audio_set_default_in(audio_list_item: str):
    """"""
    actions.user.audio_default_switch(audio_list_item.split(',')[1])

  def audio_set_default_out(audio_list_item: str):
    """"""
    actions.user.audio_default_switch(audio_list_item.split(',')[0])

  def audio_set_default_in_out(audio_list_item: str):
    """"""
    actions.user.audio_set_default_out(audio_list_item)
    actions.user.audio_set_default_in(audio_list_item)

def devices_changed(device_type):
  global currently_connected

  devices = [
    dev.name for dev in ctx.inputs() if dev.state == cubeb.DeviceState.ENABLED
  ]
  # print(devices)

  if "Wired Mic Interface (Audient EVO4)" in devices:
    # print("Wired interface in device list")
    if not currently_connected:
      print("Launching evo to fix weird audio interface bug")
      actions.user.system_command_nb(r"C:\Program Files\Audient\EVO\EVO.exe")
    currently_connected = True
  else:
    currently_connected = False

def on_ready():
  ctx.register("devices_changed", devices_changed)

app.register("ready", on_ready)