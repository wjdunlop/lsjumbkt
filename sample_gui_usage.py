import gui

# gui = gui.GUI(message_display_length=25, stat_display_length=27)  # init
# The values given to message_display_length and stat_display_length (25 & 27)
# are the same as their default values, these refer to some display formatting
# parameters that are best not changed, especially stat_display_length

gui = gui.GUI()  # simpler init

info_dict_1 = {
    'card_title': 'Frosh Rehearsal',
    'event_title': 'Group Sit',
    'event_message': 'What is your favorite flavor of paint?',
    'band': 5,
    'happiness': 5,
    'academics': 0,
    'special_stat': (False, 0),
    'options': ['red', 'blue', 'the shiney ones', 'the sparkly pink ones']
}

info_dict_2 = {
    'card_title': 'Frosh Rehearsal',
    'event_title': 'Choose sexion',
    'event_message': 'Which sexion would you like to join?',
    'band': 5,
    'happiness': 10,
    'academics': 0,
    'special_stat': (True, 10),
    'options': ['Trumps', 'Bonz', 'Mellz', 'ABF', 'Tenorz', 'Altoz', 'CPG']
}

favorite_color_index = gui.push(info_dict_1)

if favorite_color_index < 2:
    info_dict_2['happiness'] = info_dict_1['happiness'] - 2
else:
    info_dict_2['happiness'] = info_dict_1['happiness'] + 3

sexion_chosen = gui.push(info_dict_2)
