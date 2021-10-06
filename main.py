class PrzeprawaPrzezRzeczke:
    uczestnicy = {'a': 1, 'b': 4, 'c': 5, 'd': 10}
    przed = []
    po = []

    def wszystkie_mozliwosci_przed(self, przed: list):
        to_return = []
        for u1 in przed:
            for u2 in przed:
                if u1 == u2 or sorted([u1, u2]) in to_return:
                    continue
                to_return.append(sorted([u1, u2]))
        return to_return

    def wszystkie_mozliwosci_po(self, po: list):
        to_return = []
        for u in po:
            to_return.append(u)
        return to_return


    def start(self):
        self.przed_kopia0 = list(self.uczestnicy.keys())
        self.po_kopia0 = []
        self.czas_kopia0 = 0
        i = 0
        wyniki = []
        for i0 in self.wszystkie_mozliwosci_przed(self.przed_kopia0):
            self.przed = self.przed_kopia0.copy()
            self.po = self.po_kopia0.copy()
            self.czas = self.czas_kopia0 + max(self.uczestnicy[i0[0]], self.uczestnicy[i0[1]])
            self.przed.remove(i0[0])
            self.przed.remove(i0[1])
            self.po.append(i0[0])
            self.po.append(i0[1])
            self.przed_kopia1 = self.przed.copy()
            self.po_kopia1 = self.po.copy()
            self.czas_kopia1 = self.czas
            for i1 in self.wszystkie_mozliwosci_po(self.po_kopia1):
                self.przed = self.przed_kopia1.copy()
                self.po = self.po_kopia1.copy()
                self.czas = self.czas_kopia1 + self.uczestnicy[i1]
                self.po.remove(i1)
                self.przed.append(i1)
                self.przed_kopia2 = self.przed.copy()
                self.po_kopia2 = self.po.copy()
                self.czas_kopia2 = self.czas
                for i2 in self.wszystkie_mozliwosci_przed(self.przed_kopia2):
                    self.przed = self.przed_kopia2.copy()
                    self.po = self.po_kopia2.copy()
                    self.czas = self.czas_kopia2 + max(self.uczestnicy[i2[0]], self.uczestnicy[i2[1]])
                    self.przed.remove(i2[0])
                    self.przed.remove(i2[1])
                    self.po.append(i2[0])
                    self.po.append(i2[1])
                    self.przed_kopia3 = self.przed.copy()
                    self.po_kopia3 = self.po.copy()
                    self.czas_kopia3 = self.czas
                    for i3 in self.wszystkie_mozliwosci_po(self.po_kopia3):
                        self.przed = self.przed_kopia3.copy()
                        self.po = self.po_kopia3.copy()
                        self.czas = self.czas_kopia3 + self.uczestnicy[i3]
                        self.po.remove(i3)
                        self.przed.append(i3)
                        self.przed_kopia4 = self.przed.copy()
                        self.po_kopia4 = self.po.copy()
                        self.czas_kopia4 = self.czas
                        for i4 in self.wszystkie_mozliwosci_przed(self.przed_kopia4):
                            self.przed = self.przed_kopia4.copy()
                            self.po = self.po_kopia4.copy()
                            self.czas = self.czas_kopia4 + max(self.uczestnicy[i4[0]], self.uczestnicy[i4[1]])
                            self.przed.remove(i4[0])
                            self.przed.remove(i4[1])
                            self.po.append(i4[0])
                            self.po.append(i4[1])
                            i += 1
                            wyniki.append([i0, i1, i2, i3, i4, self.czas])

        min_czas = min(map(lambda i: i[5], wyniki))
        for wynik in wyniki:
            przed = list(self.uczestnicy.keys())
            po = []
            if wynik[5] == min_czas:
                print('------------------')
                print(f'CZAS: {min_czas}')
                print(f"{', '.join(przed)} \t| {' '.join(po)}")
                przed.remove(wynik[0][0])
                przed.remove(wynik[0][1])
                po.append(wynik[0][0])
                po.append(wynik[0][1])
                print(f"{', '.join(sorted(przed))} \t\t| {' '.join(sorted(po))}")
                po.remove(wynik[1])
                przed.append(wynik[1])
                print(f"{', '.join(sorted(przed))} \t| {' '.join(sorted(po))}")
                przed.remove(wynik[2][0])
                przed.remove(wynik[2][1])
                po.append(wynik[2][0])
                po.append(wynik[2][1])
                print(f"{', '.join(sorted(przed))} \t\t| {' '.join(sorted(po))}")
                po.remove(wynik[3])
                przed.append(wynik[3])
                print(f"{', '.join(sorted(przed))} \t\t| {' '.join(sorted(po))}")
                przed.remove(wynik[4][0])
                przed.remove(wynik[4][1])
                po.append(wynik[4][0])
                po.append(wynik[4][1])
                print(f"{', '.join(sorted(przed))} \t\t| {' '.join(sorted(po))}")
                print('------------------')


        

zadanie = PrzeprawaPrzezRzeczke()
zadanie.start()
