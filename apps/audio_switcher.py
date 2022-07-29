from talon import Module, app, actions

mod = Module()


@mod.action_class
class audio_switcher:
  def audio_default_switch(new_default: str):
    """"""
    actions.user.system_command(f'"G:\\Program Files\\nircmd\\nircmd.exe" setdefaultsounddevice "{new_default}" 1')
    actions.user.system_command(f'"G:\\Program Files\\nircmd\\nircmd.exe" setdefaultsounddevice "{new_default}" 2')
    
      # https://www.nirsoft.net/articles/set_default_audio_device_command_line.html
  # http://www.nirsoft.net/utils/nircmd.html