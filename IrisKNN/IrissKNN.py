"""Création de l'algo KNN pour la liste des IRIS"""
"""/!\ pensez à bien changer le 'path' """
############################################

import csv # import de la bibliothèque 'csv'
from math import sqrt
from turtle import pensize # import du module 'sqrt' de la lib 'maths' 

#############################################

path = "PY\TP\KNN\IrisKNN\iris.csv" # chemin d'accès fichier csv

fichier = open(path,"r") # ouverture du fichier CSV 
Iris = list(csv.DictReader(fichier,delimiter=",")) # création d'une liste en transformant le fichier en liste


"""Validation de la table iris str to float"""

valeurs = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"] # stockage des clefs

for fleur in Iris: # on prend le dict de chaque fleur
    for val in valeurs: # pour chaque dans "valeurs"
        fleur[val] = float(fleur[val]) # tranformation de str ==> float


def stats_fleur(liste_fleurs, type_fleur):
    """Extrait les statistiques sous forme de tuple longueur, largeur etc..."""

    SL = [] # création des listes de chaque caractère
    SW = []
    PL = []
    PW = []

    for fleur in liste_fleurs: # pour chaque fleur dans la liste
        if fleur["Species"] == type_fleur: # si le type de la fleur de la liste est le même type que type_fleur alors on ajoute les caractèristiques
            SL.append(fleur["SepalLengthCm"])
            SW.append(fleur["SepalWidthCm"])
            PL.append(fleur["PetalLengthCm"])
            PW.append(fleur["PetalWidthCm"])
    return SL, SW, PL, PW # return sous forme de tuple les valeurs

# extraction des valeurs des trois espèces d'iris
setosa = stats_fleur(Iris,"Iris-setosa")
versi = stats_fleur(Iris,"Iris-versicolor")
virgi = stats_fleur(Iris,"Iris-virginica")


def myst():
    """Création d'une def qui contient la question est retourne le résultat finale"""
    largeurPetale = float(input("Taille de la largeur de la pétale:\n>>>"))
    longueurPetale = float(input("Taille de la longueur de la pétale:\n>>>"))
    return largeurPetale, longueurPetale

def distance(A, B):
    """Création d'une def qui permet de claculer
    la distance euclidienne entre les voisins"""

    assert (len(A) == len(B) and len(A) == 2),"les points doivent avoir deux coordonnées !" # tuple A(xA, yA) et tuple B(xB, yB) verif de la pressence de la longueur des tuples

    distance_AB = sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2) # calcul de la distance euclidienne

    return distance_AB

iris_distance = [] # distance des iris à l'iris mystère

WLiris = myst() # Tuple Width et Lenght de l'iris mystère

print(WLiris) # (DEBUG)

for fleur in Iris: # pour chaque fleur dans la liste 'iris'
    point = (fleur["PetalLengthCm"],fleur["PetalWidthCm"]) # tuple,1er valeur = Length et 2eme valeur = Width
    fleur["distance"] = distance(WLiris,point) # ajout d'une clef 'distance' pour valeur un tuple de la premiere et deuxième valeur
    iris_distance.append(fleur) # on ajoute tout dans la nouvelle liste


def tri_distance(tab):
    """Création d'une def qui permet de récupérer la clef 'distance'"""
    return tab["distance"]

iris_distance_tri = sorted(iris_distance, key=tri_distance) # rensignement de la clef

print(iris_distance_tri) # (DEBUG)

def fleur(tab, k):
    """Renvoie les espèces des k premiers fleurs de la liste triées en fonction
    de la distance à la fleur mystère."""

    temp = tab[:k] # création d'une var temp qui prend l'ensemble des valeurs de la liste jusqu'a 'k'


    espece = [] # les especes des k plus proches voisins 
    for fleur in temp:
        espece.append(fleur["Species"]) # ajout des types des fleurs retournées

    return espece 


"""Compter le nombre d'occurence"""
voisins = fleur(iris_distance_tri, int(input("Valeur de 'K'\n>>>"))) # choix de la valeur du facteur K

seto = 0 # mise à zéro des vars
versi = 0
virgi = 0

for nom in voisins:
    if nom == "Iris-versicolor":
        versi = versi + 1
    if nom == "Iris-setosa":
        seto = seto + 1
    if nom == "Iris-virginica":
        virgi = virgi + 1

typeFleursK = { # création d'un dictionnaire avec la somme des 'k' plus proche voisins par type 'key'
    "Iris-versicolor" : versi,
    "Iris-setosa" : seto,
    "Iris-virginica" : virgi,
}

ValueMax = 0 # la valeur max de présence du type d'iris
TypeMax = "" # le type de l'iris max
for key,element in typeFleursK.items(): # on cherche le max
    if element > ValueMax:
        ValueMax = element
        TypeMax = key
print("L'iris prédis est " + TypeMax + " avec pour somme des k plus proches voisins " + str(ValueMax) + "!") # (DEBUG FINALE)



    
