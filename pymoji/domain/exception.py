from abc import ABCMeta, abstractmethod


class DomainException(Exception, metaclass=ABCMeta):
    @abstractmethod
    def message(self) -> str:
        pass


class EmojiNotFoundException(DomainException):
    def __init__(self, alias: str):
        self.alias = alias

    def message(self) -> str:
        return 'Emoji "{}" not found'.format(self.alias)
