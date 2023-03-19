import unittest

import funkcja_obliczajaca_netto
import kolejka_fifo
import obiekt_zajecia
import procedura_dopisujaca_dane

class Testy(unittest.TestCase):

    def test_funkcja_obliczajaca_netto(self):
        self.assertEqual(funkcja_obliczajaca_netto.oblicz_netto(100, 23), 81.30081300813008)
        self.assertEqual(funkcja_obliczajaca_netto.oblicz_netto(100, 8), 92.59259259259258)

    def test_kolejka_fifo(self):
        self.assertEqual(kolejka_fifo.kolejka, [])
        self.assertEqual(kolejka_fifo.pobierz_z_kolejki(), None)
        kolejka_fifo.dodaj_do_kolejki(1)
        kolejka_fifo.dodaj_do_kolejki(2)
        self.assertEqual(kolejka_fifo.pobierz_z_kolejki(), 1)
        self.assertEqual(kolejka_fifo.pobierz_z_kolejki(), 2)
        self.assertEqual(kolejka_fifo.pobierz_z_kolejki(), None)

    def test_obiekt_zajecia(self):
        zajecia = obiekt_zajecia.Zajecia("Pracownia programowania IV")
        self.assertEqual(zajecia.studenci, [])
        zajecia.zapisz_studenta("Student A")
        zajecia.zapisz_studenta("Student B")
        zajecia.zapisz_studenta("Student C")
        zajecia.zapisz_studenta("Student D")
        zajecia.zapisz_studenta("Student E")
        zajecia.zapisz_studenta("Student F")
        zajecia.zapisz_studenta("Student G")
        zajecia.zapisz_studenta("Student H")
        zajecia.zapisz_studenta("Student I")
        zajecia.zapisz_studenta("Student J")
        self.assertEqual(zajecia.studenci, ['Student A', 'Student B', 'Student C', 'Student D', 'Student E', 'Student F', 'Student G', 'Student H', 'Student I', 'Student J'])
        with self.assertRaises(Exception):
            zajecia.zapisz_studenta("Student K")

    def test_procedura_dopisujaca_dane(self):
        with open("dane.txt", "r") as plik:
            ostatnia_linijka = plik.readlines()[-1]
        self.assertEqual(ostatnia_linijka, "Testowy ciąg znaków")
        

if __name__ == '__main__':
    unittest.main()