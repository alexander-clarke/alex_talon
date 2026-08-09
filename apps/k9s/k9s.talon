app: k9s
-
command {user.kubectl_object}:
    insert(":{kubectl_object}\n")

cube filter: insert("/")
cube filter <user.text>:
    insert("/{text}\n")

cube logs: key(l)
cube describe: key(d)
cube shell: key(s)
cube edit: key(e)
cube quit: ":q\n"
cube port forward: key(ctrl-f)
