app: gemini_cli
-
slash chat save <user.text>:
    insert("/chat save ")
    insert(text)
    key(enter)

slash chat load <user.text>:
    insert("/chat load ")
    insert(text)
    key(enter)

slash memory add <user.text>:
    insert("/memory add ")
    insert(text)
    key(enter)

slash MCP: "/mcp\n"

slash MCP {user.gemini_mcp_servers}:
    insert("/mcp ")
    insert(user.gemini_mcp_servers)
    key(enter)

slash MCP {user.gemini_mcp_servers} auth:
    insert("/mcp ")
    insert(user.gemini_mcp_servers)
    insert(" auth")
    key(enter)
