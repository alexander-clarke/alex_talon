from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.host: www.reddit.com
browser.host: old.reddit.com
# win.title: /reddit/
"""

mod = Module()

mod.list("reddit_sort_type", desc="reddit sort type")

@mod.action_class
class Action:
  def reddit_slideshow():
    ''''''
    address = actions.browser.address()
    pre, reddit, post = address.partition("reddit")
    actions.browser.go(pre+reddit+"px"+post)
    
  def reddit_sort(sort_mode: str = "top"):
    ''''''
    address = actions.browser.address()    
    actions.browser.go(address + "top/?t=month")
    
    
  def reddit_go_old():
    ''''''
    address = actions.browser.address()
    address = address.replace("www", "old")
    address = address.replace("new", "old")
    actions.browser.go(address)
    
    
        