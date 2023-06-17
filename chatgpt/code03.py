from chatgpt.code01 import choixSecretIA
from chatgpt.code02 import evaluerIA


def propositionHumain(taille, couleurs, precedents):
    proposition = []
    for e in precedents:
        print(e)
    print("faite une proposition:")
    while len(proposition) < taille:
        print("choix de la couleur :", end="")
        for i in range(len(couleurs)):
            print(i,":",couleurs[i]," ",end="")
        numeroCouleur = int(input())
        if numeroCouleur>=0 and numeroCouleur<len(couleurs):
            proposition.append(couleurs[numeroCouleur])
        else:
            print("erreur de saisie!")
        print()
    return proposition
 
def jouerCodeurIA(nbPions = 4,couleurs = ["Rouge","Vert","Bleu","Gris","Orange","Rose"], maxEssais = 10):
    code = choixSecretIA(nbPions,couleurs)
    precedents = []
    nbEssais = 0
    gagne = False
    while not gagne and nbEssais <maxEssais :
        combinaison = propositionHumain(nbPions, couleurs,precedents)
        print(combinaison)
        bp,mp = evaluerIA(combinaison,code)
        print("il y a ",bp,"pions bien places et ",mp,"pions mal places")
        nbEssais+=1
        precedents.append((combinaison,bp,mp))
        if bp == nbPions:
            gagne = True
    if gagne:
        print("bravo vous avez trouve la combinaison secrete en ", nbEssais, "coups")
    else:
        print("vous n'avez pas trouve la combinaison secrete qui etait:", code)
