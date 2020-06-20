import random

class Card:
    
    def __init__(self, _id, eventName, contents, leftChoice, rightChoice, leftID, rightID):
        self._ID = _id
        self.eventName = eventName
        self.contents = contents
        self.leftChoice = leftChoice
        self.rightChoice = rightChoice
        self.leftID = leftID
        self.rightID = rightID

    def display(self):
        print("=============")
        print(self._ID)
        print(self.eventName)
        for line in self.contents:
            print(line)
        
        print(self.leftChoice+ '  or  '+ self.rightChoice)
        print(self.leftID,' <==> ',self.rightID)
        print("=============")

class Event:
    
    def __init__(self, name):
        self.name = name
        self.cards = {}
    
if __name__ == '__main__':
    # c = Card(0,"eventName ====", ["line 1", "line 2", "line 3"], "Choice 1", "Choice 2")
    # c.display()
    pass