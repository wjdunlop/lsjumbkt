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
            print(line)
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
    finalLines = finalLines[1:]
    thisEvent = Event(name)
    for item in finalLines[1:-1]:
        
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
            print("C >> ", c)
            print(item)
            if c is 0:
                _id = int(item)
            if c is 1:
                title = item
            if c is 2:
                if item.startswith('%'):
                    contents.append(item[1:])
                else:
                    c += 1
            if c is 3:
                leftChoice = item[1:]
            if c is 4:
                leftID = int(item[1:])
            if c is 5:
                rightChoice = item[1:]
            if c is 6:
                rightID = int(item[1:])
            if c is not 2:
                c += 1 
    
    for card in thisEvent.cards:

        thisEvent.cards[card].display()
            

if __name__ == '__main__':
    loadCards('example.txt')
