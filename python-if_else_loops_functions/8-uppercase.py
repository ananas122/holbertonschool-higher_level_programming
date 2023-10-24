#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        alpha = ord(alpha)

# Vérifie si le chr est une min
        if alpha >= 97 and alpha <= 122:

# Si oui, soustrait 32 pour convertir en maj
            alpha -= 32

# Convertit la valeur ASCII en chr
        alpha = chr(alpha)
# imprime le chr
        print(f"{alpha}", end='')
    print("")