class Node():
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None :
        return
    print(current.data, end='')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()
