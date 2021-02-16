import re

def mul(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * mul(arr[1:])
        

def checkio(number: int) -> int:
    return mul([int(i) for i in re.findall("[1-9]", str(number))])
    


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
