from talon import Context, actions, Module

mod = Module()
mod.apps.cursorless_terminal = r"""
win.title: /CursorlessTerminal/
"""

ctx = Context()
ctx.matches = r"""
win.title: /CursorlessTerminal/
app: cursorless_terminal
"""

# Tags active for all shells
ctx.tags = [
    "user.cursorless",
    "terminal",
    "user.command_client",
    "user.tabs",
    "user.file_manager",
    "user.git",
    "user.kubectl",
]

# ── Shell-specific contexts ────────────────────────────────────────────────────

ctx_windows_shell = Context()
ctx_windows_shell.matches = r"""
win.title: /CursorlessTerminal\/(powershell|cmd)/
"""
ctx_windows_shell.tags = ["user.generic_windows_shell"]

ctx_unix_shell = Context()
ctx_unix_shell.matches = r"""
win.title: /CursorlessTerminal\/(bash|zsh|fish|sh)/
"""
ctx_unix_shell.tags = ["user.generic_unix_shell"]

# Actions and modifiers that we intercept and route through the terminal command server.
# All other pairs fall through to community's default handler (actions.next).
_TERMINAL_ACTIONS = {
    "delete",
    "select",
    "goBefore",
    "goAfter",
    "copyToClipboard",
    "cutToClipboard",
}

_TERMINAL_MODIFIERS = {
    "word",
    "wordLeft",
    "wordRight",
    "line",
    "lineStart",
    "lineEnd",
    "left",
    "right",
}


def _edit_command_callback(action: str, modifier: str):
    """Return a callback that sends terminal-edit-command to the command server.

    The signature (action, direction, count) matches the custom_callbacks
    protocol in edit_command.py, which inspects for a 'count' parameter to
    decide how to call the callback.

    run_rpc_command takes individual positional args which are collected into
    a list by run_command — so we pass action, modifier, count separately."""

    def callback(action_arg, direction_arg, count):
        actions.user.run_rpc_command("terminal-edit-command", action, modifier, count)

    return callback


@ctx.action_class("edit")
class EditActions:
    def paste():
        actions.user.run_rpc_command("terminal-paste")

    def page_up():
        actions.user.run_rpc_command("terminal-page-up")

    def page_down():
        actions.user.run_rpc_command("terminal-page-down")

    def copy():
        actions.user.run_rpc_command("terminal-copy")

    def cut():
        actions.user.run_rpc_command("terminal-cut")


@ctx.action_class("app")
class AppActions:
    def tab_open():
        actions.user.run_rpc_command("terminal-new-tab")

    def tab_close():
        actions.user.run_rpc_command("terminal-close-tab")

    def tab_next():
        actions.user.run_rpc_command("terminal-next-tab")

    def tab_previous():
        actions.user.run_rpc_command("terminal-prev-tab")

    def window_close():
        actions.user.run_rpc_command("terminal-close-window")


@ctx.action_class("user")
class UserActions:
    def command_server_directory() -> str:
        return "cursorless-terminal-command-server"

    def get_compound_edit_action_modifier_callback(pair):
        action, modifier = pair
        if action in _TERMINAL_ACTIONS and modifier in _TERMINAL_MODIFIERS:
            return _edit_command_callback(action, modifier)
        return actions.next(pair)

    def tab_close_wrapper():
        actions.app.tab_close()

    def tab_jump(number: int):
        actions.user.run_rpc_command("terminal-switch-tab", number)

    def tab_final():
        actions.user.run_rpc_command("terminal-last-tab")

    def tab_duplicate():
        actions.app.tab_open()

    def file_manager_current_path():
        return actions.user.run_rpc_command_get("terminal-get-cwd") or ""
