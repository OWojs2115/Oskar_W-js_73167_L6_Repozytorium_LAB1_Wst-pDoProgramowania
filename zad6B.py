Droga=float(input("Podaj przebyta droge"))
drogaKm=Droga/100
spalanie=float(input("Podaj srednie spalanie na 100km"))
cenaPaliwa=6.5
print(f"Szacowany koszt podrozy{drogaKm * cenaPaliwa * spalanie}")
print(f"Szacowane zuzycie paliwa{drogaKm * spalanie}")