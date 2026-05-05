tag: terminal
-

arc [{user.arc_commands}]:
    insert("arc ")
    insert(user.arc_commands or "")

arc diff message [<user.text>]:
    insert("arc diff --message ")
    user.insert_between('"', '"')
    insert(user.text or "")
