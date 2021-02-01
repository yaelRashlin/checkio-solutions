def popular_words(text: str, words: list) -> dict:
    import re 
    res = {}
    for word in words:
        res[word] = len(re.findall("\s{res_word}\s|^{res_word}\s|\s{res_word}$".format(res_word = word), text, re.IGNORECASE)) or 0
    
    if res:
        return res
    return None


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
