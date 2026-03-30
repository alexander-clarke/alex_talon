from talon import Module, app, actions, Context, settings

ctx = Context()

ctx.matches = r"""
os: linux
"""


@ctx.action_class("user")
class Actions:
    def audio_set_default_in(audio_list_item: str):
        """"""
        actions.user.system_command(
            f'pacmd set-default-source "{audio_list_item.split(",")[1]}" | index'
        )

    def audio_set_default_out(audio_list_item: str):
        """"""
        actions.user.system_command(
            f'pacmd set-default-sink "{audio_list_item.split(",")[0]}" | index'
        )
