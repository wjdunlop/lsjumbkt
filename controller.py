import random
import loadCards

# QUARTERS = ['frosh_aut', 'frosh_win', 'frosh_spr']
QUARTERS = ['demo_aut']
BASE_RANDOM_CHANCE = 0.2
RANDOM_MODIFIER = 0.1

def run_quarter(character, quarter):
    # here is where we fetch events/metadata for the quarter
    # quarter_info = load_quarter(quarter)
    # quarter_info = None

    # # parse out quarter info
    # sequential_events = quarter_info.story_events
    # random_events = quarter_info.random_events
    # modifiers = quarter_info.modifiers

    # the below can be multipliers if we end up going that way
    # quarter_char = {}
    # quarter_char.range = modifiers.range + character.range
    # quarter_char.endurance = modifiers.endurance + character.endurance
    # quarter_char.luck = modifiers.luck + character.luck
    # quarter_char.monky = modifiers.monky + character.monky

    # random_prob = BASE_RANDOM_CHANCE
    #
    

    eventStack, random_events = loadCards.structureEventFromFile('pittsburgh.txt')
    

    while len(eventStack) > 0:

        current = eventStack.pop()
        # current could be an event or a card, and could be sequenced or random

        if current is 'r':
            # do a random event
            event = random.choice(list(random_events.keys()))
            
            eventStack.append(random_events[event])
            # random_prob = BASE_RANDOM_CHANCE

        else:
            # do next sequential event
            if current.isCard:
                current.display()
                # GUI.push()
            else:
                for i in current.decompose():
                    eventStack.append(i)

            # random_prob += RANDOM_MODIFIER

        # do stuff with event here
        
            

def play_event(character):
    for quarter in QUARTERS:
        run_quarter(character, quarter)


if __name__ == '__main__':
    play_event(None)