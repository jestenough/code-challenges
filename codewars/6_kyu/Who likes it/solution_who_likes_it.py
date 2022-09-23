def likes(names):
    output = " like this"
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(*names)
    elif len(names) == 2:
        return "{} and {}".format(*names) + output
    elif len(names) == 3:
        return "{}, {} and {}".format(*names) + output
    elif len(names) >= 4:
        return "{}, {} and {count} others".format(*names, count=len(names) - 2) + output 
