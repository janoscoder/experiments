def is_divisible(n, d):
    while n >= d:
        n = n - d
    return n == 0

def is_premier(n):
    for d in range(2, n):
        if is_divisible(n, d):
            return False
    return True

def affiche_nombres_premiers_jusqua(n):
    for i in range(2, n+1):
        if is_premier(i):
            print(i)

print(is_divisible(10, 3))
print(is_divisible(16, 2))
print(is_premier(45))
print(is_premier(31))
print(is_premier(91))


affiche_nombres_premiers_jusqua(100000)