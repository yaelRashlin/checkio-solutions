def words_order(text: str, words: list) -> bool:
    import re
    if len(words) != len(set(words)):
        return False
    
    words_exists_li = re.findall((r".*\b(%s)(\b|$)" * len(words) + ".*") % tuple(words), text)
    if words_exists_li:
        words_exists_li = list(filter(None, words_exists_li[0]))
    
        if words_exists_li:
            return len(words_exists_li[0] if type(words_exists_li[0]) == tuple else words_exists_li) == len(words)
    return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    words_order("london in the capital of great britain",["london"])
    print("Coding complete? Click 'Check' to earn cool rewards!")
