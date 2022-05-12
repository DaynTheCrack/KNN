################################

from PIL import Image # import du module "Image" de PIL
from math import sqrt # import du module "sqrt" de math

################################

"""Penser à bien changer le chemin d'accès relatif"""
path = "PY\\TP\KNN\\ImagePixKNN\\IMAGES\\bob.png" # accès chemin relatif de l'image

# récupéation de l'image initiale
img = Image.open(path)

liste_non_deg =[] # déclaraison des listes
liste_deg = []

K = int(input("Quelle est la valeur de 'K' :\n>>>")) # valeur de K pour définir le nombre de voisins

def distance(A,B): # A et B => (x,y)
    assert (len(A) == len(B) and len(A) == 2),"Il faut rentrer des coordonées du type tuple(x,y)" # vérification de la taille des valeurs

    distance_AB = sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2) # calcul de la distance euclidienne
    
    return distance_AB # renvoie de la listance euclidienne

def clef(tab): # def de la clef => "key=" de sorted
    return tab["distance"]

def moyenne(tab,k): # on fait la moyenne des valeurs

    tab = tab[:k] # redéfinition de la longueur de la liste

    R = 0 # Rouge
    G = 0 # Vert
    B = 0 # Bleu
    for element in tab:
        R += element["RGB"][0] # on ajoute les valeurs pour faire la moyenne
        G += element["RGB"][1]
        B += element["RGB"][2]

    return (int(R/len(tab)),int(G/len(tab)),int(B/len(tab))) # moyenne pour K des valeurs de Rouge,Vert et Bleu

for col in range(524): # colones localisées des pixels dégradées
    for lig in range(372): # lignes localisées des picels dégradées

        RGBpix = img.getpixel((col,lig)) # (R,G,B) du pixel de coord => (col,lig)
        
        if len(RGBpix) != 3:
            RGBpix = tuple(list(RGBpix)[:len(RGBpix)-1]) # si longueur > 3 alors on modifie pour que ce soit de la forme (R,G,B)
        
        if RGBpix != (255,0,0):
            liste_non_deg.append({"coord":(col,lig),"RGB":RGBpix}) # si le pixel n'est pas rouge on ajoute à la liste 'liste_non_deg'
        else:
            liste_deg.append({"coord":(col,lig),"RGB":RGBpix}) # au contraire si le pixel est rouge on ajoute à la liste 'liste_deg' 

for Redpix in liste_deg: # pour chaque pixel rouge

    liste_distance = list(liste_non_deg) # liste avec distance remise à zéro pour chaque passage
    
    for Notredpix in liste_distance:
        Notredpix["distance"] = distance(Redpix["coord"],Notredpix["coord"]) # on ajoute les distances

    liste_distance_tri = sorted(liste_distance,key=clef) # tri de la liste avec la clef 

    Moy = moyenne(liste_distance_tri,K) # calcul de la moyenne (R,G,B)
    
    img.putpixel(Redpix["coord"],Moy) # on change la couleur du pixel par la moyenne calculée pour les composantes 

img.save(input("Entrer le nom du fichier sans le format :\n>>>")+".png")
