from abc import ABCMeta, abstractmethod
from typing import Optional


class Emoji:
    def __init__(self, alias, emoji):
        self.emoji = emoji
        self.alias = alias


class EmojiRepository(metaclass=ABCMeta):
    @abstractmethod
    def find(self, alias: str) -> Optional[Emoji]:
        pass
