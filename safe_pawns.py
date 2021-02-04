def safe_pawns(pawns: set) -> int:
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    t = list(pawns)
    protected = 0
    
    for pi in t:
        back_y = int(pi[1]) -1
        if pi[0] != "a" and pi[0] != "h":
            back_x_left = a[a.index(pi[0]) - 1]
            back_x_right = a[a.index(pi[0]) + 1]
            left = "%s%s" % (back_x_left, back_y)
            right = "%s%s" % (back_x_right, back_y)
            if left in t or right in t:
                protected = protected + 1
        elif pi[0] == "a":
            back_x_right = a[a.index(pi[0]) + 1]
            right = "%s%s" % (back_x_right, back_y)
            if right in t:
                protected = protected + 1
        elif pi[0] == "h":
            back_x_left = a[a.index(pi[0]) - 1]
            left = "%s%s" % (back_x_left, back_y)         
            if left in t:
                protected = protected + 1
    return protected
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"])
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
