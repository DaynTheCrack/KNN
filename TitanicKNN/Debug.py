dictionnaire = [
    {"Nom" : 8,"Prénom" : 50},
    {"Nom" : 6, "Prénom" : 100}
]

keys = [
    "Nom",
    "Prénom",
]
def clef(tab):
    return tab[key] # rensignement de la clef directement dans la def car var global je pense
for key in keys:
    minimum = min(dictionnaire,key=clef)
    maximum = max(dictionnaire, key=clef)
    print(minimum)
    print(maximum)

var1 = minimum["Prénom"]
var2 = maximum["Prénom"]
diviseur = var2 - var1
for i in dictionnaire:
    i["Prénom"] = i["Prénom"] / diviseur
    print(i["Prénom"])
print(minimum)
print(maximum)

print(var1)
print(var2)