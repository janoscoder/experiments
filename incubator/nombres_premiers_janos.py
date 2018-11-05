def is_divisible_by_any(m, primes):
    for p in primes:
        if m % p == 0:
            return True
        if p*p > m:
            return False
    return False

def gen_primes(n):
    if n < 2:
        return []
    primes = [2]
    for i in range(3, n+1, 2):
        if not is_divisible_by_any(i, primes):
            primes.append(i)
            #print(i)
    return primes

ps = gen_primes(1000000)
print(ps[-1])
