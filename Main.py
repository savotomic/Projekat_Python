from time import time
from Parsiraj_HTML import *

if __name__ == '__main__':
    running = True
    userInput = None

    while running:
        print("")
        print("*********************")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiraj HTML fajl")
        print("2 - Parsiraj uneti HTML fajl")
        userInput = input("Izaberi opciju: ")
        if userInput == "0":
            running = False

        if userInput == "1":
            startTime = time()
            print("Vrsi se ucitavanje...")
            recnik = parsiraj()
            endTime = time()
            vreme = endTime - startTime
            print("Vreme ucitavanja HTML fajla: " + str(vreme) + " sekundi")

        if userInput == "2":
            lokacija = str(input('Unesi putanju za HTML fajl: '))
            startTime = time()
            print("Vrsi se ucitavanje...")
            recnik = parsiraj_unetu(lokacija)
            endTime = time()
            vreme = endTime - startTime
            print("Vreme ucitavanja unetog HTML fajla: " + str(vreme) + " sekundi")
