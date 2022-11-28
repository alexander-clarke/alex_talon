from talon import Module, actions, ctrl, noise, cron, Context, scope
#from talon_plugins import eye_mouse, eye_zoom_mouse
from time import sleep, time


#from talon.experimental import locate; help(locate)

start = 0
running = False
noise_length_threshold = "100ms"
threshold_passed = False

mod = Module()
setting_mouse_enable_hiss_drag = mod.setting(
    "mouse_enable_hiss_drag",
    type=int,
    default=1,
    desc="Enable hiss to drag when control mouse is enabled.",
)

def still_running():
    global running
    global threshold_passed
    if running:
        threshold_passed = True
        toggle_mouse_drag(True)
        print('hiss duration passed threshold, starting gaze drag')



def cursor_drag_on_hiss(is_active):
  if actions.app.name() == "dota2.exe":
    if is_active:
      ctrl.mouse_click(button = 4, hold = 30)
  else:
    if "noise" in scope.get("mode"):
      if is_active:
        global start
        global running
        global threshold_passed
        if is_active:
            print("Start Hiss")
            if 0 in ctrl.mouse_buttons_down():
              ctrl.mouse_click(button=0, up=True)
            else:
              # ctrl.mouse_click(button=0, down=True)
              start = time()
              running = True
              cron.after(noise_length_threshold, still_running)
        else:
            running = False
            if threshold_passed:
                threshold_passed = False
                toggle_mouse_drag(False)
                print('end of hiss detected, disabling gaze drag')

noise.register('hiss', cursor_drag_on_hiss)

def toggle_mouse_drag(active: bool):
    #Press and hold/release button 0 depending on state for dragging"""
    # used this code:
    # https://github.com/AndreasArvidsson/andreas-talon/blob/master/misc/mouse/mouse.py
    if 0 in ctrl.mouse_buttons_down():
        ctrl.mouse_click(button=0, up=True)
    else:
        ctrl.mouse_click(button=0, down=True)

# if setting_mouse_enable_hiss_drag.get() == 0 and active: # allow turning off just not on
    #     return

#    if eye_zoom_mouse.zoom_mouse.enabled or eye_mouse.mouse.attached_tracker is None:
#        return

# if active:
    #     ctrl.mouse_click(button=0, down=True)
    # else:
    #     ctrl.mouse_click(button=0, up=True)