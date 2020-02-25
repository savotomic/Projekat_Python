class Set:

    def __init__(self):
        self.rezultat = {}

    def presek(self,prvaRec,drugaRec):
        rezultat = {}
        for stranica1, rang1 in prvaRec.items():
            for stranica2, rang2 in drugaRec.items():
                if stranica1 == stranica2:
                    rezultat[stranica1] = rang1 + rang2

        return rezultat


    def unija(self,prvaRec,drugaRec):
        rezultat = {}

        for stranica1, rang in prvaRec.items():
            if stranica1 not in drugaRec:
                rezultat[stranica1] = rang

        for stranica1, rang1 in prvaRec.items():
            for stranica2, rang2 in drugaRec.items():
                if stranica1 == stranica2:
                    rezultat[stranica1] = rang1 + rang2

        for stranica2, rang in drugaRec.items():
            if stranica2 not in drugaRec:
                rezultat[stranica2] = rang

        return rezultat

    def komplement(self,prvaRec,drugaRec):
        rezultat = {}
        for stranica1, rang in prvaRec.items():
            if stranica1 not in drugaRec:
                rezultat[stranica1] = rang

        return rezultat