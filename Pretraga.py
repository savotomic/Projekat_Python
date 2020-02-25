logickeOperacije = ["AND", "OR", "NOT","and","or","not"]                 #trebace mi za proveru da li se log operacije nalaze kod reci

def obicanUpit(rootdir, upit):          # u obican upit mozemo uneti obicne reci razdvojene razmakom
    reci = upit.split(" ")         # i onda parsira svaku rec posebno
    if (len(reci) > 1 and (reci[1] in logickeOperacije) and len(reci) == 3):
        logickiupit(rootdir, upit)
        return

def logickiupit(rootdir,upit):                            #ovde se mogu podrzati i logicki operatori, da moze da parsira zajedno sa njima
    reci = upit.split(' ')
    if (reci[0] in logickeOperacije) or (reci[2] in logickeOperacije):
        print("Greska, nije dobar format! Primer formata python AND java")
        return None                                          #ako provera prodje format je dobar


