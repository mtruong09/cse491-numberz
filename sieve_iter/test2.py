# test that the next prime higher than 10 is 11

import sieve

def test2():
    s = sieve.sieve()
    i = iter(s)
    for x in sieve.sieve():
        if x > 10:
            break
    assert x == 11
    print x

test2()
