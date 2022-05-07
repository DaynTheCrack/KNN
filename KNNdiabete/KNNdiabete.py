"""Création d'un algo de Machine Learning en supervisée pour le diabete deviner si un patient mystère est atteint de diabete"""

########################################

import math
import csv # import de la lib 'csv'
from matplotlib import pyplot as plt # import de la lib 'pyplot'

########################################

path = "PY\TP\KNN\DiabeteKNN\diabete.csv" # chemin relatif du fichier csv pensez à bien le changer /!\

fichier = open(path,"r") # ouverture du fichier en "read"
patients = list(csv.DictReader(fichier,delimiter=",")) # on tranforme le fichier en liste

keys = [ # liste des clefs
    ' Number of times pregnant',
    ' Plasma glucose concentration a 2 hours in an oral glucose tolerance test',
    ' Diastolic blood pressure (mm Hg)',
    ' Triceps skin fold thickness (mm)',
    '2-Hour serum insulin (mu U/ml)',
    'Body mass index (weight in kg/(height in m)^2)',
    'Diabetes pedigree function',
    'Age (years)',
    ' Class variable (0 or 1)']

for patient in patients: # pour chaque patient dans la liste
    for key in keys: # pour chaque clef
        patient[key] = float(patient[key]) # convertion str to float 

def mystere():
    NP = float(input('Number of times pregnant :\n>>>')) # on rensigne les valeurs
    PG = float(input('Plasma glucose concentration a 2 hours in an oral glucose tolerance test :\n>>>'))
    DB = float(input('Diastolic blood pressure (mm Hg) :\n>>>'))
    TS = float(input('Triceps skin fold thickness (mm) :\n>>>'))
    SI = float(input('2-Hour serum insulin (mu U/ml) :\n>>>'))
    BM = float(input('Body mass index (weight in kg/(height in m)^2) :\n>>>'))
    DP = float(input('Diabetes pedigree function :\n>>>'))
    AGE = float(input('Age (years) :\n>>>'))

    return NP, PG, DB, TS, SI, BM, DP, AGE # on return les valeurs rensignées

def distance(A,B): # sous forme de tuple x,y
    assert (len(A) == len(B) and len(A) == 2),"Les points doivent comporter les coordonnées X et Y"
    
    distance_AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2) # on calcule la distance euclidienne des points

    return float(distance_AB) 

patients_distance = list(patients) # liste des distances

NewPatient = list(mystere()) # patient mystere

for patient in patients_distance: # on ajoute la clef distance
    patient["distance"] = 0


for i in range(len(keys)-1): # pour chaque indice principale
    for j in range(i+1,len(keys)-1): # comparaison avec indice secondaire
        PointMyst = (NewPatient[i],NewPatient[j]) # coordonnées du patient mystère
        for patient in patients_distance: # pour chaque patient de la liste
            point = (patient[keys[i]],patient[keys[j]]) # coordonnées des patients déjà rentrés
            patient['distance'] += distance(PointMyst,point) # ajout de la valeur


def tri_distance(tab): # key de tri
    return tab['distance']

patients_distance_tri = sorted(patients_distance,key=tri_distance) # on stock la liste triée dans une nouvelle var

def DiabetePatient(tab,k): # définition qui va déterminer suivant K les plus proches voisins

    temp =  tab[:k] # on coupe la liste à K

    IsDiabeteOrNot = [] # création de la liste des patients récupérés
    for patient in temp: # pour chaque patient présent dans la liste on ajoute dans une nouvelle var
        IsDiabeteOrNot.append(patient)

    return IsDiabeteOrNot # on retourne la liste

"""Compter le nombre d'occurence de patient"""

voisins = DiabetePatient(patients_distance_tri,int(input("Veuillez rentrer une valeur de 'K'\n>>>"))) # on détermine les plus proches voisins suivant K dans une nouvelle var

IsDiabetique = 0 # déclaration des vars et mise à zéro
IsNotDiabetique = 0

for patient in voisins:
    if patient[' Class variable (0 or 1)'] == 0: # s'il n'est pas diabétique on incrémente la var nondiabetique
        IsNotDiabetique += 1
    elif patient[' Class variable (0 or 1)'] == 1: # s'il est diabetique on incrémente la var diabetique
        IsDiabetique += 1

Diabete = { # création d'un dictionnaire pour ranger les valeurs par type
    "Diabetique" : IsDiabetique,
    "Non diabetique" : IsNotDiabetique,
}

ValueMax = 0 # déclaration des vars
IsOrNot = ""

for key,element in Diabete.items():
    if element > ValueMax:
        ValueMax = element
        IsOrNot = key

print("Le patient est déclaré :",IsOrNot," avec une majorité de 'K' plus proche voisins :",ValueMax)


##############################################################################
#                                  Graph                                     #
##############################################################################

diabetique = [] # création de la liste des diabétiques
nondiabetique = [] # création de la liste des nondiabetiques

for patient in patients: # pour chaque patient dans la liste
    if patient[' Class variable (0 or 1)'] == 1: # si le patient est diabetique on ajoute aux diabetiques
        diabetique.append(patient) # ajout
    else: # sinon on ajoute à la liste des non diabetiques
        nondiabetique.append(patient) # ajout

print(diabetique) # (DEBUG)
print("\n")
print(nondiabetique)

for i in range(len(keys)-1): # pour chaque indice de keys (1 par 1)

    xDiabete = [] # mise à zéro des vars
    yDiabete = []
    xNonDiabete = []
    yNonDiabete = []

    for j in range(i+1,len(keys)-1): # pour chaque indice supérieur (1 par 1)

        for z in range(len(diabetique)): # boucle sur longueur de la liste diabetique
            
            xDiabete.append(diabetique[z][keys[i]]) # on ajoute pour chaque menbre de diabetique la valeur de la clef[i]
            yDiabete.append(diabetique[z][keys[j]])

        for z in range(len(nondiabetique)): # idem avec non diabetique
            
            xNonDiabete.append(nondiabetique[z][keys[i]])
            yNonDiabete.append(nondiabetique[z][keys[j]])
        
        plt.scatter(xDiabete,yDiabete, c = 'red') # diabetique
        plt.scatter(xNonDiabete,yNonDiabete, c = 'blue') # non diabetique
        plt.show() # affichage

##############################################################################
