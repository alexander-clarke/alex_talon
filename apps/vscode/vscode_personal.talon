app: vscode
-

journal [<phrase>]: user.command_search("journal: " + user.text or "")

journal today: user.vscode("journal.today")

journal open: user.vscode("journal.open")

journal memo [<phrase>]:
    user.vscode("journal.memo")
    sleep(200ms)
    insert(user.text or "")

cursorless hats on: user.run_rpc_command("cursorless.toggleDecorations", true)
cursorless hats off: user.run_rpc_command("cursorless.toggleDecorations", false)
