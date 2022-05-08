"""Création d'un algo K plus proche voisins pour définir en fonctions d'informations les chances de survie d'un passager du Titanic"""

##########################################

from matplotlib import pyplot as plt # import du module 'pyplot' de la lib matplotlib
import math # import de la lib "math"
import csv # import de la lib "csv"

##########################################

path = "PY\\TP\\KNN\\TitanicKNN\\titanic.csv" # on défini le chemin d'accès relatif

fichier = open(path,"r") # on ouvre le fichier en mode 'read'
passagers = list(csv.DictReader(fichier,delimiter=",")) # on tranforme le fichier en liste dans une variable

keys = [ # liste des clefs
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked",
]

def deleteEmpty(dictionnaire,indice,keys):
    """Création d'une def qui permet de supprimer les infos incomplétes"""

    dictionnaire = list(dictionnaire) # transformation du type en list
    for key in keys: # pour chaque clef
        if indice[key] == "": # si la valeur de la clef est vide alors on retire le menbre de la liste
            dictionnaire.remove(indice) # on retire le menbre
            return dictionnaire # on renvoie la liste avec un menbre en moins
    return dictionnaire # on renvoie la liste sans modification

for passager in passagers: # pour chaque menbre dans la liste
    passagers = deleteEmpty(dictionnaire=passagers,indice=passager,keys=keys) # on réafecte la nouvelle liste à chaque passage
    
"""Male et Female Value"""
for passager in passagers: # on remplace les valeurs str par des valeurs float
    if passager["Sex"].lower() == "male":
        passager["Sex"] = 20.0 # male = 20
    else:
        passager["Sex"] = 10.0 # female = 10


#########
Association_Em = {
    "S" : 100,  # association de Lettres à des valeurs => "Embarked"
    "C" : 200,
    "Q" : 300,
}
#########

for passager in passagers: # pour chaque passager dans la liste on associe une valeur à une lettre

    """Embarked"""
    for key in Association_Em.keys(): # 
        if key == passager["Embarked"]:
            passager["Embarked"] = float(Association_Em[key])


    """Str to float"""
    for key in keys:
        passager[key] = float(passager[key])


def mystere():
    """Création du billet mystère"""
    PC = float(input("Pclass :\n>>>")) # on renseigne les variables
    SEX = float(input("SEX :\n>>>"))
    AGE = float(input("AGE :\n>>>"))
    SS = float(input("SibSp :\n>>>"))
    PAR = float(input("Parch :\n>>>"))
    FARE = float(input("Fare :\n>>>"))
    EMB = float(input("Embarked :\n>>>"))

    return PC, SEX, AGE, SS, PAR, FARE, EMB # return sous forme d'un tuple

def distance(A,B): # sous forme de tuple (x,y)
    """Calcul de la distance"""
    assert (len(A) == len(B) and len(A) == 2),"Les points doivent comporter les coordonées X et Y"

    distance_AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2) # distance euclidienne

    return distance_AB # on renvoie la distance    

passagerMystere = list(mystere()) # valeur du billet myestère convertion to list

passagers_distance = list(passagers) # nouvelle liste avec l'ajout des distances

for passager in passagers_distance: # création et mise à zéro d'une nouvelle clef
    passager["distance"] = 0

for i in range(len(keys)): # pour chaque indice principale
    for j in range(i+1,len(keys)): # comparaison avec indice secondaire
        PointMyst = (passagerMystere[i],passagerMystere[j]) # coordonnées du passager mystère
        for passager in passagers_distance: # pour chaque passager de la liste
            point = (passager[keys[i]], passager[keys[j]]) # point du passager déjà connu
            passager["distance"] += distance(PointMyst,point) # calcul de la distance

def tri_distance(tab): # définition de la clé de tri
    return tab["distance"]

passagers_distance_tri = sorted(passagers_distance,key=tri_distance) # tri de la liste des distances



    


