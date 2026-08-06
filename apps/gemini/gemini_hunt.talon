gemini hunt <user.text>$:
    user.gemini_hunt(user.text)

gemini hunt (that | this):
    text = edit.selected_text()
    user.gemini_hunt(text)

gemini hunt clip:
    text = clip.text()
    user.gemini_hunt(text)

gemini hunt:
    user.gemini_hunt("")



