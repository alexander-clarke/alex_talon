from talon import Module, ui
import os

mod = Module()

@mod.action_class
class Actions:
  def talon_shutdown():
    "Shutdown Talon on windows"
    talon_app = ui.apps(pid=os.getpid())[0]
    talon_app.quit()

  def talon_restart():
    ""
    talon_app = ui.apps(pid = os.getpid())[0]
    os.startfile(talon_app.exe)
    talon_app.quit()