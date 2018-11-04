import sys

toto = [4, 6, 2]
print(toto)
print(toto[1])
#toto = toto + [8, 3]
toto += [8, 3]
print(toto)
print(len(toto))
print()
for k in toto:
    print(k*k)

tutu = ["papa", "maman", 'coline', 'mahault']
for numero, nom in enumerate(tutu):
    print(numero)
    print(nom)

lulu = ["dadou", "manou", "maman", "anaïs","clément", "gaspard", "coline", "mahault", "aiden", "leo"]
for numero, nom in enumerate(lulu):
    print("la personne née en numero %d s'appelle : %s"%(numero+1, nom))

dates_de_naissance = {"dadou":1956, "manou":1957, "maman":1980, "anaïs":1982, "clément":1985, "gaspard":1988, "coline":2009, "mahault":2012, "aiden":2015, "leo": 2018}
print(dates_de_naissance["manou"])
print(dates_de_naissance["gaspard"])

annee = 1989

def calcule_l_age(nom):
    return annee - dates_de_naissance[nom]

def affiche_l_age(nom):
    print(2018 - dates_de_naissance[nom])

affiche_l_age("coline")

for nom in lulu:
    print("en %d, %s aura %d ans"%(annee, nom, calcule_l_age(nom)))

for nom1 in lulu:
    for nom2 in lulu:
        print("%s et %s ont %d ans d'écart"%(nom1, nom2, dates_de_naissance[nom1] - dates_de_naissance[nom2]) )