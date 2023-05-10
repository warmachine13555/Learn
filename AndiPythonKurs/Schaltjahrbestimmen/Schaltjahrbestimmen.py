'''Dieses Programm ermittelt, ob ein Jahr ein Schaltjahr ist oder nicht.'''

#Schaltjahrbestimmen
jahr = int(input("Geben Sie das jahr zum überprüfen ein."))
jahr_berechnung_durch_4 = jahr / 4
jahr_berechnung_durch_100 = jahr / 100

if jahr_berechnung_durch_4.is_integer() and not jahr_berechnung_durch_100.is_integer():
    print("Ist ein Schaltjahr.")
else:
    print("Dieses Jahr ist kein Schaltjahr.")