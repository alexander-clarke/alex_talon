from talon import Module, app, actions, Context
from talon.lib import cubeb

mod = Module()
ctx = cubeb.Context()

currently_connected = False

@mod.action_class
class audio_switcher:
  def audio_default_switch(new_default: str):
    """"""
    actions.user.system_command(f'"G:\\Program Files\\nircmd\\nircmd.exe" setdefaultsounddevice "{new_default}" 1')
    actions.user.system_command(f'"G:\\Program Files\\nircmd\\nircmd.exe" setdefaultsounddevice "{new_default}" 2')
    
    # https://www.nirsoft.net/articles/set_default_audio_device_command_line.html
    # http://www.nirsoft.net/utils/nircmd.html

def devices_changed(device_type):
  global currently_connected

  devices = [
    dev.name for dev in ctx.inputs() if dev.state == cubeb.DeviceState.ENABLED
  ]
  print(devices)

  if "Wired Mic Interface (Audient EVO4)" in devices:
    print("Wired interface in device list")
    if not currently_connected:
      print("Launching evo to fix weird audio interface bug")
      actions.user.system_command_nb(r"C:\Program Files\Audient\EVO\EVO.exe")
    currently_connected = True
  else:
    currently_connected = False

def on_ready():
    ctx.register("devices_changed", devices_changed)


app.register("ready", on_ready)