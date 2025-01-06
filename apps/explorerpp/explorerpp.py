from talon import Module, Context, actions

mod = Module()

mod.apps.explorerpp = r"""
os: windows
and app.name: Explorer++
os: windows
and app.exe: /^explorer\+\+\.exe$/i
"""

ctx = Context()
ctx.matches = r"""
app: explorerpp
os: windows
"""


@ctx.action_class("user")
class Actions:
    def file_manager_terminal_here():
        actions.user.system_command_nb(
            f"wt.exe -d {actions.user.file_manager_current_path()}"
        )
