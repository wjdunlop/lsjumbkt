class GUI:
    def __init__(self):
        self.card_title = ''
        self.event_title = ''
        self.event_message = ''
        self.band = ''
        self.happiness = 0
        self.academics = 0
        self.special_stat_on = False
        self.special_stat_val = 0
        self.options = []

    def push(self, info_dict):
        """
        Takes in the necessary info to display a card,
        and returns the user inputted choice
        """
        # Update GUI info
        self.card_title = info_dict['card_title']
        self.event_title = info_dict['event_title']
        self.event_message = info_dict['event_message']
        self.band = info_dict['band']
        self.happiness = info_dict['happiness']
        self.academics = info_dict['academics']
        self.special_stat_on = info_dict['special_stat_on']
        self.special_stat_val = info_dict['special_stat_val']
        self.options = info_dict['options']

        return self._update()

    def _update(self):
        print('{:^50}'.format(self.card_title))
        event_title = '>> ' + self.event_title + ' <<'
        print('{:^50}'.format(event_title))
        print()

        print('{:^50}'.format('|'))

        choice = 0
        return choice

    def _format_message(self):
        result = ['']
        if len(self.event_message) > 45:
            words = self.event_message.split()
            curr = 0
            while len(words) > 0:
                if (len(result[curr]) + len(words[0])) > 45:
                    curr += 1
                    result.append('')
                result[curr] = result[curr] + words[0] + ' '
                words.pop(0)
        else:
            result[0] = self.event_message

        return result
