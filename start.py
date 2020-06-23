import sys
import os
from loadCards import structureEventFromFile

print('#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#')
print('# Killa Trumpz text-based adventure #')
print('#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#')

_BASESP = 10

def clearScreen():

    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

# returns dictionary with {attribute:skillpts}
def chooseCharacter():
    sp = _BASESP
    print("=========CHARACTER CUSTOMIZATION=========")
    rangeSP = 0
    enduranceSP = 0
    luckSP = 0
    monkySP = 0


    while sp > 0:
        
        
        selected = input("Customize your character! you have >>" +
                         str(sp)+"<< skill points remaining...\n\n"+
                         "(R)ANGE  " +str(rangeSP)+ "\n(E)NDURANCE   "+str(enduranceSP)+"\n(L)UCK   " +str(luckSP)+ "\n(M)ONKY   "+str(monkySP)+"\n>> ")
        
        if selected.lower() == 'r':
            print("cccc")
            rangeSP += 1
        elif selected.lower() == 'e':
            enduranceSP += 1
        elif selected.lower() == 'l':
            luckSP += 1
        elif selected.lower() == 'm':
            monkySP += 1
        
        if selected.lower() in ['r', 'e', 'l', 'm']:
            sp -= 1
        
        clearScreen()
        


    

    

    return {'range': rangeSP, 'endurance':enduranceSP, 'luck':luckSP, "monky":monkySP}

#TEST CODE
event = structureEventFromFile('example.txt')


