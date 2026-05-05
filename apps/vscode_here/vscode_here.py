from talon import Context, Module, actions

mod = Module()


@mod.action_class
class Actions:
    def vscode_here():
        """Opens VS Code in the current file manager folder"""
        actions.user.system_command_nb(
            f"code \"{actions.user.file_manager_current_path()}\""
        )

    def vscode_open(path: str):
        """Opens a relative path in VS Code from the current file manager folder"""
        base = actions.user.file_manager_current_path()
        target = f"{base}\\{path}" if path else base
        actions.user.system_command_nb(f"code \"{target}\"")


ctx_terminal = Context()
ctx_terminal.matches = r"""
tag: user.terminal
"""


@ctx_terminal.action_class("user")
class TerminalActions:
    def vscode_here():
        actions.insert("code .")
        actions.key("enter")

    def vscode_open(path: str):
        if path:
            actions.insert(f"code {path}")
            actions.key("enter")
        else:
            actions.insert("code ")
