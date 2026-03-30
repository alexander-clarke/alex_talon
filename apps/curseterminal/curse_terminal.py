from talon import Context, actions

ctx = Context()
ctx.matches = r"""
title: /Cursorless Terminal/
"""

# Enable the command_client to automatically discover our server
ctx.tags = ["user.cursorless", "terminal", "user.command_client"]


@ctx.action_class("user")
class UserActions:
    def command_server_directory() -> str:
        # Matches the directory name used in CommandServer.ts
        return "cursorless-terminal-command-server"
