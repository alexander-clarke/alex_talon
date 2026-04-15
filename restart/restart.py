from talon import Module, ui, Context, actions
import os
import signal

from subprocess import Popen

mod = Module()


@mod.action_class
class Actions:
    def talon_shutdown():
        "Shutdown Talon"

    def talon_restart():
        "Restart talon"


ctx_linux = Context()

ctx_linux.matches = r"""
os: linux
"""

ctx_windows = Context()
ctx_windows.matches = r"""
os: windows
"""

ctx_mac = Context()
ctx_mac.matches = r"""
os: mac
"""


@ctx_windows.action_class
class Actions:
    def talon_shutdown():
        "Shutdown Talon"
        talon_app = ui.apps(pid=os.getpid())[0]
        talon_app.quit()

    def talon_restart():
        """"""
        talon_app = ui.apps(pid=os.getpid())[0]
        os.startfile(talon_app.exe)
        talon_app.quit()


@ctx_linux.action_class("user")
class LinuxActions:
    def talon_shutdown():
        "Shutdown Talon"
        os.kill(os.getpid(), signal.SIGKILL)

    def talon_restart():
        """"""

        pid = os.getpid()

        with open(f"/proc/{pid}/cmdline", "rb") as f:
            # Arguments are separated by null bytes (\x00)
            content = f.read().decode("utf-8").replace("\x00", " ")
            Popen(content.strip())
            actions.user.talon_shutdown()


@ctx_mac.action_class("user")
class MacActions:
    def talon_shutdown():
        "Shutdown Talon"
        talon_app = ui.apps(pid=os.getpid())[0]
        talon_app.quit()

    def talon_restart():
        """restart talon"""
        talon_app = ui.apps(pid=os.getpid())[0]
        print("Restarting:", talon_app)
        talon_path = talon_app.path
        print("Path to app:", talon_path)
        subprocess.Popen(f"sleep 2; open {talon_path}", shell=True)
        talon_app.quit()
