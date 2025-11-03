#custom balatro commands go here
#https://github.com/emmapixels/community/blob/a6edc6dc77fe5c034a93eb87d8474b75f4177fc2/apps/balatro/balatro.talon
app: balatro
os: windows

-
settings():
    key_hold = 20
    key_wait = 20

shift right: key("=")
shift left: key("-")
discard: key(backspace)
(use|open): key(enter)
play hand: key(enter)
select blind: key(enter)
buy card: key(enter)
cash out: key(enter)
(by|buy) and use: key("p")
go hand:  key(".")
go jokers:  key(";")
go consumables:  key("'")
go pack:  key(",")
shop jokers:  key("\\")
shop vouchers:  key("[")
shop (booster|pack):  key("]")
left:  key(left)
right:  key(right)
deselect:  key("/")
reroll:  key(tab)
sell card:  key("q")
sort suit:  key("x")
sort rank:  key("z")
deck:  key("o")
next round: key(backspace)
skip this: key(backspace)
ten: key("0")