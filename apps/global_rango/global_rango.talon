not tag: browser
-

tab hunt <user.text>:
    user.focus_default_browser()
    user.rango_command_without_target("focusTabByText", text)

visit {user.website}:
    user.focus_default_browser()
    user.rango_command_without_target("focusOrCreateTabByUrl", website)

slot <user.rango_tab_target>:
    user.focus_default_browser()
    user.rango_activate_tab(rango_tab_target)
