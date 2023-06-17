import random
def choixSecretIA(taille, couleurs):
	return [random.choice(couleurs) for x in range(taille)]
