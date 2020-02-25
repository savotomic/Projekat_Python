class Set:

    def __init__(self):
        self.rezultat = {}

    def presek(self, prvaRec, drugaRec):

        for stranica1, rang1 in prvaRec.items():
            for stranica2, rang2 in drugaRec.items():
                if stranica1 == stranica2:
                    self.rezultat[stranica1] = rang1 + rang2

    def unija(self, prvaRec, drugaRec):

        for stranica1, value in prvaRec.items():
            for stranica2, value2 in drugaRec.items():
                if stranica1 == stranica2:
                    self.rezultat[stranica1] = value + value2

        for stranica1, value in prvaRec.items():
            if stranica1 not in drugaRec:
                self.rezultat[stranica1] = value

        for stranica2, value in drugaRec.items():
            if stranica2 not in prvaRec:
                self.rezultat[stranica2] = value

    def komplement(self, prvaRec, drugaRec):

        for stranica1, rang in prvaRec.items():
            if stranica1 not in drugaRec:
                self.rezultat[stranica1] = rang

