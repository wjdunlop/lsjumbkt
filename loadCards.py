from card import Card, Event
def loadEventFromFile(file):
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
    
    for line in finalLines:
        print(line)
    
    

            

if __name__ == '__main__':
    loadEventFromFile('pittsburgh.txt')
    

