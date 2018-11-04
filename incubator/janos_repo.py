import sys

questions = []
questions.append(('quelle est la capitale de la france?', ['paris', 'tokyo'], 'paris'))
questions.append(('quelle est la monnaie Japonaise', ['won', 'dollar', 'euro', 'yen', 'yuan'], 'yen'))

for q in questions:
    print(q[0])
    answers = q[1]
    correct_answer = q[2]
    if len(answers) != 0:
        for idx, a in enumerate(answers):
            print("%d: %s"%(idx,a))
        #user_answer = input()
        #if (int(user_answer)
