def is_divisible(nombre, diviseur):
    while nombre >= diviseur:
        nombre = nombre - diviseur
    return nombre == 0 

def is_premier(u):
    for d in range(2, u):
        if is_divisible(u, d):
            return False
    return True


def affiche_les_nombres_premiers_jusqua(n):
    for w in range(2, n+1):
        if is_premier(w):
            print(w)

estceque77estprmier = is_premier(77)

print(estceque77estprmier)
print(is_premier(7))



affiche_les_nombres_premiers_jusqua(20)