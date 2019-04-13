CHARSET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE = 62

def convert_base62(value):
    """Converts integer to base62 string"""

    if value == 0:
        return CHARSET[0]

    result = []
    while value > 0:
        reminder = value % 62
        value = value // 62
        result.append(CHARSET[reminder])

    return ''.join(result)

def convert_from_base62(base62):
    """Converts base62 string to integer"""

    value = 0
    pow = 0
    for c in base62:
        value += CHARSET.index(c) * (BASE ** pow)
        pow += 1

    return value