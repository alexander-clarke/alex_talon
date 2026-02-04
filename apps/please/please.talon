tag: terminal
-

# Basic commands: "please build", "please clean"
please {user.please_commands}:
    "plz "
    insert(user.please_commands)
    " "

# Nested subcommands: "please query deps", "please query graph"
please query {user.please_subcommands}:
    insert("plz query ")
    insert(user.please_subcommands)
    insert(" ")

# Quick flags: "please flag config", "please flag verbose"
please flag {user.please_flags}:
    insert(user.please_flags)

# Target shortcuts (standard Please syntax)
please target all: "//..."
please target here: ":all"
