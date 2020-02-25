from time import time
from Parsiraj_HTML import *
from Pretraga import *
from Graf import Graph

if __name__ == '__main__':
    running = True
    userInput = None
    graf = Graph(True)
    while running:
        print("")
        print("*********************")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiraj HTML fajl")
        print("2 - Parsiraj uneti HTML fajl")
        print("3 - Unos i pretraga upita")
        print("")
        print("NAPOMENA:")
        print("Ako zelite da unesete neki upit, tj zelite opciju 3, potrebno je da prvo izaberete opciju 1 ili 2.")
        userInput = input("Izaberi opciju: ")
        if userInput == "0":
            running = False

        if userInput == "1":
            startTime = time()
            print("Vrsi se ucitavanje...")
            recnik = parsiraj(graf)
            endTime = time()
            vreme = endTime - startTime
            print("Vreme ucitavanja HTML fajla: " + str(vreme) + " sekundi")

        if userInput == "2":
            lokacija = str(input('Unesi putanju za HTML fajl: '))
            startTime = time()
            print("Vrsi se ucitavanje...")
            recnik = parsiraj_unetu(lokacija,graf)
            endTime = time()
            vreme = endTime - startTime
            print("Vreme ucitavanja unetog HTML fajla: " + str(vreme) + " sekundi")

        if userInput == "3":
            running1 = True
            userInput1 = None
            while running1:
                print("")
                print("!!!!!!!MENU!!!!!!")
                print("0 - Vrati se na prethodni meni")
                print("1 - Ako je HTML fajl parsiran pretrazi uneti upit")
                userInput1 = input("Izaberi opciju: ")
                if userInput1 == "0":
                    running1 = False
                if userInput1 == "1":
                    print("")
                    print("NAPOMENA:")
                    print("Ako zelite da unesete obican upit, unesite na sl nacin: rec rec rec ...")
                    print("Ako zelite da uneste logicki upit, unesite na sl nacin: rec operand rec (operand=[and,or,not,AND,OR,NOT])")
                    print("")
                    unos = str(input("Unesite upit koji zelite da pretrazite: "))
                    startTime = time()
                    #obicanUpit(recnik, unos, graf)
                    # rang = obicanUpit(recnik, unos, graf)
                    #
                    # print(rang)
                    # listaZaSort = []                      #proba ranga
                    # br = 1
                    # for key, value in rang.items():
                    #     print("ket ",key)
                    #     print("vr: ",value)
                    endTime = time()
                    vreme = endTime - startTime
                    if len(unos) == 0:
                        print("GRESKA!")
                        print("Morate uneti neki unos!")
                    else:
                        print("Vreme pronalazenja unosa: " + str(vreme) + " sekundi")
                    running1 = False                         #da bi se vratio na pocetni meni
