class Zajecia:
    studenci = []

    def __init__(self, nazwa):
        """Konstruktor klasy Zajecia
        
        Argumenty:
        nazwa -- nazwa zajęć
        """
        self.nazwa = nazwa

    def zapisz_studenta(self, student):
        """Zapisuje studenta na zajęcia, przy czym nie dopuszcza do zapisu więcej niż 10 osób
        
        Argumenty:
        student -- obiekt klasy Student
        """
        if len(self.studenci) < 10:
            self.studenci.append(student)
        else:
            raise Exception("Limit studentów na zajęcia został osiągnięty, nie można zapisać studenta")

# Testy ----------------------------

zajecia = Zajecia("Pracownia programowania IV")

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

print(zajecia.studenci) # ['Student A', 'Student B', 'Student C', 'Student D', 'Student E', 'Student F', 'Student G', 'Student H', 'Student I', 'Student J']

zajecia.zapisz_studenta("Student K") # Exception: Limit studentów zapisanych na zajęcia został osiągnięty, nie można dopisać kolejnego studenta
