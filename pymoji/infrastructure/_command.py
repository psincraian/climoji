import click

from pymoji.domain.exception import DomainException
from pymoji.infrastructure import container


@click.group()
def cli():
    pass


@cli.command()
@click.argument('alias')
def show(alias):
    try:
        emoji = container.finder().get(alias)
        click.echo(emoji.emoji)
    except DomainException as e:
        click.echo(e.message())
