"""Operations sur une matrice"""


#Le determinant d'une matrice

def determinant_2(m = [[], []]):
    "Determinant d'une matrice 2x2"

    if len(m[0]) != 2 or len(m[1]) != 2:
        return None
    else:
        det = m[0][0]*m[1][1] - m[1][0]*m[0][1]
        return det

#Inverse d'une matrice

def inverse_2(m = [[], []]):
    "Calcul l'invers d'une matrice"

    det = determinant_2(m)
    if det and det!= 0:
        inv = [[1/det*m[0][0], 1/det*m[0][1]], [1/det*m[1][0], 1/det*m[1][1]]]
        return inv
    else:
        return None

#La trace d'une matrice

def trace(m = []):
    "Somme des termes de la diagonale"
    tr = 0
    for i in range(0, len(m), 1):
        tr = tr  + m[i][i]
    return tr
            
