from talon import Context, Module, settings, actions

mod = Module()

mod.setting("default_browser", type=str, default="Firefox", desc="Default browser")


@mod.action_class
class Actions:
    def focus_default_browser():
        """Focuses the default browser, default set by a setting"""
        browser_name = settings.get("user.default_browser")
        actions.user.switcher_focus(browser_name)
