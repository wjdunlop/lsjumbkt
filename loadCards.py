from card import Card, Event
def loadToDicts(file):
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
    
    # for line in finalLines:
    #     print(line)
    
    #Construct event with name from firstLine of decommented file
    rawSequence = {}
    rawFiller = {}
    buffer = []
    curr = 0

    _id = None
    eventName = None
    p = None
    contents = []
    choice_1 = None
    choice_2 = None
    effect_1 = None
    effect_2 = None
    storyline = finalLines[0]
    finalLines = finalLines[1:]
    for i in finalLines:
        
        
        
        if i.startswith('id: '):
            # print(i)
            key = i[3:].strip()
            if key.startswith('r'):
                curr = key
            else:
                curr = int(key)
        
        if i.startswith('title: '):
            eventName = i[6:].strip()
        if i.startswith('p: '):
            p = i[2:].strip()
        if i.startswith('%'):
            contents.append(i[1:].strip())
        if i.startswith('choice_1: '):
            choice_1 = i[9:].strip()
        if i.startswith('effect_1: '):
            effect_1 = i[9:].strip()
        if i.startswith('choice_2: '):
            choice_2 = i[9:].strip()
        if i.startswith('effect_2: '):
            effect_2 = i[9:].strip()
        if i.startswith('$'):
            
        
            if key.startswith('r'):
                rawFiller[curr] = Card(curr, eventName, p, contents, choice_1, choice_2, effect_1, effect_2)
                
            else:
                rawSequence[curr] = Card(curr, eventName, p, contents, choice_1, choice_2, effect_1, effect_2)
            _id = None
            eventName = None
            p = None
            contents = []
            choice_1 = None
            choice_2 = None
            effect_1 = None
            effect_2 = None

    return storyline, rawSequence, rawFiller
import sys
def structureEventFromFile(file):
    storyline, rawSeq, rawFill = loadToDicts(file)
    
    print(storyline)
    eventID = 0
    while len(storyline) > 0:
        cont = []
        if storyline.startswith('e'):
            eventID = storyline[1]
            storyline = storyline[3:]
        else:
            if storyline.find(',') < storyline.find(')'):
                k = storyline.find(',')
                cont.append(int(storyline[0:k]))
            elif storyline.find(')') < storyline.find(','):
                k = storyline.find(')')
                print(storyline) 
            sys.exit()

    for i in storylineSeq:
        rawSeq[i].display()
        while True:
            if input('') == '1':
                print(rawSeq[i].effect_1)
                break
            elif input('') == '2':
                print(rawSeq[i].effect_2)
                break
        
            


if __name__ == '__main__':
    structureEventFromFile('pittsburgh_tabular.txt')
    

