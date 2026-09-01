import json
import os
import subprocess
from pathlib import Path

from talon import Context, Module

mod = Module()
# Matches a Zellij pane pinned to this name via `zellij action rename-pane
# claude-cli` (or the "pane rename claude cli" voice command). Claude Code
# overwrites its terminal title with a dynamic status/summary string, so
# unlike Gemini/k9s a plain "claude" title match isn't stable enough to use
# directly — the pane name must be pinned first so it can't be overwritten.
mod.apps.claude_cli = r"""
win.title: /claude-cli/i
"""

mod.list("claude_mcp_actions", desc="Claude Code MCP subcommands")


@mod.action_class
class Actions:
    def claude_start():
        """Open Claude Code in a new Windows Terminal tab with a pinned title."""
        fragment_dir = (
            Path(os.environ["LOCALAPPDATA"])
            / "Microsoft" / "Windows Terminal" / "Fragments" / "talon"
        )
        fragment_dir.mkdir(parents=True, exist_ok=True)
        fragment_path = fragment_dir / "claude-cli.json"
        if not fragment_path.exists():
            fragment_path.write_text(json.dumps({
                "profiles": [{
                    "name": "Claude CLI",
                    "tabTitle": "claude-cli",
                    "suppressApplicationTitle": True,
                    "commandline": "powershell.exe -NoExit -Command \"$env:CLAUDE_CLI_SESSION = '1'; claude\""
                }]
            }, indent=2))
        wt = Path(os.environ["LOCALAPPDATA"]) / "Microsoft" / "WindowsApps" / "wt.exe"
        subprocess.Popen([str(wt), "new-tab", "--profile", "Claude CLI"])

ctx = Context()
ctx.matches = r"""
app: claude_cli
"""
ctx.tags = ["user.slash_commands"]
ctx.lists["user.claude_mcp_actions"] = {
    "reconnect": "reconnect",
    "enable": "enable",
    "disable": "disable",
}
