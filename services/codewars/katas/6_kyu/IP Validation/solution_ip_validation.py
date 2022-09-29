def is_valid_IP(strng):
    if strng:
        adress = strng.split('.')
        if len(adress) == 4:
            for i in adress:
                if i.isdigit() and int(i) < 256:
                    if len(i) > 1 and i.startswith('0'):
                        return False
                    else:
                        continue
                else:
                    return False
            else:
                return True
    return False
