from talon import Module, actions
from phue import Bridge

mod = Module()

bridge_ip = mod.setting(
  "hue_bridge_ip",
  str,
  None,
  "The IP for the hue bridge"
)
bridge =None
if bridge_ip.get() is not None:
  bridge = Bridge(bridge_ip.get())

@mod.action_class
class HueActions:
  def lights_on():
    """"""
    actions.user.lights_onoff(True)
    
  def lights_off():
    """"""
    actions.user.lights_onoff(False)
  
  def lights_onoff(newstate: bool):
    """"""
    if bridge is not None:
      for light in bridge.lights:
        light.on = newstate