from talon import Module, actions, Context, app
from phue import Bridge


mod = Module()
ctx = Context()

bridge_ip = mod.setting(
  "hue_bridge_ip",
  str,
  None,
  "The IP for the hue bridge"
)

bridge = None

def on_ready():
  if bridge_ip.get() is not None:
    global bridge
    bridge = Bridge(bridge_ip.get())
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