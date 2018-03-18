from typing import Optional, List

from climoji.domain.model import EmojiRepository, Emoji
from climoji.infrastructure._file_repository._emoji_list import EMOJI_ALIAS_UNICODE


class FileEmojiRepository(EmojiRepository):
    def find(self, alias: str) -> Optional[Emoji]:
        try:
            data = EMOJI_ALIAS_UNICODE[alias]
            return Emoji(alias, data)
        except KeyError:
            return None

    def all(self) -> List[Emoji]:
        return [Emoji(alias, data) for alias, data in EMOJI_ALIAS_UNICODE.items()]
