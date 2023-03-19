def oblicz_netto(cena_brutto, stawka_podatku) -> float:
    """Oblicza cenę netto na podstawie ceny brutto i stawki podatku.
    
    Argumenty:
    cena_brutto -- cena brutto
    stawka_podatku -- stawka podatku w procentach
    """
    return cena_brutto / (1.0 + stawka_podatku / 100.0)

# Testy ----------------------------

# print(oblicz_netto(100, 23)) # 81.30081300813008
# print(oblicz_netto(100, 8)) # 92.59259259259258