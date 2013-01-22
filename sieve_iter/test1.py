# test that the second prime is 3

import sieve

def test1():
    s = sieve.sieve()
    i = iter(s)
    x = s.next()
    assert x == 3
    print x

test1()
