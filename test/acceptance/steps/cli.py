from behave import when, then
from behave.runner import Context

from climoji.infrastructure import _command


@when("I make a call to {method} with {arguments}")
def step_impl(context: Context, method: str, arguments: str):
    arguments = arguments.split(' ')
    method = getattr(_command, method)
    context.result = context.cli.invoke(method, arguments)


@then("I want to see the following")
def step_impl(context: Context):
    assert context.text in context.result.output, "Get {}".format(context.result.output)
