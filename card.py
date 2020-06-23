import random

class Card:
    
    def __init__(self, _id, eventName, p, contents, choice_1, choice_2, effect_1, effect_2):
        self._ID = _id
        self.p = p
        self.effect_1 = effect_1
        self.effect_2 = effect_2

        # GUI-visible attributes
        self.eventName = eventName
        self.contents = contents
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        
       

    def display(self):
        print("=============")
        print(self._ID)
        print(self.eventName)
        for line in self.contents:
            print(line)
        print("---")
        print(self.choice_1+ '  or  '+ self.choice_2)
        # print("flow #debug")
        # print(self.effect_1,' <==> ',self.effect_2)
        print("=============")

class Event:
    
    def __init__(self, name, cont):
        self.name = name
        self.contents = {}
        self.size = cont
    
if __name__ == '__main__':
    # c = Card(0,"eventName ====", ["line 1", "line 2", "line 3"], "Choice 1", "Choice 2")
    # c.display()
    pass
