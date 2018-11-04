def makeItStupid(nom):
    if nom == "Coline" or nom == "Janos":
        return nom + " is wonderful"
    else:
        return nom + " is stupid"

couche = "Dadou is idiot"

print("start")
print(couche)
douche = "douche"
ceQueColineADit = douche + " " + couche
print(ceQueColineADit)
ceQueJanosDit = ceQueColineADit.replace("idiot", "funny")
print(ceQueJanosDit)

print(makeItStupid("toto"))
print(makeItStupid("Anaïs"))
print(makeItStupid("Coline"))
print(makeItStupid("Dadou"))
print(makeItStupid("Janos"))


def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n-1)

print(factorielle(10))