import random

class Card:
    eventName = ''
    contents = []
    leftChoice = None
    rightChoice = None
    #always 2 for now

    def __init__(self, _id, eventName, contents, leftChoice, rightChoice):
        self._ID = _id
        self.eventName = eventName
        self.contents = contents
        self.leftChoice = leftChoice
        self.rightChoice = rightChoice

    def display(self):
        print("=============")
        print(self._ID)
        print(self.eventName)
        for line in self.contents:
            print(line)
        
        print(self.leftChoice+ '  or  '+ self.rightChoice)
        print("=============")

class Deck:
    cards = []


c = Card(0,"eventName ====", ["line 1", "line 2", "line 3"], "Choice 1", "Choice 2")
c.display()