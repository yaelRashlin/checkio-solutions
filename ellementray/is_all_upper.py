def is_all_upper(text: str) -> bool:
    import re
    if text.lstrip().rstrip() == "" or re.sub("[0-9]", "",  text) == '':
        return False
    return len(text) == len(re.findall("([0-9A-Z ])", text))


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
