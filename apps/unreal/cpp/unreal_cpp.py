from talon import Module

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