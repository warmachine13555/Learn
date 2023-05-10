import csv

#vars
preis_gesamt = 0
waregp_a_preis = 0
waregp_b_preis = 0
waregp_c_preis = 0

einkauf = []


#get data from csv
with open('Kassenbericht.csv', 'r') as datafile:
    for line in datafile:
        einkauf.append(line.replace('\n', ""))

print(einkauf)

warengruppe_a = {

    'Bananen': 1.50,
    'Mehl': 0.50

}

warengruppe_b = {

    'Mineralwasser': 3.00,
    'Cola': 2.50

}

warengruppe_c = {

    'Backpapier': 1.00,
    'Bleistifte': 2.50

}


#Menge aller verkauften Artikel

print(f"Es wurden insgesamt {len(einkauf)} Artikel verkauft")

#Summe aller Verkäufe

for warevk in einkauf:

    preis_get_a = warengruppe_a.get(warevk, 0)
    preis_get_b = warengruppe_b.get(warevk, 0)
    preis_get_c = warengruppe_c.get(warevk, 0)

    preis_gesamt_dazu = preis_get_a + preis_get_b + preis_get_c
    preis_gesamt = preis_gesamt_dazu + preis_gesamt

print(f"Insgesamt haben die Artikel {preis_gesamt} € gekostet.")

#Summe der Verkäufe nach Warengruppe

for waregp_a in einkauf:

    waregp_a_dazu = warengruppe_a.get(waregp_a, 0)
    waregp_a_preis = waregp_a_preis + waregp_a_dazu

for waregp_b in einkauf:

    waregp_b_dazu = warengruppe_b.get(waregp_b, 0)
    waregp_b_preis = waregp_b_preis + waregp_b_dazu

for waregp_c in einkauf:

    waregp_c_dazu = warengruppe_c.get(waregp_c, 0)
    waregp_c_preis = waregp_c_preis + waregp_c_dazu

print(f"Die kosten der verschiedenen Warengruppen sind wie folgt Gruppe A {waregp_a_preis} €, Gruppe B {waregp_b_preis} € "
      f"und Gruppe C {waregp_c_preis} €.")

