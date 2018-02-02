from typing import Optional

from pymoji.domain.model import EmojiRepository, Emoji
from pymoji.infrastructure._file_repository._emoji_list import EMOJI_ALIAS_UNICODE


class FileEmojiRepository(EmojiRepository):
    def find(self, alias: str) -> Optional[Emoji]:
        try:
            data = EMOJI_ALIAS_UNICODE[alias]
            return Emoji(alias, data)
        except KeyError:
            return None
