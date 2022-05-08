"""Création d'un algo K plus proche voisins pour définir en fonctions d'informations les chances de survie d'un passager du Titanic"""

##########################################

from cProfile import label
from turtle import color, colormode
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
    "Survived",
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

    
"""Equilibre des amplitudes"""

diviseurs = []

def clef(tab):
    return tab[key]

for key in keys:
    minimum = min(passagers,key=clef)[key]
    maximum = max(passagers,key=clef)[key]
    diviseur = maximum - minimum
    diviseurs.append(diviseur)
    for passager in passagers:
        passager[key] = passager[key] / diviseur


def mystere():
    """Création du billet mystère"""
    PC = float(input("Pclass :\n>>>")) / diviseurs[0]# on renseigne les variables
    SEX = float(input("SEX :\n>>>")) / diviseurs[1]
    AGE = float(input("AGE :\n>>>")) / diviseurs[2]
    SS = float(input("SibSp :\n>>>")) / diviseurs[3]
    PAR = float(input("Parch :\n>>>")) / diviseurs[4]
    FARE = float(input("Fare :\n>>>")) / diviseurs[5]
    EMB = float(input("Embarked :\n>>>")) / diviseurs[6]

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

for i in range(len(keys)-1): # pour chaque indice principale
    for j in range(i+1,len(keys)-1): # comparaison avec indice secondaire
        PointMyst = (passagerMystere[i],passagerMystere[j]) # coordonnées du passager mystère
        for passager in passagers_distance: # pour chaque passager de la liste
            point = (passager[keys[i]], passager[keys[j]]) # point du passager déjà connu
            passager["distance"] += distance(PointMyst,point) # calcul de la distance

def tri_distance(tab): # définition de la clé de tri
    return tab["distance"]

passagers_distance_tri = sorted(passagers_distance,key=tri_distance) # tri de la liste des distances

def TitanicPassagers(tab,k): # définition qui va déterminer les K plus proches voisins

    temp = tab[:k] # on coupe la liste à K

    SurvivedTitanic = [] # création de la liste des passagers récupérés
    for passager in temp: # pour chaque passager présent dans la liste 'temp' on ajoute à la nouvelle liste crée
        SurvivedTitanic.append(passager)

    return SurvivedTitanic # renvoie de la liste

"""Compter le nombre d'occurence de voisins"""

voisins = TitanicPassagers(passagers_distance_tri,int(input("Veuillez rentrer une valeur de 'K' !\n>>>")))

Survived = 0 # déclaration des vars et mise à zéro
Dead = 0

for passager in voisins:
    if passager["Survived"] == 1:
        Survived += 1
    else:
        Dead += 1
    
SurvivedList = { # création d'un dictionnaire pour ranger les valeurs par type
    "survivant" : Survived,
    "mort" : Dead,
}

ValueMax = 0 # déclaration des vars
SurDead = ""

for key,element in SurvivedList.items():
    if element > ValueMax:
        ValueMax = element
        SurDead = key

print("Le passager est déclaré :",SurDead,"avec pour 'K' plus proche voisins :",ValueMax)


##############################################################################
#                                  Graph                                     #
##############################################################################

survivant = [] # création de la liste des survivants
nonsurvivant = [] # création de la liste des nonsurvivants

for passager in passagers: # pour chaque passager dans la liste
    if passager["Survived"] == 1: # si le passager est un survivant on l'ajoute aux survivants
        survivant.append(passager)
    else: # sinon on l'ajoute aux nonsurvivants
        nonsurvivant.append(passager)

for i in range(len(keys)-1): # pour chaque indice de key (1 par 1)

    xSurvivant = [] # déclaration et mise à zéro des listes
    ySurvivant = []
    xNonSurvivant = []
    yNonSurvivant = []

    for j in range(i+1,len(keys)-1):

        for z in range(len(survivant)):

            xSurvivant.append(survivant[z][keys[i]])
            ySurvivant.append(survivant[z][keys[j]])

        for z in range(len(nonsurvivant)):

            xNonSurvivant.append(nonsurvivant[z][keys[i]])
            yNonSurvivant.append(nonsurvivant[z][keys[j]])

        xPassagerMyst = passagerMystere[i]
        yPassagerMyst = passagerMystere[j]

        plt.plot(xSurvivant,ySurvivant,"ro",color="blue",label="Survivant")
        plt.plot(xNonSurvivant,yNonSurvivant,"ro",color="red",label="Non survivant")
        plt.plot(xPassagerMyst,yPassagerMyst,"ro",color="black",label="Patient mystère")
        plt.xlabel(str(keys[i]))
        plt.ylabel(str(keys[j]))
        plt.legend()

        plt.show()

##############################################################################    


