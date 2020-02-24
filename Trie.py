class TrieNode(object):

    def __init__(self, char = str):
        self.char = char
        self.children = []                #lista reci
        self.kraj_reci = False       #gledamo da li je poslednji
        self.counter = 0
        self.recnik = {}             #ovde smestamo reci koje pretrazimo

def add(root, word = str, html_word = str):
    node = root
    word_len = len(word)
    for char in word:
        word_len -= 1
        found_in_child = False
        for child in node.children:      #trazimo karakter u cvoru
            if child.char == char:
                node = child             #vezi cvor i karakter
                found_in_child = True
                break
        if not found_in_child:           #ako ne nadjemo karakter, trebamo ga napraviti
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node              #vezi cvor i karakter
    node.kraj_reci = True                #kraj reci
    if(html_word in node.recnik.keys()):
        node.recnik[html_word] += 1
    else:
        node.recnik[html_word] = 1
    node.counter += 1
    return node.counter

def find_word(root, word = str):
    node = root
    if not root.children:               #ako cvor nema karakter, tj ako je prazan
        return False, 0
    for char in word:
        char_not_found = True
        for child in node.children:     #pretrazi karaktere trenutnog cvora
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
                return False, 0
        if node.kraj_reci == False:
            node.counter = 0
    return node.kraj_reci, node.counter, node.recnik    #ako pronadjemo rec, vrati True i broj pronalazenja date reci

if __name__ == "__main__":
    root = TrieNode('o')
    add(root, "prefiks")
    add(root, 'pre')

    print(find_word(root, 'pre'))
    print(find_word(root, 'pree'))
    print(find_word(root, 'prefiks'))
    print(find_word(root, 'pr'))
    print(find_word(root, 'prep'))
    print(find_word(root, '.'))
