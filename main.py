import time

class PrzeprawaPrzezMost:
    uczestnicy = {}
    instrukcje = []

    def wczytaj_dane(self):
        for i, czas_uczestnika in enumerate(input('Podaj czasy uczestników (w minutach), oddzielając je przecinkiem: ').split(',')):
            try:
                self.uczestnicy[chr(i+97)] = int(czas_uczestnika)
            except ValueError:
                print(f'Podałeś/aś złą daną ({czas_uczestnika}), spróbuj ponownie!')
                self.uczestnicy = {}
                return self.wczytaj_dane()

    def _dodaj_do_instrukcji(self, instrukcja: list, przed: list, po: list, czas: int):
        instrukcja.append(f'{" ".join(sorted(przed)) + "  "*len(po)}{" " if len(przed) else ""}| {" ".join(sorted(po)) + "  "*len(przed)} ({czas})')

    def _wszystkie_mozliwosci_przed(self, przed: list):
        to_return = []
        for u1 in przed:
            for u2 in przed:
                if u1 == u2 or sorted([u1, u2]) in to_return:
                    continue
                to_return.append(sorted([u1, u2]))
        return to_return

    def _przesun_do_po(self, przed_kopia: list, po_kopia: list = list(), czas_kopia: int = 0, instrukcja_kopia: list = None):
        for uczestnik1, uczestnik2 in self._wszystkie_mozliwosci_przed(przed_kopia):
            po = po_kopia.copy()
            przed = przed_kopia.copy()
            czas = czas_kopia + max(self.uczestnicy[uczestnik1], self.uczestnicy[uczestnik2])
            instrukcja = instrukcja_kopia.copy() if instrukcja_kopia is not None else [' '.join(przed_kopia) + ' |']

            przed.remove(uczestnik1)
            przed.remove(uczestnik2)
            po.append(uczestnik1)
            po.append(uczestnik2)

            self._dodaj_do_instrukcji(instrukcja, przed, po, czas)

            if len(po) < len(self.uczestnicy):
                self._przesun_do_przed(przed.copy(), po.copy(), czas, instrukcja.copy()) 
            else:
                instrukcja.append(czas)
                self.instrukcje.append(instrukcja)

    def _przesun_do_przed(self, przed_kopia: list, po_kopia: list, czas_kopia: int, instrukcja_kopia: list):
        for uczestnik in po_kopia:
            po = po_kopia.copy()
            przed = przed_kopia.copy()
            czas = czas_kopia + self.uczestnicy[uczestnik]
            instrukcja = instrukcja_kopia.copy()

            po.remove(uczestnik)
            przed.append(uczestnik)

            self._dodaj_do_instrukcji(instrukcja, przed, po, czas)

            self._przesun_do_po(przed.copy(), po.copy(), czas, instrukcja.copy())

    def oblicz(self):
        self.start = time.time()
        self._przesun_do_po(list(self.uczestnicy.keys()))
        self.stop = time.time()

    def wynik(self):
        najkrotszy_czas = min(map(lambda i: i[-1], self.instrukcje))
        ile_sposobow = sum(map(lambda i: i[-1] == najkrotszy_czas, self.instrukcje))

        for uczestnik, czas in self.uczestnicy.items():
            print(uczestnik, '=', czas, end='; ')

        print(f'\nPrzeanalizowałem {len(self.instrukcje)} możliwości w {round((self.stop-self.start)*100, 2)}ms.')
        print(f'Najszybciej uczestnicy przejdą w {najkrotszy_czas}min.')
        print(f'Mogą to zrobić na {ile_sposobow} spos{"ób" if ile_sposobow == 1 else ("oby" if ile_sposobow < 5 else "obów")}.')
        
        i = 0
        for instrukcja in self.instrukcje:
            if instrukcja[-1] == najkrotszy_czas:
                i += 1
                print(f'{i}.', '-'*int(5*len(self.uczestnicy)-len(str(i))))
                print('\n'.join(instrukcja[:-1]))


zadanie = PrzeprawaPrzezMost()
zadanie.wczytaj_dane()
zadanie.oblicz()
zadanie.wynik()