from talon import Module, actions, Context

mod = Module()

ctx = Context()
ctx.matches = r"""
code.language: c
code.language: cpp
"""

mod.list("ue_types", desc="ue types")
ctx.lists["self.ue_types"] = {
    "actor": "AActor",
    "subclass": "TSubclassOf<",
    "soft object pointer": "FSoftObjectPtr<",
    "array": "TArray<",
    "transform": "FTransform",
    "vector": "FVector",
    "name": "FName",
}

mod.list("unreal_log_verbosity", desc="Unreal log verbosity")

mod.list("unreal_ufunction_specifiers", desc="Unreal function specifiers")
mod.list("unreal_uproperty_specifiers", desc="Unreal uproperty specifiers")


@mod.capture(rule="{user.unreal_ufunction_specifiers}+")
def ufunction_specifiers(m) -> str:
    """A sequence of unreal engine ufunction specifiers"""
    return ", ".join(m.unreal_ufunction_specifiers_list)


@mod.capture(rule="Cat <user.text>")
def uspecifiers_category(m) -> str:
    """A category to be added to a specifier list"""
    return f'Category="{actions.user.formatted_text(m.text, "CAPITALIZE_ALL_WORDS")}"'


@mod.capture(rule="(<user.uspecifiers_category> | {user.unreal_uproperty_specifiers})")
def uproperty_specifier(m) -> str:
    return m.uspecifiers_category or m.unreal_uproperty_specifiers


@mod.capture(rule="<user.uproperty_specifier>+")
def uproperty_specifiers(m) -> str:
    """A sequence of unreal engine uproperty specifiers"""
    return ", ".join(m.uproperty_specifier_list)


mod.list("unreal_delegate_dynamic", "unreal delegate dynamic")
mod.list("unreal_delegate_multicast", "unreal delegate multicast")
mod.list("unreal_delegate_param_count", "unreal delegate parameter count")


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
