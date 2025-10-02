from talon import Module, actions, Context, app, settings
from .phue import Bridge


mod = Module()
ctx = Context()

mod.setting(
  "hue_bridge_ip",
  str,
  None,
  "The IP for the hue bridge"
)

bridge = None

def on_ready():
  if settings.get("user.hue_bridge_ip") is not None:
    global bridge
    bridge = Bridge(settings.get("user.hue_bridge_ip"))
    print("Found bridge in startup")
    
app.register("ready", on_ready)

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
    else:
      print("No bridge")    
    