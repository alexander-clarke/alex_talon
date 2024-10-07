from talon import Context, actions, app, Module, cron
import time
import asyncio
ctx = Context()
mod = Module()

mod.apps.unreal = r"""
os: windows
and app.name: /UE4/
os: windows
and app.exe: /UE4Editor/
os: windows
and app.name: UnrealEditor
os: windows
and app.exe: unrealeditor.exe
"""

ctx.matches = r"""
os: windows
app: unreal
"""

mod.list("unreal_prefixes", desc="class name prefixes")

ctx.lists["user.unreal_prefixes"] = {
  "blueprint": "BP_",
  "widget blueprint": "WBP_",
  "animation blueprint": "ABP_",
  "behavior tree": "BT_",
  "static mesh": "SM_",
  "skeletal mesh": "SK_",
  "texture": "T_",
  "material instance": "MI_",
  "material": "M_",
  
  # nonstandard
  "material function": "MF_",
  "Niagara system": "NS_",
  "curve vector": "CV_",
  "curve float": "CF_",
  "editor utility": "EU_",
  # project specific
  "ziggy dialog tree": "ZDT_",
}

@mod.action_class
class Actions:
  def find_file(file_name: str):
    """Finds a file"""
    actions.key("ctrl-p")
    if file_name:
      
      def insert_file_name_text():
        actions.insert(file_name)

      cron.after("100ms", insert_file_name_text)

  def arrow_key_sequence_with_modifiers(arrows: str, modifier: str =  ""):
    ''''''
    for d in arrows.split():
      actions.key(modifier + d)