from code import *


print("#****************************************************************************************#")
print("#                        Welcome To Rell'Contact                                         # ")                             
print("#****************************************************************************************#")

print("Avec Rell'Contact vous pouvez faire beaucoup de chose \n")

val = input("Voulez commencer?o/n ")

if val=="o":
    print("Good mon ami(e) voici tout ce que vous pouvez faire avec moi\n")

    print("1->  Creer un contact")
    print("2->  Modifier le nom d'un contact")
    print("3->  Modifier le numero d'un contact")
    print("4->  Modifier le numero et le nom d'un contact")
    print("5->  Supprimer un contact")
    print("6->  Afficher mon repertoir")

    choix = input("Que souhaitez vous faire?   ")
    print("\n")
    if choix == "1":
        nom_contact = input("Entrez le nom du contact: ")
        numero_contact = input("Entrez le numro du contact: ")
        ajouter_contact(nom_contact, numero_contact)

    if choix == "2":
        numero = input("Entrez le numero du contact a modifier: ")
        nouveau_nom = input("Entrez le nouveau nom: ")
        modifier_nom(numero,nouveau_nom)

    if choix == "3":
        ancien_numero = input("Entrez le numero actuel du contact: ")
        nouveau_numero = input("Entrez le nouveau numero: ")
        nom = input("Entrez le nom actuel du contact: ")
        modifier_numero(ancien_numero, nouveau_numero, nom)

    if choix == "4":
        ancien_numero = input("Entrer le numero actuel du contact: ")
        nouveau_numero = input("Entrer le nouveau numero du contact: ")
        nouveau_nom = input("Entrez le nouveau nom: ")
        modifier_n_n(ancien_numero, nouveau_numero,nouveau_nom)

    if choix == "5":
        numero_contact = input("Entrez le numero du contact a supprimer: ")
        supprimer_contact(numero_contact)
    if choix == "6":
        print("Numeros    Noms")
        afficher_repertoir()

else:
    print("ok")
    exit()

