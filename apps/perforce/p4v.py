from talon import Module

mod = Module()

mod.apps.perforce = r"""
os: windows
and app.name: Helix Visual Client (P4V)
os: windows
and app.exe: /^p4v\.exe$/i
"""