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


@mod.action_class
class Actions:
    def unfocus_address_bar():
        """Unfocuses the address bar"""
        actions.key("ctrl-l")
        actions.key("tab")
        actions.key("tab")


@ctx.action_class("user")
class Actions:
    def file_manager_terminal_here():
        actions.user.system_command_nb(
            f"wt.exe -d {actions.user.file_manager_current_path()}"
        )

    def file_manager_select_directory(path: str):
        """selects the directory"""
        actions.user.unfocus_address_bar()
        actions.insert(path)

    def file_manager_new_folder(name: str):
        """Creates a new folder in a gui filemanager or inserts the command to do so for terminals"""
        actions.user.unfocus_address_bar()
        actions.key("ctrl-shift-n")
        actions.insert(name)

    def file_manager_open_file(path: str):
        """opens the file"""
        actions.user.unfocus_address_bar()
        actions.insert(path)
        actions.key("enter")

    def file_manager_select_file(path: str):
        """selects the file"""
        actions.user.unfocus_address_bar()
        actions.insert(path)
