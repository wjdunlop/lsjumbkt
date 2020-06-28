import queue


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

        self.message_display_length = 25
        self.stat_display_length = 27

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
        print()
        print(self.card_title)
        event_title = '>> ' + self.event_title + ' <<'
        print(event_title)
        print()

        message_queue = self._format_message()
        stats_list = self._generate_stats_list()
        empty_line = '{s:<{message_length}}{mid:^1}' \
                     '{s:>{stat_length}}'.format(s=' ', mid='|',
                                                 message_length=self.message_display_length,
                                                 stat_length=self.stat_display_length)
        print(empty_line)

        for stat in stats_list:
            if not message_queue.empty():
                message = message_queue.get()
            else:
                message = ' ' * self.message_display_length
            print('{message:<{message_length}}{mid:^1}'
                  '{stat:>{stat_length}}'.format(message=message,
                                                 mid='|',
                                                 stat=stat,
                                                 message_length=self.message_display_length,
                                                 stat_length=self.stat_display_length))
        while not message_queue.empty():
            print('{message:<{message_length}}{mid:^1}'.format(message=message_queue.get(),
                                                               mid='|',
                                                               message_length=self.message_display_length))
        print(empty_line)
        print()

        for i in range(len(self.options)):
            print('({n}) {option}'.format(n=i + 1, option=self.options[i]))

        print()
        print('-' * (self.message_display_length + self.stat_display_length + 1))

        choice = self._handle_input()

        print()
        print('#' * (self.message_display_length + self.stat_display_length + 1))

        return choice

    def _format_message(self):
        """
        Turns the message into a list of sub-sentences,
        so we can print it onto multiples with restricted
        length for each line
        """
        result = queue.Queue()
        if len(self.event_message) > self.message_display_length:
            words = self.event_message.split()
            curr = ''
            for word in words:
                if (len(curr) + len(word)) < self.message_display_length:
                    curr += word + ' '
                else:
                    result.put(curr)
                    curr = word + ' '

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

    def _handle_input(self):
        choice = input('> ')
        while (not choice.isdigit()) or (int(choice) not in range(1, len(self.options) + 1)):
            print('Invalid input, please enter a number from the choices above.')
            choice = input('> ')
        return int(choice)


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

    gui.options = ['red', 'green', 'aaaaa']

    print(gui._update())


if __name__ == '__main__':
    debug()
