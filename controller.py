import random

QUARTERS = ['frosh_aut', 'frosh_win', 'frosh_spr']
BASE_RANDOM_CHANCE = 0.2
RANDOM_MODIFIER = 0.1

def run_quarter(character, quarter):
    # here is where we fetch events/metadata for the quarter
    # quarter_info = load_quarter(quarter)
    quarter_info = None

    # parse out quarter info
    sequential_events = quarter_info.story_events
    random_events = quarter_info.random_events
    modifiers = quarter_info.modifiers

    # the below can be multipliers if we end up going that way
    quarter_char = {}
    quarter_char.range = modifiers.range + character.range
    quarter_char.endurance = modifiers.endurance + character.endurance
    quarter_char.luck = modifiers.luck + character.luck
    quarter_char.monky = modifiers.monky + character.monky

    random_prob = BASE_RANDOM_CHANCE
    while sequential_events:
        event = None
        if random.random() < random_prob:
            # do a random event
            event = random.choice(random_events)
            random_events.remove(event)
            random_prob = BASE_RANDOM_CHANCE
        else:
            # do a sequential event
            event = sequential_events[0]
            sequential_events.pop(0)
            random_prob += RANDOM_MODIFIER

        # do stuff with event here

def play_game(character):
    for quarter in QUARTERS:
        run_quarter(character, quarter)