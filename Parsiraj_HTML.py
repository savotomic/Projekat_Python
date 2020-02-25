from Parser import  *
from Trie import TrieNode, add, find_word
import os

def parsiraj():
    rootdir = 'C:\\Users\PC\\Desktop\\FAKS\\OISISI PYTHON\\Projekat_Python\\test'
    recnik1 = {}             # recnik u koji kao kljuc ide putanja a kao vrednost ide trie svih reci
    if(os.path.exists(rootdir)):
        parser = Parser()
        root = TrieNode(rootdir)
        for putanja_dir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".html"):
                    putanja = os.path.abspath(putanja_dir + os.sep + file).lower()
                    reci = parser.parse(putanja)[1]
                    for rec in reci:
                        add(root, rec.lower(),putanja)
                    recnik1[putanja] = root
    else:
        print("Uneti link nije validan.")
        return None
    return recnik1

def parsiraj_unetu(rootdir):
    recnik1 = {}             # recnik u koji kao kljuc ide putanja a kao vrednost ide trie svih reci
    if(os.path.exists(rootdir)):
        parser = Parser()
        root = TrieNode(rootdir)
        for putanja_dir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".html"):
                    putanja = os.path.abspath(putanja_dir + os.sep + file).lower()
                    reci = parser.parse(putanja)[1]
                    for rec in reci:
                        add(root, rec.lower(),putanja)
                    recnik1[putanja] = root
    else:
        print("Uneti link nije validan.")
        return None
    return recnik1