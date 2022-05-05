"""Création d'un algo de Machine Learning en supervisée pour le diabete deviner si un patient mystère est atteint de diabete"""

########################################

import csv # import de la lib 'csv'
from matplotlib import pyplot as plt # import de la lib 'pyplot'

########################################

path = "PY\TP\KNNdiabete\diabete.csv" # chemin relatif du fichier csv

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
print(patients)

diabetique = [] # création de la liste des diabétiques
nondiabetique = [] # création de la liste des nondiabetiques

"""for patient in patients: # pour chaque patient dans la liste
    if patient[]"""

