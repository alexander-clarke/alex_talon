from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /atlassian.com\\/jira/
"""


mod = Module()


@mod.action_class
class UserActions:
    def jira_copy_ticket_id():
        """"""
        address: str = actions.browser.address()
        _, _, issue = address.partition("/browse/")
        actions.clip.set_text(issue)
