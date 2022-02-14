import random
import time

# liste de tentatifs
tentatifs = list()

# counter : nombre de tentatifs valable
counter = 3

def num_hasard():
    """[num_hasard]
    jeu de numero mystere.
    """
    
    # numero choisi aleatoirement
    numReal = random.randint(1, 100)
    
    print("\nDevinez le nombre mystère | [taper -h ou --help pour l'aide]")   
    
    # chaque tour de boucle, je soustrais la taille du tentatifs à counter,
    # si counter == 0 j'arrete la boucle et j'affiche le message
    while True:
        rest = counter - len(tentatifs)
        if rest == 0:
            print(f"Tu as perdu ! le nombre mystère est [{numReal}]\n")
            break
        
        # j'affiche les tentations restantes
        ESSAIE = f"Tentation restante {rest}"
        print(ESSAIE)
        
        # liste de numero selectionné aleatoirement, pour afficher aux users 
        numbers = [
            numReal,
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100),
        ]
        
        # mixage de la liste
        random.shuffle(numbers)
        
        # eleminer les elements dupplicata dans la liste puis iterer et afficher
        for i in set(numbers):
            print(f"-> {i}")
            
        # recuperation de numero choisi par user et faire toutes les comparaison possible
        # et excepter tout les imprevu
        try:
            num = input("-> Numero $ ")
            if num.lower() == "show":
                print(f"\nLe nombre mystère est [{numReal}]\n")
                break
            
            elif num.lower() == "stop":
                print("\nBye !\n")
                break
            
            elif num.lower() in ["-h", "--help"]:
                with open('help.text', 'r') as h:
                    read = h.read()
                    print(read)
                    break
                    
            elif int(num) == numReal:
                print(f"\nBravo !\nTu as trouvé, c'est bien [{numReal}] le nombre mystère.\n")
                break
            
            elif int(num) > numReal:
                print(f"\n************ [{num}] est Supérieur. | [taper -h ou --help pour l'aide]\n")
                time.sleep(1)
                
            else:
                print(f"\n************ [{num}] est inférieur. | [taper -h ou --help pour l'aide]\n")
                time.sleep(1)
                
            # à la fin du boucle j'ajoute le numero saisi par user dans la liste de tentatifs
            tentatifs.append(num)
            
        except  ValueError as e:
            print(f"\nError : {e}\nSaisissez uniquement un ENTIER, SHOW ou STOP\n")

            
num_hasard()