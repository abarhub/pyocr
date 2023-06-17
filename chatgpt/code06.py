from chatgpt.code04 import genererPossibles
from chatgpt.code05 import filtrerCouleur


def stats():
    for taille in range(3,7):
        possibles = genererPossibles(taille, ["1","2","3","4","5","6"])
        print("taille initiale:", len(possibles))
        for nbp in range(0, taille +1) :
            cpos = possibles.copy()
            filtrerCouleur("1",nbp,cpos)
            print("nbp", nbp, "taille apres filtration:", len(cpos))
