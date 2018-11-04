
import random

def main():
    questionCount = 10
    correctResults = 0
    print("Test d'addition. Combien de chiffres voulez-vous?")
    chiffre = int(input())
    if chiffre == 1:
        maxValue = 10
    elif chiffre == 2:
        maxValue = 100
    elif chiffre == 3:
        maxValue = 1000

    for i in range(1, questionCount+1):
        a = random.randrange(0, maxValue)
        b = random.randrange(0, maxValue)
        r = a + b
        print("%d: que vaut %d + %d ?"%(i, a, b))
        user_result_string = input()
        user_number = int(user_result_string)
        if user_number == r:
            correctResults += 1
            print("correct. score :  %d/%d"%(correctResults,i))
        else:
            print("désole, mais %d + %d vaut %d et non %s. score : %d/%d"%(a,b,r,user_result_string, correctResults, i))
        print("")
    print("bravo, mais fais attention, ce sera plus compliqué la prochaine fois.")
    pct_correct = 100 * correctResults / questionCount
    if pct_correct == 100:
        commentaire = "parfait, t'es le boss"
    elif pct_correct > 80:
        commentaire = "vraiment pas mal"
    elif pct_correct > 50:
        commentaire = "tu feras mieux la prochaine fois"
    else:
        commentaire = "retourne à la maternelle"
    print("ton score est de %d%%. %s."%(pct_correct, commentaire))
main()