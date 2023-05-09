import math

# Seitenlänge a vom Benutzer abfragen
a = float(input("Gib die Seitenlänge des Quadrats ein: "))

# Radius des umschreibenden Kreises berechnen
r = a * math.sqrt(2) / 2

# Ergebnis ausgeben
print("Der Radius des umschreibenden Kreises beträgt:", r)