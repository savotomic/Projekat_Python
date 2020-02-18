class TrieNode(object):

    def __init__(self, char = str):
        self.char = char
        self.children = []                #lista reci
        self.word_finished = False        #gledamo da li je poslednji
        self.counter = 1

def add(root, word = str):

    node = root
    for char in word:
        found_in_child = False
        for child in node.children:      #trazimo karakter u cvoru
            if child.char == char:       #ako nadjemo povecaj brojac
                child.counter += 1
                node = child             #vezi cvor i karakter
                found_in_child = True
                break
        if not found_in_child:           #ako ne nadjemo karakter, trebamo ga napraviti
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node              #vezi cvor i karakter
    node.word_finished = True            #kraj reci


def pretraga(root, prefix = str):

    node = root
    if not root.children:               #ako cvor neka karakter, tj ako je prazan
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:     #pretrazi karaktere trenutnog cvora
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0

    return True, node.counter


if __name__ == "__main__":
    root = TrieNode('o')
    add(root, "prefiks")
    add(root, '.')

    print(pretraga(root, 'pre'))
    print(pretraga(root, 'pree'))
    print(pretraga(root, 'prefiks'))
    print(pretraga(root, 'pr'))
    print(pretraga(root, 'prep'))
    print(pretraga(root, '.'))



