from talon import Module, actions, app, speech_system

mod = Module()

modes = {
    "game": "limited commands just for games"
}

for key, value in modes.items():
    mod.mode(key, value)
