import fib

def test1():
    f = fib.fib()
    i = iter(f)
    x = i.next()
    assert x == 2
    print x

def test2():
    f = fib.fib()
    i = iter(f)
    i.next()
    x = i.next()
    print x
    assert x == 3
    
def test3():
    f = fib.fib()
    i = iter(f)
    i.next()
    i.next()
    x = i.next()
    assert x == 5
    print x

test1()
test2()
test3()

