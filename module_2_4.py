numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
for i in range (2,16):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        primes.append (i)
print ('Primes:' ,primes,)
not_primes = [i for i in range (2, 16) if i not in primes]
print ('Not primes:' ,not_primes,)


