import random

cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ")
if cpo != 'O' and cpo != 'N':
    print("Je n'ai pas compris votre réponse")
    while cpo != 'O' and cpo != 'N':
        cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ")
        if cpo != 'O' and cpo != 'N':
            print("Je n'ai pas compris votre réponse")

if cpo == 'O':
    n1 = input("Quel est votre nom ? ")
    print(f"Bienvenu {n1} nous allons jouer ensemble \n")
    n2 = 'Machine'
else:
    n1 = input("Quel est votre nom ? ")
    print(f"Bienvenu {n1} nous allons jouer ensemble")
    n2 = input("Quel est le nom du deuxième joueur ? ")
    print(f"Bienvenu {n2} nous allons jouer ensemble \n")

def check_answer(answer: str) -> bool:
    return answer == 'pierre' or answer == 'papier' or answer == 'ciseaux' or answer == 'puit'

s1 = 0
np = 0
c = True
p2 = 0
while c:
    np += 1 
    c1 = input(f"{n1} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
    c1ok = check_answer(c1)
    if not c1ok:
        print("Je n'ai pas compris votre réponse")
        while not c1ok:
            c1 = input(f"{n1} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
            c1ok = check_answer(c1)

    if n2 == 'Machine':
        e2 = ['papier', 'pierre', 'ciseaux', 'puit'][random.randint(0, 3)]
    else:
        e2 = input(f"{n2} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
        e2ok = check_answer(e2)
        if not e2ok:
            print("Je n'ai pas compris votre réponse")
            while not e2ok:
                e2 = input(f"{n2} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
                e2ok = check_answer(e2)

    print(f"Si on récapitule : {n1} {c1} et {n2} {e2} \n")

    # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if (c1 == 'papier' and e2 == 'papier') or (c1 == 'pierre' and e2 == 'pierre') or \
       (c1 == 'ciseaux' and e2 == 'ciseaux') or (c1 == 'puit' and e2 == 'puit'):
        print("le gagnant est aucun de vous, vous être ex æquo")
        print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
    if c1 == 'pierre':
        if e2 == 'papier':
            p2 = p2 + 1
            print("le gagnant est", n2)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        elif e2 == 'puit':
            p2 = p2 + 1
            print("le gagnant est", n2)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        else:
            s1 = s1 + 1
            print("le gagnant est", n1)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
    elif c1 == 'papier':
        if e2 == 'ciseaux':
            p2 = p2 + 1
            print("le gagnant est", n2)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        elif e2 == 'puit':
            s1 = s1 + 1
            print("le gagnant est", n1)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        else:
            s1 = s1 + 1
            print("le gagnant est", n1)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
    elif c1 == 'ciseaux':
        if e2 == 'pierre':
            p2 = p2 + 1
            print("le gagnant est", n2)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        elif e2 == 'puit':
            p2 = p2 + 1
            print("le gagnant est", n2)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        else:
            s1 = s1 + 1
            print("le gagnant est", n1)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
    elif c1 == 'puit':
        if e2 == 'pierre':
            s1 = s1 + 1
            print("le gagnant est", n1)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        elif e2 == 'ciseaux':
            s1 = s1 + 1
            print("le gagnant est", n1)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")
        else:
            p2 = p2 + 1
            print("le gagnant est", n2)
            print(f"Les scores à l'issue de cette manche sont donc {n1} {s1} et {n2} {p2} \n")

    if np == 5:
        c = False
    else:
        go = input(f"Souhaitez vous refaire une partie {n1} contre {n2} ? (O/N) ")
        if go == 'N':
            c = False
        if go != 'O' and go != 'N':
            print("Vous ne répondez pas à la question, on continue ")

print("Merci d'avoir joué ! A bientôt")
