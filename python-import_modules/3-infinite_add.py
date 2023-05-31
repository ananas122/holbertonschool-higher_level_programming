#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
# Vérifier le nombre d'arguments stockés dans la variable num_args
    num_args = len(argv)

    resultat = 0

# Parcourir les arguments à partir de l'index 1
    for i in range(1, num_args):
        # Vérifier si l'argument est un nombre, conversion
        resultat += int(argv[i])

# Afficher le résultat
    print("{}".format(resultat))
