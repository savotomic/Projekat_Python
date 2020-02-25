from Graf import *
from Parsiraj_HTML import nas_recnik

logickeOperacije = ["AND", "OR", "NOT","and","or","not"]                 #trebace mi za proveru da li se log operacije nalaze kod reci

def obicanUpit(rootdir, upit, graf):          # u obican upit mozemo uneti obicne reci razdvojene razmakom
    reci = upit.split(" ")         # i onda parsira svaku rec posebno
    for i in range(len(reci)):
        if (reci[i] in logickeOperacije):
            logickiupit(rootdir, upit)
            return
    for i in range(len(reci)):
        print("Pronalazenje reci " + str(reci[i]) + ":")
        recnik2, broj2 = nas_recnik(reci[i], rootdir)


def logickiupit(rootdir,upit):                         #ovde se mogu podrzati i logicki operatori, da moze da parsira zajedno sa njima
    reci = upit.split(' ')
    if (len(reci) != 3):                      # duzina formata mora biti duzine 3, npr. java AND python
        print("Greska, nije dobar format! Primer formata: python AND java")
        return None
    if (reci[0] in logickeOperacije) or (reci[2] in logickeOperacije) or (reci[1] not in logickeOperacije):
        print("Greska, nije dobar format! Primer formata python AND java")
        return None
    print("Upit je uspesno unet!")


