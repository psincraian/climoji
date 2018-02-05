
def file_emoji_repository():
    from climoji.infrastructure import FileEmojiRepository
    return FileEmojiRepository()


def finder():
    from climoji.application import Finder
    return Finder(file_emoji_repository())
