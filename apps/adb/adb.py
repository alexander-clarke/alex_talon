from talon import Module

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.tag("adb", desc="ADB commandline commands")

mod.list("adb_commands", desc="ADB command line commands")