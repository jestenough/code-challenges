def generate_hashtag(s):
    if not s:
        return False

    string = '#' + "".join(i.title() for i in s.split())

    return False if len(string) > 140 else string
