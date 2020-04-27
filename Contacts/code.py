                             ###############  MES FONCTIONS ################### 


def verifier_numero(numero):#done
    "Pour verifier si le numero existe deja"
    confirmer = False
    with open("fichier_contacts","r") as fichier_contacts:
        for line in fichier_contacts:
            if numero in line:
                confirmer = True
    return confirmer


def ajouter_contact(nom, numero):#done  
    "Pour creer un contact"
    if len(numero) != 9:
        raise ValueError("Le numero doit etre a 9 chiffres")
    elif verifier_numero(numero)==False:
        with open("fichier_contacts","a") as fichier_contacts, open("fichier_numero","a") as fichier_numero:
            contact = numero," ", nom
            fichier_contacts.write(' '.join(contact) + '\n')
            fichier_numero.write(''.join(numero) + '\n')
            print("Bien enreigistre!")
    else:
        raise ValueError("Le contact existe deja!!!")
    

def modifier_nom(numero, nouveau_nom): #done
    "Pour modifier le nom d\'un comtact"
    supprimer_contact(numero)
    ajouter_contact(nouveau_nom, numero)
    
def modifier_numero(ancien_numero, nouveau_numero, nom): #done
    "Pour modifier le numero d\' un contact"
    supprimer_contact(ancien_numero)
    ajouter_contact(nom, nouveau_numero)
    
def modifier_n_n(ancien_numero, nouveau_numero ,nouveau_nom):#done
    "pour modifier le nom et le numero du contact"
    supprimer_contact(ancien_numero)
    ajouter_contact(nouveau_nom, nouveau_numero)

def supprimer_contact(numero_contact): #done done 
    "Pour supprimer un contact"
    if verifier_numero(numero_contact):
        file = open('fichier_contacts','r')
        lines = file.readlines() # ou lines = file.split('\n')
        new_lines = list()
        for line in lines:
            if numero_contact not in line:
                new_lines.append(line)
        file.close()
        file = open('fichier_contacts', 'w')
        file.write("\r\n".join(new_lines))
        file.close()
        #print("Contact bien supprime!!!")
    else:
        raise ValueError("Ce numero n'exite pas")

def afficher_repertoir():#done done
    "afficher tous les contacts "
    with open("fichier_contacts","r") as fichier_contacts:
        fichier_contacts.seek(0) #on verifie si nous sommes ai debut du fichier
        first_char = fichier_contacts.read(1) #on recupere le premier caratere
        if not first_char:
            print("Vous n'avez encore aucun contact")
        else:
            for line in fichier_contacts:
                print(line)
            