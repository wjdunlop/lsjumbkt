from card import Card, Event
def loadCards(file):
    lines = open(file).readlines()
    readLines = []

    for l in lines:
        line = l.strip()
        # print(line)
        if line:
            if line[0] != '#':
                readLines.append(line.strip())
            else:
                pass
                # print(line)
    
    finalLines = []
    for line in readLines:
        if line != '':
            # print(line)
            finalLines.append(line)
    
    c = 0
    _id = 0
    title = ''
    contents = []
    leftChoice = ''
    rightChoice = ''
    leftID = 0
    rightID = 0

    name = finalLines[0]
    cont = int(finalLines[1][9:].strip())
    finalLines = finalLines[11:]
    thisEvent = Event(name, cont)
    for item in finalLines[2:-1]:
        
        if item == '[':
            c = 0
            pass

        elif item == ']':
            thisEvent.cards[_id] = Card(_id, title, contents, leftChoice, rightChoice, leftID, rightID)
            c = 0
            _id = 0
            title = ''
            contents = []
            leftChoice = ''
            rightChoice = ''
            leftID = 0
            rightID = 0

        else:
            # print("C >> ", c)
            # print(item)
            if c is 0:
                _id = int(item[3:].strip())
            if c is 1:
                title = item[7:].strip()
            if c is 2:
                if item.startswith('%'):
                    contents.append(item[1:])
                else:
                    c += 1
            if c is 3:
                leftChoice = item[9:].strip()
            if c is 4:
                leftID = int(item[10:].strip())
            if c is 5:
                rightChoice = item[9:].strip()
            if c is 6:
                rightID = int(item[10:].strip())
            if c is not 2:
                c += 1 
    
    print(thisEvent.name)
    print("# of cards  ", thisEvent.size)
    for card in thisEvent.cards:
        
        thisEvent.cards[card].display()
            

if __name__ == '__main__':
    loadCards('example.txt')

