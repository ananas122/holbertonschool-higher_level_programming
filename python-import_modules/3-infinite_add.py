#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
# Vérifier le nombre d'arguments stockés dans la variable num_args
    num_args = len(argv)

    resultat = sum(int(argv[i]) for i in range(1, num_args))
# Afficher le résultat
    print(f"{resultat}")
