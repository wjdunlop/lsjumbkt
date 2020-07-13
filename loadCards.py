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
    eventComp = finalLines[1]
    finalLines = finalLines[2:]

    for i in finalLines:
        
        if i.startswith('id: '):
            
            # print(i)
            key = i[3:].strip()
            # if key.startswith('r'):
            #     curr = key
            # else:
            curr = key
        
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

    return storyline, eventComp, rawSequence, rawFiller
import sys
def structureEventFromFile(file):
    storyline, eventComp, rawSeq, rawFill = loadToDicts(file)
    originalStoryline = storyline
    cont = []
    
    # print(storyline)
    eventComp = eventComp.strip()
    
    # print(eventComp)
    # sys.exit()
    events = {}
    eventID = 0
    
    top = True
    while len(eventComp) > 0:
        
        if eventComp.startswith('e') and top:
            cont = []
            eventID = eventComp[:2]
            eventComp = eventComp[3:]
            top = False
        else:

            if eventComp.endswith(')') and ',' not in eventComp:
                cont.append(eventComp[:-1])
                eventComp = ''
                # print(len(eventComp))
                # print(eventComp)
                # print("eventID:", eventID)
                # print("CONT: ", cont)
                # print('3')
                rawSeq[eventID] = cont
                # print('1')
                top = True
            elif eventComp.find(',') < eventComp.find(')'):
                k = eventComp.find(',')
                cont.append(eventComp[0:k])
                eventComp = eventComp[k+1:]
                # print(eventComp)
                # print('2')
            elif eventComp.find(')') < eventComp.find(',') or eventComp.endswith(')'):
                k = eventComp.find(')')
                cont.append(eventComp[0:k])
                eventComp = eventComp[k+2:]
        
                # print(len(eventComp))
                # print(eventComp)
                # print("eventID:", eventID)
                # print("CONT: ", cont)
                # print('3')
                top = True
                rawSeq[eventID] = cont
            else:
                print('parsing error')
                sys.exit()
            # print('storyline')
            # print(eventComp)
            # print('ccc>>')
            # print(cont)
            for c in cont:
                # print('checking: ',c)
                if not (c.isdigit() or c[0] == 'e'):
                    print("eventComp format incorrect...")
            
            c = eventID
            if not c[0] == 'e' and c[1:].isdigit():
                print("eventComp format incorrect...")

    # print(events)
           
    eventsAsType = {}
    # print(rawSeq)
    # sys.exit()
    eventStack = []
    structured = {}
    for i in rawSeq.keys():
        if i.startswith('e'):
            # print(i)
            
            thisCont = []
            toEventCont = []
            thisCont += rawSeq[i]
            for k in thisCont:
                if k[0] != 'e':
                    
                    toEventCont.append(rawSeq[k])
                else:
                    toEventCont.append(k)
            eventsAsType[i] = Event(i, toEventCont)
            eventsAsType[i].contents.reverse()
            # print(eventsAsType[i].contents)

    for key in eventsAsType.keys():
        conts = eventsAsType[key].contents
        for i in range(len(eventsAsType[key].contents)):
            if isinstance(conts[i], str):
                conts[i] = eventsAsType[conts[i]]
                
        
        eventsAsType[key].contents = conts
        print('e', eventsAsType[key])

    

    for i in storyline.split(','):
        if i.startswith('r'):
            eventStack.append('r')
        else:
            eventStack.append(eventsAsType[i])
    
    eventStack.reverse()
    # print('----')
    # print(originalStoryline)
    # eventStack.pop().contents[1].display()
    return eventStack, rawFill
if __name__ == '__main__':
    print("DEBUG START")
    stack, rands = structureEventFromFile('pittsburgh copy.txt')
    print(rands)
    print(stack)
    # while len(stack) > 0:
    #     print(stack)
    #     this = stack.pop()
    #     if this.isCard:
    #         this.display()
    #     elif not this.isCard:
    #         stack += this.decompose()
    
    print("DEBUG END")
    

