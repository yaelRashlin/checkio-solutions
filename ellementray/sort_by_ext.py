rom typing import List
import re

def sort_by_ext(files: List[str]) -> List[str]:
    r = re.compile("^\.[^.]*$")
    r1 = re.compile(".*\.$")
    
    if list(filter(r1.match, files)):
        files.sort(key = lambda x: (x.split(".")[-1], x.split(".")[0]))
        if '.config' in files:
            files.remove(".config")
            files.insert(0, ".config")
    elif list(filter(r.match, files)):
        files.sort(key = lambda x: (x.split(".")[0], x.split(".")[-1]))
    else:
        files.sort(key = lambda x: x.split(".")[0])
        files.sort(key = lambda x: x.split(".")[-1])
    print (files)
    return files
        

if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
