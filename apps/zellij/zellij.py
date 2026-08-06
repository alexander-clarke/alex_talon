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


@mod.action_class
class Actions:
    def zellij_enter_scroll():
        """Enter Zellij scroll mode"""

    def zellij_exit_scroll():
        """Exit Zellij scroll mode"""


@ctx.action_class("app")
class AppActions:
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
    # right/left/up/down navigate between panes
    def split_window_right():
        actions.key("alt-right")

    def split_window_left():
        actions.key("alt-left")

    def split_window_up():
        actions.key("alt-up")

    def split_window_down():
        actions.key("alt-down")

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
        pass

    def split_flip():
        pass

    def split_reset():
        pass

    def split_number(index: int):
        pass  # no default Zellij binding

    def tab_close_wrapper():
        actions.app.tab_close()

    def tab_jump(number: int):
        actions.key("ctrl-t")
        actions.sleep("50ms")
        actions.key(str(number))

    def tab_final():
        pass  # no default Zellij binding

    def tab_duplicate():
        pass  # not supported

    def zellij_enter_scroll():
        actions.key("ctrl-s")
        scroll_ctx.tags = ["user.zellij_scroll"]

    def zellij_exit_scroll():
        actions.key("escape")
        scroll_ctx.tags = []
