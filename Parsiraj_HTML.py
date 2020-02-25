from Parser import  *
from Trie import TrieNode, add, find_word
import os

def parsiraj(graf):
    rootdir = 'F:\\aca\oisisi_git_python\Projekat_Python\\test'
    recnik1 = {}             # recnik u koji kao kljuc ide putanja a kao vrednost ide trie svih reci
    if(os.path.exists(rootdir)):
        parser = Parser()
        root = TrieNode(rootdir)
        for putanja_dir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".html"):
                    putanja = os.path.abspath(putanja_dir + os.sep + file).lower()
                    reci = parser.parse(putanja)[1]
                    linkovi = parser.parse(putanja)[0]
                    cvor = graf.insert_vertex(putanja)
                    for rec in reci:
                        add(root, rec.lower(), cvor)
                    recnik1[putanja] = root
                    for link in linkovi:
                        cvor1 = graf.insert_vertex(link)
                        graf.insert_edge(cvor, cvor1, link)
    else:
        print("Uneti link nije validan.")
        return None
    return recnik1

def parsiraj_unetu(rootdir,graf):
    recnik1 = {}             # recnik u koji kao kljuc ide putanja a kao vrednost ide trie svih reci
    if(os.path.exists(rootdir)):
        parser = Parser()
        root = TrieNode(rootdir)
        for putanja_dir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".html"):
                    putanja = os.path.abspath(putanja_dir + os.sep + file).lower()
                    reci = parser.parse(putanja)[1]
                    linkovi = parser.parse(putanja)[0]
                    cvor = graf.insert_vertex(putanja)
                    for rec in reci:
                        add(root, rec.lower(), cvor)
                    recnik1[putanja] = root
                    for link in linkovi:
                        cvor1 = graf.insert_vertex(link)
                        graf.insert_edge(cvor, cvor1, link)
    else:
        print("Uneti link nije validan.")
        return None
    return recnik1

def nas_recnik(upit, recnik1):
    novi_recnik = {}
    broj_pojavljivanja = 0
    for key, value in recnik1.items():
        if int(find_word(value,upit)[1]) != 0:
            root, broj_pojavljivanja, novi_recnik = find_word(value,upit)
    print("Broj pojavljivanja reci " +str(upit)+ " : " +str(broj_pojavljivanja))
    print("Novi recnik: " +str(novi_recnik))
    #for item in novi_recnik.items():
        #print (item)
    if(broj_pojavljivanja == 0):
        print("Uneta rec ne postoji na unetoj lokaciji.")
    return novi_recnik, broj_pojavljivanja