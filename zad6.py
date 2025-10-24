Droga=float(input("Podaj przebyta droge"))
drogaKm=Droga/100
spalanie=float(input("Podaj srednie spalanie na 100km"))
cenaPaliwa=6.5
print("Szacowany koszt podrozy",drogaKm*cenaPaliwa*spalanie)
print("Szacowane zuzycie paliwa",drogaKm*spalanie)