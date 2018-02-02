from behave.runner import Context
from click.testing import CliRunner


def before_all(context: Context):
    context.cli = CliRunner()
