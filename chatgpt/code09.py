from chatgpt.code04 import genererPossibles
from chatgpt.code07 import propositionIA
from chatgpt.code08 import filtrerImpossibles


def choixSecretHumain(taille, couleurs):
    code = []
    print("votre combianaison secrète?")
    while len(code) < taille:
        print("choix de la couleur :", end="")
        for i in range(len(couleurs)):
            print(i,"->",couleurs[i]," ",end="")
        numeroCouleur = int(input())
        if numeroCouleur>=0 and numeroCouleur<len(couleurs):
            code.append(couleurs[numeroCouleur])
        else:
            print("erreur de saisie!")
    return code
 
def evaluerHumain(hypothese, secret):
    print("votre combinaison secrete est :", secret)
    print("proposition de votre adversaire:", hypothese)
    nbp = int(input("combien de bien places?"))
    nmp = int(input("combien de mal places?"))
    return (nbp,nmp)
            
def jouerCodeurHumain(nbPions = 4,couleurs = ["Rouge","Vert","Bleu","Gris","Orange","Rose"], maxEssais = 10):
    code = choixSecretHumain(nbPions,couleurs)
    possibles = genererPossibles(nbPions,couleurs)
    nbEssais = 0
    gagne = False
    while not gagne and nbEssais <maxEssais :
        combinaison = propositionIA(possibles)
        print(combinaison)
        bp,mp = evaluerHumain(combinaison,code)
        print("il y a ",bp,"pions bien places et ",mp,"pions mal places")
        nbEssais+=1
        if bp == nbPions:
            gagne = True
        filtrerImpossibles(combinaison, (bp,mp), possibles)
    if gagne:
        print("L'IA a trouve votre combinaison secrete en ", nbEssais, "coups")
    else:
        print("Bravo l'IA n'a pas trouve combinaison secrete qui etait:", code)
        
jouerCodeurHumain()
