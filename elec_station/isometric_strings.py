def get_di_count(str2count):
    di = {}
    for i in str2count:
        if not di.get(i):
            di[i] = 1
        else:
            di[i] = di[i] + 1
    return di

def isometric_strings(str1: str, str2: str) -> bool:
    di1 = get_di_count(str1)
    di2 = get_di_count(str2)
    return list(di1.values()) == list(di2.values())


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
