kolejka = []

def dodaj_do_kolejki(element):
    """Dodaje element na koniec kolejki
    
    Argumenty:
    element -- element do dodania
    """
    kolejka.append(element)

def pobierz_z_kolejki():
    """Pobiera element z początku kolejki

    Zwraca:
    element -- element z początku kolejki lub None jeśli kolejka jest pusta
    """
    if kolejka:
        return kolejka.pop(0)
    else:
        return None

# Testy ----------------------------

dodaj_do_kolejki(1)
dodaj_do_kolejki(2)
dodaj_do_kolejki(3)

print(pobierz_z_kolejki()) # 1

print(kolejka) # [2, 3]

pobierz_z_kolejki()
pobierz_z_kolejki()

print(pobierz_z_kolejki()) # None