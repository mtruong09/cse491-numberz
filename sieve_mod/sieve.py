# this is an implementation of the 'sieve' functionality using a module

primeslist = [2]

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
        return True

def next():
    global primeslist
    start = primeslist[-1] + 1
    while 1:
        if _is_prime(primeslist, start):
            primeslist.append(start)
            return start
        
        start += 1
                                                            
