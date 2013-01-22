# this is an implementation of the 'sieve' functionality using Python's iterator functionality. here, 
# 'adder' is a class that obeys the iterator protocol


class sieve(object):
    def __init__(self):
        self.primeslist = [2]

    def __iter__(self):
        return self

    def _is_prime(self, primes, n):
    	for i in primes:
        	if n % i == 0:
	            return False
 	return True

    def next(self):
   	start = self.primeslist[-1] + 1
   	while 1:
	    if self._is_prime(self.primeslist, start):
       	        self.primeslist.append(start)
        	return start

     	    start += 1

