app: claude_cli
-
slash model <user.text>:
    insert("/model ")
    insert(text)
    sleep(50ms)
    key(enter)

slash add dir <user.text>:
    insert("/add-dir ")
    insert(text)
    sleep(50ms)
    key(enter)

slash MCP: "/mcp\n"

slash MCP {user.claude_mcp_actions}:
    insert("/mcp ")
    insert(user.claude_mcp_actions)
    sleep(50ms)
    key(enter)

slash subtask <user.text>:
    insert("/subtask ")
    insert(text)
    sleep(50ms)
    key(enter)

slash by the way <user.text>:
    insert("/btw ")
    insert(text)
    sleep(50ms)
    key(enter)
