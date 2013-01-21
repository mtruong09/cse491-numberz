last_1 = 1
last_2 = 1

def next():
    global last_1, last_2

    next_fib = last_1 + last_2 # next = 1 + 1
    last_1, last_2 = last_2, next_fib # last1 = 1, last2 = 2
    
    return next_fib

print next()
print next()
print next()
