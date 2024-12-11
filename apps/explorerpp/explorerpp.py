from talon import Module, Context

mod = Module()

mod.apps.explorerpp = r"""
os: windows
and app.name: Explorer++
os: windows
and app.exe: /^explorer\+\+\.exe$/i
"""

ctx = Context()


@mod.action_class
class FileManager:
    pass
