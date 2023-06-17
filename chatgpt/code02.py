def evaluerIA(hypothese,secret):
    nbBP = len([1 for i in range(len(secret)) if hypothese[i] == secret[i]])
    nbMP = sum([min(hypothese.count(c), secret.count(c)) for c  in set(hypothese)]) - nbBP

    return nbBP,nbMP