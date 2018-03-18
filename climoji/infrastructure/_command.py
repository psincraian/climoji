import click

from climoji.domain.exception import DomainException
from climoji.infrastructure import container


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


@cli.command()
@click.argument('word')
def search(word: str):
    emojis = container.finder().search(word)
    for pos, emoji in enumerate(emojis):
        click.echo('[{}] {}  - {}'.format(pos + 1, emoji.emoji, emoji.alias))
