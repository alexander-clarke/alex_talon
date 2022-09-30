import time
from talon import Module, cron, Context, ctrl, ui,actions
import numpy as np

mod = Module()
mod.apps.dota = """
os: windows
and app.name: dota2.exe
os: windows
and app.exe: dota2.exe
"""

class DotaGaze:
  def __init__(self):
    self.gaze_cron = None
    
  def start_gaze(self):
    if not self.gaze_cron:
      self.gaze_cron = cron.interval("16ms", self.gaze_checker)
      
  def stop_gaze(self):
    if self.gaze_cron:
      cron.cancel(self.gaze_cron)
      
    self.gaze_cron = None
    actions.key("up:up")
    actions.key("down:up")
    actions.key("left:up")
    actions.key("right:up")
      
      
  def toggle_gaze(self):
    if self.gaze_cron:
      self.stop_gaze()
    else:
      self.start_gaze()
      
  def gaze_checker(self):
    x, y = ctrl.mouse_pos()
    screen_width = ui.screens()[0].rect.width
    screen_height = ui.screens()[0].rect.height
    scaled_position  = (x/screen_width, y/screen_height)
    centered_position = np.subtract(scaled_position,0.5) * 2
    direction = np.sign(centered_position) * (np.abs(centered_position) > 0.6)
    
    if direction[0] == -1:
      actions.key("left:down")
    else:
      actions.key("left:up")
      
    if direction[0] == 1:
      actions.key("right:down")
    else:
      actions.key("right:up")
    
    if direction[1] == -1:
      actions.key("up:down")
    else:
      actions.key("up:up")
      
    if direction[1] == 1:
      actions.key("down:down")
    else:
      actions.key("down:up")
      

class KeyHolder:
  def __init__(self, key):
    self.key_up_time = -1
    self.key_is_down = False
    self.job = None
    self.key = key
    
  def key_hold(self, time_hold="1000ms"):
    now = time.perf_counter()
    hold_s = cron.timespec_to_seconds(time_hold)
    if self.key_is_down:
        self.key_up_time += hold_s
    else:
        self.key_up_time = now + hold_s
    cron.cancel(self.job)
    timespec = cron.seconds_to_timespec(self.key_up_time - now)
    self.job = cron.after(timespec, self.key_up)
    print(self.job)
    self.key_is_down = True
    print(f"key {self.key} down")
    actions.key(f"{self.key}:down")
    
  def key_up(self):
    self.key_is_down = False
    print(f"key {self.key} up @ {time.perf_counter()} (intended: {self.key_up_time})")
    print(f"difference: {time.perf_counter()-self.key_up_time}")
    actions.key(f"{self.key}:up")
    
ctx = Context()
ctx.matches = r"""
os: windows
app: dota
"""

dg = DotaGaze()
key_holders = {}

@mod.action_class
class dota_actions:
  def dota_toggle_gaze():
    ''''''
    dg.toggle_gaze()
    
  def key_hold(key: str, time: str):
    """"""
    if key not in key_holders:    
      key_holders[key] = KeyHolder(key)
    key_holders[key].key_hold(time)
    
  def hold_middle_mouse():
    """"""
    ctrl.mouse_click(2, down = True, up=False)
    
    
  def release_middle_mouse():
    """"""
    ctrl.mouse_click(2, up = True, down=False)
    
  def center_cursor_position():
    """"""
    screen_center = ui.screens()[0].rect.center
    ctrl.mouse_move(screen_center.x, screen_center.y)
    # ctrl.mouse_click(2, up = True)
    
  def dota_send_chat_message(message: str, all: bool = False):
    """"""
    if all:
      actions.key("shift-enter")
    else:
      actions.key("enter")
    actions.sleep("10ms")
    actions.insert(message)
    actions.sleep("10ms")
    actions.key("enter")
