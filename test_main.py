from main import add

def test1():
    assert add(1, 3) == 4

def test2():
    assert add(-2, -4) == -6

def test3():
    assert add(7, -5) == 2

if __name__ == "__main__":
    test1()
    test2()
    test3()
    print("All tests passed.")