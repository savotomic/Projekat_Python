from Graf import *
from Parsiraj_HTML import nas_recnik
from Set import *

logickeOperacije = ["AND", "OR", "NOT","and","or","not"]                 #trebace mi za proveru da li se log operacije nalaze kod reci

def obicanUpit(rootdir, upit, graf):          # u obican upit mozemo uneti obicne reci razdvojene razmakom
    reci = upit.split(" ")         # i onda parsira svaku rec posebno
    for i in range(len(reci)):
        if (reci[i] in logickeOperacije):
            logickiupit(rootdir, upit)
            return
    s = Set()
    for i in range(len(reci)):
        print("Pronalazenje reci " + str(reci[i]) + ":")
        recnik2, broj2 = nas_recnik(reci[i], rootdir)
        rangiranaPretraga=rangiranje(recnik2,graf)          #vraca recnik rangiranih stranica za datu rec
        # if (len(reci) == 1):
        #     return rangiranaPretraga
        if (len(reci) == 1):
            s.rezultat = rangiranaPretraga
            return s
        reci[i] = rangiranaPretraga
    for i in range(len(reci) - 1):
        s.unija(reci[i], reci[i + 1])
    return s


def logickiupit(rootdir,upit):                         #ovde se mogu podrzati i logicki operatori, da moze da parsira zajedno sa njima
    reci = upit.split(' ')
    if (len(reci) != 3):                      # duzina formata mora biti duzine 3, npr. java AND python
        print("Greska, nije dobar format! Obican upit: rec rec ... Logicki upit: rec operand rec [operand = AND,and,OR,or,NOT,not]")
        return None
    if (reci[0] in logickeOperacije) or (reci[2] in logickeOperacije) or (reci[1] not in logickeOperacije):
        print("Greska, nije dobar format! Obican upit: rec rec ... Logicki upit: rec operand rec [operand = AND,and,OR,or,NOT,not]")
        return None
    if (reci[1] == 'AND' or reci[1] == 'and'):
        s1 = Set()
        and0, vr_and0 = nas_recnik(reci[0], rootdir)
        and2, vr_and2 = nas_recnik(reci[2], rootdir)
        if vr_and0 == 0 and vr_and2 == 0:
            return None
        rang0and = rang(and0, graf)
        rang2and = rang(and2, graf)
        s1.presek(rang0and, rang2and)
        return s1

    if (reci[1] == 'OR' or reci[1] == 'or'):
        s2 = Set()
        or0, vr_or0 = nas_recnik(reci[0], rootdir)
        or2, vr_or2 = nas_recnik(reci[2], rootdir)
        if or0 == 0 and vr_or2 == 0:
            return None
        rang0or = rang(or0, graf)
        rang2or = rang(or2, graf)
        s2.unija(rang0or, rang2or)
        return s2

    if (reci[1] == 'NOT' or reci[1] == 'not'):
        s3 = Set()
        not0, vr_not0 = nas_recnik(reci[0], rootdir)
        not2, vr_not2 = nas_recnik(reci[2], rootdir)
        if vr_not0 == 0 and vr_not2 == 0:
            return None
        rang0not = rang(not0, graf)
        rang2not = rang(not2, graf)
        s3.komplement(rang0not, rang2not)
        return s3

        # print ("Upit je uspesno pretrazen!")
    return reci  # ako provera prodje format je dobar


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