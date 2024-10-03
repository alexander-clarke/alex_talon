from talon import Module

mod = Module()
mod.list("unreal_ufunction_specifiers", desc="Unreal function specifiers")

@mod.capture(rule="{user.unreal_ufunction_specifiers}+")
def ufunction_specifiers(m) -> str:
    """A sequence of unreal engine ufunction specifiers"""
    return ", ".join(m.unreal_ufunction_specifiers_list)