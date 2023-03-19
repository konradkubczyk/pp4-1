import os.path

if __name__ == '__main__':
    ciag_znakow = input("Podaj ciąg znaków: ")
else:
    ciag_znakow = "Testowy ciąg znaków"

with open("dane.txt", "a") as plik:
    # Nowa linia jest dodawana tylko gdy plik nie jest pusty, by ilość linii była równa ilości wprowadzonych ciągów znaków
    if os.path.getsize("dane.txt") > 0:
        plik.write("\n")
        
    plik.write(ciag_znakow)
