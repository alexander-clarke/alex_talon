from talon import Context, Module, actions

mod = Module()
mod.tag("herdr_copy", desc="Active when herdr is in copy mode")

mod.apps.herdr = """
win.title: /herdr/i
"""

ctx = Context()
ctx.matches = """
app: herdr
win.title: /herdr/i
"""
ctx.tags = ["user.splits", "user.tabs", "terminal"]

# Toggled when entering/exiting herdr copy mode
copy_ctx = Context()

# Overrides edit.find* with herdr copy-mode search keys
copy_edit_ctx = Context()
copy_edit_ctx.matches = """
tag: user.herdr_copy
"""

_vim_direction_keys = {
    "up": "k",
    "down": "j",
    "left": "h",
    "right": "l",
}


@mod.action_class
class Actions:
    def herdr_enter_copy():
        """Enter herdr copy mode"""

    def herdr_exit_copy():
        """Exit herdr copy mode"""

    def herdr_focus(direction: str):
        """Focus the herdr pane in the given direction"""

    def herdr_move(direction: str):
        """Swap the herdr pane in the given direction"""


@copy_edit_ctx.action_class("edit")
class CopyEditActions:
    def find(text: str = None):
        actions.key("/")
        if text:
            actions.sleep("50ms")
            actions.insert(text)
            actions.key("enter")

    def find_next():
        actions.key("n")

    def find_previous():
        actions.key("shift-n")


@ctx.action_class("app")
class AppActions:
    def tab_open():
        actions.key("ctrl-b c")

    def tab_next():
        actions.key("ctrl-b n")

    def tab_previous():
        actions.key("ctrl-b p")

    def tab_close():
        actions.key("ctrl-b shift-x")


@ctx.action_class("user")
class UserActions:
    # -------------------------------------------------------------------------
    # user.splits — pane creation and navigation
    # -------------------------------------------------------------------------
    def split_window_right():
        actions.key("ctrl-b v")

    def split_window_down():
        actions.key("ctrl-b minus")

    def split_window_left():
        actions.key("ctrl-b v")
        actions.sleep("50ms")
        actions.key("ctrl-b shift-h")

    def split_window_up():
        actions.key("ctrl-b minus")
        actions.sleep("50ms")
        actions.key("ctrl-b shift-k")

    def split_window_vertically():
        actions.key("ctrl-b v")

    def split_window_horizontally():
        actions.key("ctrl-b minus")

    def split_window():
        actions.key("ctrl-b v")

    def split_next():
        actions.key("ctrl-b tab")

    def split_last():
        actions.key("ctrl-b shift-tab")

    def split_maximize():
        actions.key("ctrl-b z")

    def split_clear():
        actions.key("ctrl-b x")

    def split_clear_all():
        pass

    def split_flip():
        pass

    def split_reset():
        pass

    def split_number(index: int):
        pass

    # -------------------------------------------------------------------------
    # user.tabs
    # -------------------------------------------------------------------------
    def tab_close_wrapper():
        actions.app.tab_close()

    def tab_jump(number: int):
        actions.key(f"ctrl-b {number}")

    def tab_final():
        pass

    def tab_duplicate():
        pass

    # -------------------------------------------------------------------------
    # Custom herdr actions
    # -------------------------------------------------------------------------
    def herdr_enter_copy():
        actions.key("ctrl-b [")
        copy_ctx.tags = ["user.herdr_copy", "user.find"]

    def herdr_exit_copy():
        actions.key("q")
        copy_ctx.tags = []

    def herdr_focus(direction: str):
        key = _vim_direction_keys[direction]
        actions.key(f"ctrl-b {key}")

    def herdr_move(direction: str):
        key = _vim_direction_keys[direction]
        actions.key(f"ctrl-b shift-{key}")
