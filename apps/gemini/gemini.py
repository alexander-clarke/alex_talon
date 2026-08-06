from talon import Context, Module

mod = Module()
mod.apps.gemini_cli = r"""
win.title: /gemini/i
"""

mod.list("user.gemini_mcp_servers", desc="Gemini CLI MCP server names")

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
