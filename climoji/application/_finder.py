from typing import List

import editdistance

from climoji.domain.exception import EmojiNotFoundException
from climoji.domain.model import EmojiRepository, Emoji


class Finder:
    ITEMS_TO_RETRIEVE = 5

    def __init__(self, emoji_projection: EmojiRepository):
        self._emoji_projection = emoji_projection

    def get(self, alias: str) -> Emoji:
        emoji = self._emoji_projection.find(alias)
        if emoji is None:
            raise EmojiNotFoundException(alias)
        return emoji

    def search(self, word: str) -> List[Emoji]:
        emojis = self._emoji_projection.all()
        most_similar = []
        for emoji in emojis:
            similarity = editdistance.eval(word, emoji.alias.strip(':'))
            most_similar.append((similarity, emoji))
        most_similar.sort(key=lambda t: t[0])

        return [emoji for _, emoji in most_similar[:self.ITEMS_TO_RETRIEVE]]
