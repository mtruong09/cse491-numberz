# test that the next prime higher than 151 is 157

import sieve

def test3():
    s = sieve.sieve()
    i = iter(s)
    for x in sieve.sieve():
        if x > 151:
            break
    assert x == 157
    print x

test3()
