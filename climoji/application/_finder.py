from climoji.domain.exception import EmojiNotFoundException
from climoji.domain.model import EmojiRepository, Emoji


class Finder:
    def __init__(self, emoji_projection: EmojiRepository):
        self._emoji_projection = emoji_projection

    def get(self, alias: str) -> Emoji:
        emoji = self._emoji_projection.find(alias)
        if emoji is None:
            raise EmojiNotFoundException(alias)
        return emoji
