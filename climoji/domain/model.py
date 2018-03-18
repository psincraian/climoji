from abc import ABCMeta, abstractmethod
from typing import Optional, List


class Emoji:
    def __init__(self, alias: str, emoji):
        self.emoji = emoji
        self.alias = alias


class EmojiRepository(metaclass=ABCMeta):
    @abstractmethod
    def find(self, alias: str) -> Optional[Emoji]:
        pass

    @abstractmethod
    def all(self) -> List[Emoji]:
        pass
