os: windows
and app.name: Hacknet
os: windows
and app.exe: Hacknet.exe
-

tag(): user.generic_windows_shell
tag(): terminal

probe:
  insert('probe\n')

ssh hack [<number_small>]:
  insert('SSHcrack {number_small or "22"}\n')

ftp hack [<numbers_small>]:
  insert('FTPBounce {number_small or "21"}\n')

Smtp hack:
  insert('SMTPoverflow 25\n')

web hack:
  insert('WebServerWorm 80\n')

port hack:
  insert('PortHack\n')

sql hack:
  insert('SQL_MemCorrupt 1433\n')

med hack:
  insert('KBT_PortTest 104\n')

mail:
  insert('connect JMail.com\n')

shall|shell:
  insert('shell\n')

analyze:
  insert('analyze\n')

solve:
  insert('solve ')

Decypher:
  insert('Decypher ')

trace kill:
  insert('TraceKill\n')

reboot:
  insert('reboot -i\n')

disconnect| (dee cee):
  insert('dc\n')

settings():
  key_wait= 20
  key_hold= 20