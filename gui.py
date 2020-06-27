import queue

MESSAGE_DISPLAY_LENGTH = 25
STATS_DISPLAY_LENGTH = 27


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
        # Prints out the headers
        print(self.card_title)
        event_title = '>> ' + self.event_title + ' <<'
        print(event_title)
        print()

        message_queue = self._format_message()
        stats_list = self._generate_stats_list()
        empty_line = '{s:<{message_length}}{mid:^1}' \
                     '{s:>{stat_length}}'.format(s=' ', mid='|',
                                                 message_length=MESSAGE_DISPLAY_LENGTH,
                                                 stat_length=STATS_DISPLAY_LENGTH)
        print(empty_line)

        for stat in stats_list:
            if not message_queue.empty():
                message = message_queue.get()
            else:
                message = ' ' * MESSAGE_DISPLAY_LENGTH
            print('{message:<{message_length}}{mid:^1}'
                  '{stat:>{stat_length}}'.format(message=message,
                                                 mid='|',
                                                 stat=stat,
                                                 message_length=MESSAGE_DISPLAY_LENGTH,
                                                 stat_length=STATS_DISPLAY_LENGTH))
        while not message_queue.empty():
            print('{message:<{message_length}}{mid:^1}'.format(message=message_queue.get(),
                                                               mid='|',
                                                               message_length=MESSAGE_DISPLAY_LENGTH))
        print(empty_line)
        print()

        choice = 0
        return choice

    def _format_message(self):
        """
        Turns the message into a list of sub-sentences,
        so we can print it onto multiples with restricted
        length for each line
        """
        result = queue.Queue()
        if len(self.event_message) > MESSAGE_DISPLAY_LENGTH:
            words = self.event_message.split()
            curr = ''
            for word in words:
                if (len(curr) + len(word)) < MESSAGE_DISPLAY_LENGTH:
                    curr += word + ' '
                else:
                    result.put(curr)
                    curr = ''

            # Catches edge cases
            if curr:
                result.put(curr)
        else:
            result.put(self.event_message)

        return result

    def _generate_stats_list(self):
        result = [self._format_stat('band', self.band),
                  self._format_stat('happiness', self.happiness),
                  self._format_stat('academics', self.academics)]

        if self.special_stat_on:
            result.append('-' * 25)
            result.append(self._format_stat('special stat', self.special_stat_val))

        return result

    @staticmethod
    def _format_stat(name, val):
        """
        Given a stat name and value out of ten, display a stat bar
        """
        # The following definition for bar is the same as: '=' * val + ' ' * (10 - val)
        bar = '{s:=<{bar_width}}{s: <{fill_width}}'.format(s='', bar_width=val, fill_width=10 - val)
        return '{name:<13}[{bar}]'.format(name=name, bar=bar)


def debug():
    gui = GUI()
    gui.event_message = 'what is yor favorite flavor of paint'
    """q = gui._format_message()
    while not q.empty():
        print(q.get())"""

    gui.band = 10
    gui.happiness = 10
    gui.academics = 1
    gui.special_stat_on = False
    gui.special_stat_val = 10

    gui.card_title = 'Frosh Rehearsal'
    gui.event_title = 'group sit'

    gui._update()


if __name__ == '__main__':
    debug()