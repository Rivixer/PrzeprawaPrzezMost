from typing import List

class PrzeprawaPrzezRzeczke:

    przed: List[int] = list()
    po: List[int] = list()
    liczba_uczestnikow: int = None
    
    def wczytaj_dane(self):
        #self.uczestnicy = [int(i) for i in input('Podaj minuty uczestników, oddzielając ich przecinkiem: ').split(',')]
        self.przed = [1, 2, 5, 10]
        self.liczba_uczestnikow = len(self.przed)

    def _wybierz_przed(self):
        for os1 in self.przed:
            for os2 in self.przed:
                if os1 == os2:
                    continue
                yield os1, os2

    def przeprowadz_przez_most(self, os1, os2):
        self.przed.remove(os1)
        self.przed.remove(os2)
        self.po.append(os1)
        self.po.append(os2)

    def _wroc_z_powrotem(self, os):
        self.po.remove(os)
        self.przed.append(os)

    def _wybierz_po(self):
        for os in self.po:
            yield os

    def sprawdz(self):
        while True:
            for os1 in self.przed:
                for os2 in self.przed:
                    if os1==os2:
                        continue
                    self.przeprowadz_przez_most(os1, os2)
                    if len(self.po) == self.liczba_uczestnikow:
                        break
                    for os in self._wybierz_po():
                        self._wroc_z_powrotem(os)
                    
                

    def pokaz_dane(self):
        print(self.uczestnicy)


zadanie = PrzeprawaPrzezRzeczke()
zadanie.wczytaj_dane()
zadanie.sprawdz()
