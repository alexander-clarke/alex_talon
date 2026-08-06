from urllib.parse import quote_plus
from talon import Context, Module, actions, clip, ui

mod = Module()
mod.apps.gemini_cli = r"""
win.title: /gemini/i
"""

mod.list("gemini_mcp_servers", desc="Gemini CLI MCP server names")

ctx = Context()
ctx.matches = r"""
app: gemini_cli
"""
ctx.tags = ["user.slash_commands"]
ctx.lists["user.slash_commands"] = {
    "clear": "clear",
    "compress": "compress",
    "resume": "chat resume",
    "chat list": "chat list",
    "memory show": "memory show",
    "memory refresh": "memory refresh",
    "rewind": "rewind",
}
ctx.lists["user.gemini_mcp_servers"] = {
    "atlassian": "atlassian",
    "github": "github",
    "google drive": "gdrive",
}


@mod.action_class
class Actions:
    def gemini_hunt(text: str = ""):
        """Search Gemini using focus_default_browser, browser.go, rango_focus_first_input, insert, and enter."""
        actions.user.focus_default_browser()
        actions.sleep("200ms")

        actions.browser.go("https://gemini.google.com")
        actions.sleep("1s")

        if text:
            actions.user.rango_focus_first_input()
            actions.sleep("300ms")
            actions.insert(text)
            actions.sleep("300ms")
            actions.key("enter")









