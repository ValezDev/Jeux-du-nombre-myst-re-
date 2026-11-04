
import random 

nombre_mystere = random.randint(1, 100)
tentative = 0
nb_user = 0

while tentative < 10 and nb_user != nombre_mystere:
    nb_user = int(input("Devine le nombre mystère : "))

    if nb_user < nombre_mystere:
        tentative += 1
        print("C'est plus grand")

    elif nb_user > nombre_mystere:
        tentative += 1
        print("C'est plus petit")

    elif nb_user == nombre_mystere:
        print("Félicitations, vous avez trouvé le nombre mystère !")
        break

else:
    print("Vous avez perdu, vous n'avez plus de tentatives.")
    print("Le nombre mystère était :", nombre_mystere)
