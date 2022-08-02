not mode: sleep
-
^game mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("user.game")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

