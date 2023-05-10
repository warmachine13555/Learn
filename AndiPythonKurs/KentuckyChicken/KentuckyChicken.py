'''Dieses Programm rechnet verschiedene Parameter einer Farm aus.'''

import csv

###Kentucky###

print("DAS IST DIE KENTYUCKY FRIED CHICKEN FARM\n")


#dictionary animals
cow = {"Siegfried" : 0.0, "FEE" : 10.5, "Lena" : 7.5, "Ricky" : 12.3}
chicken = {"Berta" : 1.0, "Johnny" : 0.0, "Pipa" : 0.5, "Sam" : 1.0, "Heni" : 0.8}
sheep = {"Cordula" : 3.7, "Bert" : 0.0, "Wolli" : 2.5}


#keys = cow.keys() ##Dict
keys =list(cow.keys()) ##Liste


#Zählen der Tiere in Dictionary von oben

Anzahl_cow = len(cow)
Anzahl_chicken = len(chicken)
Anzahl_sheep = len(sheep)


#Dictionary Mittelsumme Berrechnen von der Gesamtproduktion der Tiere

total_cow_production = sum(cow.values())
total_sheep_production = sum(sheep.values())
total_chicken_production = sum(chicken.values())



#Die Kuh mit der meisten Milch
maxMilchKuh = max(cow.values())
der_Name_der_Kuh_mit_der_meisten_Milch = max(cow, key=cow.get) #Name der Kuh für Output


#print(keys) #Namen der Tiere

#Anzahl der Tiere Output
print(f"{Anzahl_cow} Kuehe")
print(f"{Anzahl_chicken} Huehner")
print(f"{Anzahl_sheep} Schafe\n")

#Listen für Tiernamen zur schöneren Ausgaben
Liste_cow = list(cow.keys())
Liste_chicken = list(chicken.keys())
Liste_sheep = list(sheep.keys())

#Die Gesamtanzahl der Tiere Berrechnung
Gesamtanzahl_Tiere = Anzahl_cow + Anzahl_chicken + Anzahl_sheep


#Output
print(f"Die Gesamtanzahl der Tiere ist: {Gesamtanzahl_Tiere}\n\n")

print(f"Die Namen der Kühe sind: {Liste_cow}\n")
print(f"Die Namen der Hühner sind: {Liste_chicken}\n")
print(f"Die Namen der Schafe sind: {Liste_sheep}\n\n")

print(f"Die Kuh mit der höchsten Tages Michproduktion brachte {maxMilchKuh}\n")
print(f"Der Name der Kuh mit den meisten Liter Milch ist {der_Name_der_Kuh_mit_der_meisten_Milch}")

print(f"Die Wöchentliche Produktion der Kühe {total_cow_production} Liter")
print(f"Die Wöchentliche Produktion der Schafe {total_sheep_production} Liter")
print(f"Die Wöchentliche Produktion der Hühner {total_chicken_production} Eier")

print(f"Die Wöchentlichen Einnahmen der Kühe sind {round(total_cow_production * 0.4, 2) } €")
print(f"Die Wöchentlichen Einnahmen der Schafe sind {round(total_sheep_production * 0.3, 2) } €")
print(f"Die Wöchentlichen Einnahmen der Hühner sind {round(total_chicken_production * 0.2, 2) } €")

#for cow_value in cow.values():
# print(cow_value)