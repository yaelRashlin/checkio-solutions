def days_diff(a, b):
    import datetime
    x = datetime.datetime(a[0], a[1], a[2])
    y = datetime.datetime(b[0], b[1], b[2])
    
    if x > y:
        diff = x - y
    else:
        diff = y - x
    return diff.days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
