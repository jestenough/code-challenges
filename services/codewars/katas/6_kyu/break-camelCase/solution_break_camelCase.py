def solution(s):
    import re
    return " ".join(re.split('(?=[A-Z])', s))