
def file_emoji_repository():
    from pymoji.infrastructure import FileEmojiRepository
    return FileEmojiRepository()


def finder():
    from pymoji.application import Finder
    return Finder(file_emoji_repository())
