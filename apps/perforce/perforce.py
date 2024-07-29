from talon import Module

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.tag("p4", desc="perforce commandline commands")

mod.list("p4_commands", desc="Perforce command line commands")