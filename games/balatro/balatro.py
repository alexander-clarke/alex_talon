from talon import Module, actions, Context

mod = Module()

mod.apps.balatro = """
os: windows
and app.exe: Balatro.exe
"""

ctx = Context() 
ctx.matches = """
os: windows
app: balatro
"""