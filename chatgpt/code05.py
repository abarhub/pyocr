def filtrerCouleur(coul,nb,pos):
    i = 0
    while i < len(pos):    
        if (pos[i].count(coul)!=nb):
            pos.remove(pos[i])      
        else:
            i = i+1
