#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # Afficher le nombre d'arguments
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print(f"{arguments} arguments:")
    for count in range(arguments):
        # Afficher chaque argument avec son numéro
        print(f"{count + 1}: {sys.argv[count + 1]}")
