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
        rangiranaPretraga=rangiranje(recnik2,graf)          #vraca recnik rangiranih stranica za datu rec
        # if (len(reci) == 1):
        #     return rangiranaPretraga
        reci[i]= rangiranaPretraga


def logickiupit(rootdir,upit):                         #ovde se mogu podrzati i logicki operatori, da moze da parsira zajedno sa njima
    reci = upit.split(' ')
    if (len(reci) != 3):                      # duzina formata mora biti duzine 3, npr. java AND python
        print("Greska, nije dobar format! Obican upit: rec rec ... Logicki upit: rec operand rec [operand = AND,and,OR,or,NOT,not]")
        return None
    if (reci[0] in logickeOperacije) or (reci[2] in logickeOperacije) or (reci[1] not in logickeOperacije):
        print("Greska, nije dobar format! Obican upit: rec rec ... Logicki upit: rec operand rec [operand = AND,and,OR,or,NOT,not]")
        return None
    print("Upit je uspesno unet!")


def rangiranje(podaci,graf):
    rangovi = {}
    for key in podaci.keys():
        rang = podaci[key] * 3
        linkovi = graf.incident_edges(key, False)
        rang += len(linkovi) * 0.3
        for edge in linkovi:
            prekoputa = edge.opposite(key)
            if prekoputa in podaci.keys():
                rang += podaci[prekoputa] * 0.5
        rangovi[key.element()] = rang
    return rangovi