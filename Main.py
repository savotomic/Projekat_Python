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
        print("3 - Unos upita")
        print("")
        print("NAPOMENA:")
        print("Ako zelite da unesete neki upit potrebno je da prvo izaberete opciju 1 ili 2.")
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
            print("")
            print("NAPOMENA:")
            print("Ako zelite da unesete obican unos, unesite na sl nacin: rec rec rec ...")
            print("Ako zelite da uneste logicki unos, unesite na sl nacin: rec operand rec (operand=[and,or,not,AND,OR,NOT])")
            print("")
            unos = str(input("Unesite unos koji zelite da pretrazite: "))
            obicanUpit(recnik, unos)
            if len(unos) == 0:
                print("GRESKA!")
                print("Morate uneti neki unos!")

