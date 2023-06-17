from chatgpt.code02 import evaluerIA


def filtrerImpossibles(p,r,pos):
    i = 0
    while i < len(pos):
        if evaluerIA(p,pos[i])!=r:
            pos.remove(pos[i])
        else:
            i=i+1
