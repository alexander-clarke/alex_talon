from talon import Module, actions, Context, scope

mod = Module()
ctx = Context()

mod.apps.adobe_premiere_pro = r"""
os: windows
and app.name: Adobe Premiere Pro 2023
os: windows
and app.exe: Adobe Premiere Pro.exe
os: windows
and app.name: /Premiere Pro/
"""

mod.tag("feet_cutting", desc="enables the feet to cut")

mod.tag("feet_moving", desc="enables the feet to move")

ctx.matches = r"""
os: windows
app: adobe_premiere_pro
"""

@mod.action_class
class Action:
  def feet_moving():
    """"""
    ctx.tags = ["user.feet_moving"]

  def feet_cutting():
    """"""
    ctx.tags = ["user.feet_cutting"]
    

@mod.action_class
class Action:
  def cut_at_play_head():
    """"""
    actions.key("x")
    
  def trim_previous_edit_to_play_head():
    """"""
    actions.key("ctrl-alt-q")
  
  def trim_next_edit_to_play_head():
    """"""
    actions.key("ctrl-alt-w")
    
  def ripple_trim_previous_edit_to_play_head():
    """"""
    actions.key("q")
    
  def ripple_trim_next_edit_to_play_head():
    """"""
    actions.key("w")
    
  def ripple_delete():
    """"""
    actions.key("e")
    
  def shuttle_left():
    """"""
    actions.key("j")
    
  def shuttle_right():
    """"""
    actions.key("l")
    
  def shuttle_slow_left():
    """"""
    actions.key("shift-j")
    
  def shuttle_slow_right():
    """"""
    actions.key("shift-l")
    
  def frame_left():
    """"""
    actions.key("left")
    
  def clip_left():
    ''''''
    actions.key("shift-up")
    
  def clip_right():
    ''''''
    actions.key("shift-down")
        
  def frame_right():
    """"""
    actions.key("right")
    
  def mark_in():
    """"""
    actions.key("i")
    
  def mark_out():
    """"""
    actions.key("o")
    
  def recording_toggle():
    ''''''
    actions.speech.toggle()
    if "sleep" not in scope.get("mode"):    
      actions.key("space")
    else:
      actions.key("keypad_divide:down")
      actions.sleep(0.1)
      actions.key("keypad_divide:up")
    
    
@ctx.action_class("edit")
class EditActions:
  def zoom_in():
    actions.key("f")
    
  def zoom_out():
    actions.key("g")