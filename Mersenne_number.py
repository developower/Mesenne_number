def is_prime(p):
    list_ = list(range(3+1,65))
    odds = []
    initial_primes = []
    y = 0
    basic_primes = [5,7,9]
    for i in list_:
        #print(i)
        if not i % 2 == 0 and i % i == 0:
            odds.append(i)
    #print(odds)
    #print(len(odds))
    for j in odds:
        #print(j)
        if not j % 3 == 0 and not j % 5 == 0 and not j % 7 == 0 and not j % 9 == 0:
            #print(j)
            initial_primes.append(j)
    initial_primes.extend(basic_primes) 
    for k in initial_primes:
        if p == k:
            #print('Prime Number')
            return p
        else:
            print('Not a prime')
    #print(len(initial_primes))
       
print(is_prime(5))


def mersenne_num(p):
    return (2 ** p) - 1
print(mersenne_num(is_prime(5)))
    
