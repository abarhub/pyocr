def genererPossibles(taille,lesCouleurs):
    reste = taille -1
    pos = [[c] for c in lesCouleurs]
        
    while reste > 0:
        pos = [[c] + e for c in lesCouleurs for e in pos]
        reste = reste -1
    return pos
