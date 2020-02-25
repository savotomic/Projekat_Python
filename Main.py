from locale import atoi
from time import time
from Parsiraj_HTML import *
from Pretraga import *
from Graf import Graph
from Pomocni import *
from django.core.paginator import Paginator

def paginacija(searchedFiles, N):
    stranice = Paginator(searchedFiles, N)
    trenutnastr = stranice.page(1)
    while True:
        br = 1
        print("-------------------------")
        for htmlStr in trenutnastr.object_list:
            print(br, ". ", htmlStr.link, " rang: ", htmlStr.rang)
            br+=1
        print ("-------------------------")
        prethodna = False
        if trenutnastr.has_previous():
            prethodna = True
            print("Prethodna ", end=" ")
        pocetna = 1
        krajnja = stranice.num_pages
        if stranice.num_pages > 11:
            end = 11
            if trenutnastr.number > 6 :
                pocetna = trenutnastr.number - 5
                krajnja = trenutnastr.number + 5
                if krajnja > stranice.num_pages:
                    pocetak = pocetna - (krajnja - stranice.num_pages)
                    end = stranice.num_pages
        for strana in range(pocetna, krajnja+1):
            if strana == trenutnastr.number:
                CYELLOW = '\033[93m'
                CEND = '\033[0m'
                print(CYELLOW + str(strana) + CEND , end=" ")
            else:
                print(strana, end=" ")
        n = False
        if trenutnastr.has_next():
            n = True
            print("Sledeca")
        print('')
        print("Pritisnite N za promenu broja prikaza rezultata po stranici")

        print("Pritisnite 0 za izlaz iz programa")


        opcija = input("Izaberi opciju: ")

        if opcija == "0":
            break
        if prethodna == True:
            if opcija == "Prev":
                trenutnastr = stranice.page(trenutnastr.previous_page_number())
        for i in range(1, stranice.num_pages+1):
            if opcija == str(i):
                trenutnastr = stranice.page(i)
                break
        if n == True:
            if opcija == "Next":
                trenutnastr = stranice.page(trenutnastr.next_page_number())

        if opcija == "N" or opcija == "n":
            broj = input("Unesite novi broj za prikaz rezultata po stranici: ")
            if broj.isdigit():
                broj = atoi(broj)
                if broj > 0:
                    stranice = Paginator(searchedFiles, broj)
                    trenutnastr = stranice.page(1)


if __name__ == '__main__':
    running = True
    userInput = None
    pom=0
    graf = Graph(True)
    while running:
        print("")
        print("*********************")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiraj HTML fajl")
        print("2 - Parsiraj uneti HTML fajl")
        print("3 - Unos i pretraga upita")
        print("4 - Ispis rezultata pretrage")
        print("5 - Prikaz rezultata po stranici")
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
            pom=1
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
                    rezultatRangiranja = obicanUpit(recnik, unos, graf)
                    zaSortiranje = []
                    br = 1
                    if  (rezultatRangiranja != None):
                        for key, value in rezultatRangiranja.rezultat.items():
                            item = Pomocni(key, value)
                            zaSortiranje.append(item)
                    # bubble_sort(listaZaSort)
                    quick_sort(zaSortiranje, 0, len(zaSortiranje) - 1)
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

        if userInput == "4":
            if pom == 0:
                print("GRESKA!")
                print("Morate uneti neki upit!")
                continue

            print('-----REZULTAT-----')
            print('--------')
            for i in range(len(zaSortiranje)):
                print(i + 1,") ",zaSortiranje[i].link)
                print("rang: ",zaSortiranje[i].rang)
                print('----------')

        if userInput == "5":
            if pom == 0:
                print("GRESKA!")
                print("Morate uneti neki upit!")
                continue
            N = input("Unesite broj za prikaz rezultata po stranici: ")
            if N.isdigit():
                N = atoi(N)
                if N > 0:
                    paginacija(zaSortiranje, N)
