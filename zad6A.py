import random
Droga= random.randint(100, 1000)
drogaKm=Droga/100
spalanie=float(input("Podaj srednie spalanie na 100km"))
cenaPaliwa=float(input("Podaj aktualna cene paliwa"))
print("Szacowany koszt podrozy",drogaKm*cenaPaliwa*spalanie)
print("Szacowane zuzycie paliwa",drogaKm*spalanie)