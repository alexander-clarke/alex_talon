from talon import Module, actions

mod = Module()
mod.list("unreal_ufunction_specifiers", desc="Unreal function specifiers")


@mod.capture(rule="{user.unreal_ufunction_specifiers}+")
def ufunction_specifiers(m) -> str:
    """A sequence of unreal engine ufunction specifiers"""
    return ", ".join(m.unreal_ufunction_specifiers_list)


mod.list("unreal_uproperty_specifiers", desc="Unreal uproperty specifiers")


@mod.capture(rule="{user.unreal_uproperty_specifiers}+")
def uproperty_specifiers(m) -> str:
    """A sequence of unreal engine uproperty specifiers"""
    return ", ".join(m.unreal_uproperty_specifiers_list)


@mod.action_class
class Actions:
    def smart_insert_specifiers(uproperty_specifiers: str):
        """"""
        before, after = actions.user.dictation_peek(True, True)
        no_whitespace = "".join(before.split())
        last_character = no_whitespace[-1]
        if last_character == "(" or last_character == ",":
            actions.insert(uproperty_specifiers)
        else:
            actions.insert(f", {uproperty_specifiers}")
        after_first_char = "".join(after.split())[0]
        if after_first_char != ")" and after_first_char != ",":
            actions.insert(", ")
