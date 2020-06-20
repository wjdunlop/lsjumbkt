import sys
from os import system, name

print('#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#')
print('# Killa Trumpz text-based adventure #')
print('#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#')

_BASESP = 10


def clearScreen():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def chooseCharacter():
    sp = _BASESP
    print("=========CHARACTER CUSTOMIZATION=========")
    
    while sp > 0:
        
        print("Customize your character! you have >>"+str(sp)+"<< skill points remaining...")

        sp -= 1


    

    clearScreen()
    
    return 8

chooseCharacter()
print('cat')
