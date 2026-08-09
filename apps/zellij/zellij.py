from talon import Context, Module, actions

mod = Module()
mod.tag("zellij_scroll", desc="Active when Zellij is in scroll mode")

mod.apps.zellij = """
win.title: /zellij/i
"""

ctx = Context()
ctx.matches = """
app: zellij
win.title: /zellij/i
"""
ctx.tags = ["user.splits", "user.tabs", "terminal"]

# Toggled when entering/exiting Zellij scroll mode
scroll_ctx = Context()

# Overrides generic find commands (from the "find" tag) with Zellij's
# scroll-mode search keys; only active while in scroll mode.
scroll_edit_ctx = Context()
scroll_edit_ctx.matches = """
tag: user.zellij_scroll
"""

_focus_direction_keys = {
    "up": "k",
    "down": "j",
    "left": "h",
    "right": "l",
}


@mod.action_class
class Actions:
    def zellij_enter_scroll():
        """Enter Zellij scroll mode"""

    def zellij_exit_scroll():
        """Exit Zellij scroll mode"""

    def zellij_focus(direction: str):
        """Focus the Zellij pane in the given direction"""


@ctx.action_class("edit")
class EditActions:
    def page_up():
        actions.key("f3")

    def page_down():
        actions.key("f4")


@scroll_edit_ctx.action_class("edit")
class ScrollEditActions:
    def find(text: str = None):
        actions.key("s")
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
    # Implementing app tab actions
    def tab_open():
        actions.key("ctrl-t n")

    def tab_next():
        actions.key("ctrl-t right esc")

    def tab_previous():
        actions.key("ctrl-t left esc")

    def tab_close():
        actions.key("ctrl-t x")


@ctx.action_class("user")
class UserActions:
    # -------------------------------------------------------------------------
    # Implementing user.splits tag
    # -------------------------------------------------------------------------
    # right/left/up/down create new panes in that direction
    def split_window_right():
        actions.key("ctrl-p r")

    def split_window_left():
        actions.key("ctrl-p r")
        actions.sleep("50ms")
        actions.key("ctrl-h left esc")

    def split_window_up():
        actions.key("ctrl-p d")
        actions.sleep("50ms")
        actions.key("ctrl-h up esc")

    def split_window_down():
        actions.key("ctrl-p d")

    # vertically/horizontally create new panes
    def split_window_vertically():
        actions.key("ctrl-p r")

    def split_window_horizontally():
        actions.key("ctrl-p d")

    def split_window():
        actions.key("ctrl-p n")

    def split_next():
        actions.key("alt-right")

    def split_last():
        actions.key("alt-left")

    def split_maximize():
        actions.key("ctrl-p f")

    def split_clear():
        actions.key("ctrl-p x")

    def split_clear_all():
        actions.key("ctrl-p o")

    def split_flip():
        actions.key("ctrl-p s")

    def split_reset():
        actions.key("ctrl-p =")

    def split_number(index: int):
        pass  # no direct index jump binding in standard Zellij

    # -------------------------------------------------------------------------
    # Implementing user.tabs tag
    # -------------------------------------------------------------------------
    def tab_close_wrapper():
        actions.app.tab_close()

    def tab_jump(number: int):
        actions.key("ctrl-t")
        actions.sleep("50ms")
        actions.key(str(number))

    def tab_final():
        actions.key("ctrl-t 1")
        actions.sleep("50ms")
        actions.key("ctrl-t left")

    def tab_duplicate():
        actions.insert("zellij action dump-layout > /tmp/zellij_tab_layout.kdl && zellij action new-tab --layout /tmp/zellij_tab_layout.kdl\n")

    # -------------------------------------------------------------------------
    # Implementing custom Zellij actions
    # -------------------------------------------------------------------------
    def zellij_enter_scroll():
        actions.key("ctrl-s")
        scroll_ctx.tags = ["user.zellij_scroll", "user.find"]

    def zellij_exit_scroll():
        actions.key("escape")
        scroll_ctx.tags = []

    def zellij_focus(direction: str):
        key = _focus_direction_keys[direction]
        actions.key(f"ctrl-p {key} esc")
