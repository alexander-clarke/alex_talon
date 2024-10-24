from talon import Module, Context, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
code.language: config
"""


@ctx.action_class("user")
class UserActions:
    def code_insert_true():
        actions.auto_insert("True")

    def code_insert_false():
        actions.auto_insert("False")

    def code_comment_line_prefix():
        actions.auto_insert("; ")

    def code_operator_assignment():
        actions.auto_insert("=")
