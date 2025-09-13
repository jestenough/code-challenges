import re


def strip_comments(strng, markers):
    if ms := [m for m in markers if m]:
        pat = re.compile(r'(?:' + '|'.join(map(re.escape, ms)) + r').*')
        return "\n".join(pat.sub('', i).rstrip() for i in strng.splitlines())
    return strng