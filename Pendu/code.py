import random
"""
Principe: L'ordinateur choisit un mot au hasard dans une liste, un mot de huit lettres maximum. Le 
joueur tente de trouver les lettres composant le mot. À chaque coup, il saisit une lettre. Si la lettre 
figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. Celles qui ne le sont 
pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu​ .  
"""

liste = ["sherelle", "maurice"]

lettre = ""


def str_to_liste(l = ""):
    "permet de transformer une chaine de caractere en une liste"
    liste = []
    for el in l:
        liste.append(el)
    return liste


def list_to_str(liste = []):
    "permet de transformer une liste en une chaine de caractere"
    mot = ""
    for el in liste:
        mot = mot + el
    return mot

def remplacer(liste1 = [], liste2 = []):
    "remplace tous les elements de la liste1 qui ne sont pas dans liste2 par '*'"
    
    for el in liste1:
        if el not in liste2:
            i = liste1.index(el)
            liste1[i] = "*"
           
def jouer(liste):
    "fonction jouer"
    mot = random.choice(liste)
    chance = 8
    let = []#contient les lettres entrees par le joueur
    p1 = str_to_liste(mot)
    while chance > 0:
        p = str_to_liste(mot)
        lettre = input("Entrez la lettre: ")
        let.append(lettre)
        remplacer(p,let)
        print(list_to_str(p))
        chance -=1
jouer(liste)

   