def is_command_in_phrase(phrase, command_list):
    for key in command_list:
        if key.lower() in phrase.lower():
            return True, command_list[key]

    return False, ''


class CommandController:

    def __init__(self, command_list):
        self.command_list = command_list

    def play_if_command_exists(self, phrase):
        x, seq = is_command_in_phrase(phrase, self.command_list)
        if x:
            for command in seq:
                command.play_command()

