# coding=utf-8

""" le quadrilatère (1;0), (3;0), (0;3), (0,1) est un bête trapèze isocèle,
mais votre algorithme le reconnaît comme un parallélogramme. D'ailleurs, je
vous rappelle que rectangles, losanges et carrés ne sont rien de plus que des
parallélogrammes particuliers, le test initial est donc à revoir.

Dans la même lignée, il y a bien trop de tests inutiles ou redondants que vous
pourriez éviter en imbriquant les tests les uns dans les autres. Les tests
d'inégalité peuvent notamment être évités en utilisant le SINON.

Lorsque ces quelques points auront été améliorés, vous pourrez ajouter quelques
fonctionnalités de votre choix à votre algorithme (dessin du quadrilatère,
affichage d'informations supplémentaires ou de natures différentes…)

Bonne soirée et bon courage"""

EPSILON = 0.00000000001  # imprécision du float en python
QUELCONQUE = 0
CARRE = 1
RECTANGLE = 2
LOSANGE = 3
PARALLELOGRAMME = 4
TRAPEZE = 5


def dist(pointA, pointB):
    # distance euclidienne
    return (pointA[0]-pointB[0])*(pointA[0]-pointB[0]) + (
        pointA[1]-pointB[1])*(pointA[1]-pointB[1])


def paralleles(droite1, droite2):
    """check si deux droites sont paralleles"""
    (A, C), (D, B) = droite1, droite2

    if A[0] != C[0]:
        # calcul du coeffcient directeur
        coeff_directeur_AC = (A[1] - C[1]) / (A[0] - C[0])
    else:
        # (AC) verticale, check si (BD) verticale
        return B[0] == D[0]

    if B[0] != D[0]:
        # calcul du coeffcient directeur
        coeff_directeur_BD = (B[1] - D[1]) / (B[0] - D[0])
    else:
        # (BD) verticale, check si (AC) verticale
        return A[0] != C[0]  # forcément False car déjà check avant

    # deux droites sont parallèles ssi elles ont le même coeffcient directeur
    return coeff_directeur_AC == coeff_directeur_BD


def intersection(droite1, droite2):
    """calcul le point d'inresection de deux droites
    retourne None si elles sont parallèles"""
    (A, C), (D, B) = droite1, droite2

    if paralleles(droite1, droite2):
        return None

    # K (x_K, y_K) est le point d'intersection des droites (AC) et (DB)
    # (AC) a pour équation y = E*x + F
    if A[0] != C[0]:
        E = (A[1] - C[1]) / (A[0] - C[0])
        # F = y - E*x
        F = A[1] - E * A[0]

    # (BD) a pour équation y = G*x + H
    if B[0] != D[0]:
        G = (B[1] - D[1]) / (B[0] - D[0])
        # H = y - G*x
        H = B[1] - G * B[0]

    # on ne peut pas le mettre dans un else avant car on a besoin
    # que l'équation de la droite (BD) soit définie
    if A[0] == C[0]:
        x_K = A[0]
        y_K = G * x_K + H

    # on ne peut pas le mettre dans un else avant car on a besoin
    # que l'équation de la droite (AC) soit définie
    elif B[0] == D[0]:
        x_K = B[0]
        y_K = E * x_K + F

    else:
        x_K = (H-F) / (E-G)
        y_K = E * x_K + F

    K = (x_K, y_K)
    return K


def sur_segment(point, segment):
    """ check si un point est sur un segment
    """
    (A, B) = segment
    # equation de la droite (A,B) est y = E*x+F
    if A[0] != B[0]:
        E = (A[1] - B[1]) / float((A[0] - B[0]))
        # F = y - E*x
        F = A[1] - E * A[0]

        # grace a l'équation de la droite on vérifie que le point est dessus
        # le test désiré était `if point[1] != E * point[0] + F : `
        # mais à cause de l'imprecision des floats, on considère qu'un point est
        # sur un segment s'il en est distant de moins de EPSILON (en quelque sorte)
        if not(E * point[0] + F - EPSILON <= point[1] <= E * point[0] + F + EPSILON):
            return False

    # si la droite est verticale on vérifie que le point est dessus
    else:
        if point[0] != A[0]:
            return False

    # si il l'est, on vérifie qu'il est entre les deux extrémités du segment
    return min(A[1], B[1]) <= point[1] <= max(A[1], B[1])


def convexe(pointA, pointB, pointC, pointD):
    """ test la convexité d'un quadrilatere
    """
    diagonale1 = (pointA, pointC)
    diagonale2 = (pointB, pointD)
    K = intersection(diagonale1, diagonale2)
    return K is not None and (
        sur_segment(K, diagonale1) and sur_segment(K, diagonale2)
    )


def angele_algo(pointA, pointB, pointC, pointD):
    dist_AB = dist(pointA, pointB)
    dist_BC = dist(pointC, pointB)
    dist_CD = dist(pointC, pointD)
    dist_AC = dist(pointA, pointC)
    dist_AD = dist(pointA, pointD)
    dist_DB = dist(pointD, pointB)

    if dist_AB == dist_CD and dist_AD == dist_BC:
        if dist_AC == dist_DB:
            if dist_AB == dist_BC:
                return CARRE
            else:
                return RECTANGLE
        else:
            if dist_AB == dist_BC:
                return LOSANGE
            else:
                return PARALLELOGRAMME
    else:
        return QUELCONQUE


def angele_algo2(pointA, pointB, pointC, pointD):
    dist_AB = dist(pointA, pointB)
    dist_BC = dist(pointC, pointB)
    dist_CD = dist(pointC, pointD)
    dist_AC = dist(pointA, pointC)
    dist_AD = dist(pointA, pointD)
    dist_DB = dist(pointD, pointB)

    if dist_AB == dist_CD and dist_AD == dist_BC:
        if dist_AC == dist_DB and dist_AB != dist_BC:
            return RECTANGLE
        elif dist_AC != dist_DB and dist_AB == dist_BC:
            return LOSANGE
        elif dist_AC == dist_DB and dist_AB == dist_BC:
            return CARRE
        else:
            return PARALLELOGRAMME
    else:
        return QUELCONQUE


def angele_algo3(A, B, C, D):
    dist_AB = dist(A, B)
    dist_BC = dist(C, B)
    dist_CD = dist(C, D)
    dist_AC = dist(A, C)
    dist_AD = dist(A, D)
    dist_DB = dist(D, B)

    if convexe(A, B, C, D):
        if paralleles((A, B), (D, C)) or paralleles((C, B), (D, A)):
            if dist_AB == dist_CD and dist_AD == dist_BC:
                if dist_AC == dist_DB:
                    if dist_AB == dist_BC:
                        return CARRE
                    else:
                        return RECTANGLE
                else:
                    if dist_AB == dist_BC:
                        return LOSANGE
                    else:
                        return PARALLELOGRAMME
            else:
                return TRAPEZE
    return QUELCONQUE
