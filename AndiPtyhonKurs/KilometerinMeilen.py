Kilometer = input("Geben sie die KM an, die Sie umrechnen wollen.")



Meilen = round(float(Kilometer) * float(0.621371), 2)
Seemeilen = round(float(Kilometer) * float(0.53996), 2)
SchwedischeMeilen = round(float(Kilometer) * float(0.1))


print(f"Das entspricht {Meilen} Meilen.")
print(f"Das entspricht {Seemeilen} Seemeilen.")
print(f"Das entspricht {SchwedischeMeilen} Schwedische Meilen.")