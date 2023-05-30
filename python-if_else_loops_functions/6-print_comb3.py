#!/usr/bin/python3
for dizaine in range(0, 9): # Parcours les dizaines de 0 à 8
    for unite in range(dizaine + 1, 10): # Parcours les unités de dizaine + 1 à 9
        if dizaine == 8 and unite == 9: #Verifie le dernier nombre 
            print("{:d}{:d}".format(dizaine, unite))
        else:
            print("{:d}{:d}".format(dizaine, unite), end=", ")#Sinon on imprime des nombres avc ", "