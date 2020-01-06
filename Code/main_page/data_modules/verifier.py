
import re


class Verifier:
    def __init__(self, user_input):
        self.user_input = user_input

    def check_id(self):
        """Checks, whether user input consists only of digits; result - 'True' | 'False'"""
        if self.user_input.isdigit():
            return True
        else:
            return False

    def check_password(self):
        """Checks if password consists only of digits or letters."""
        regex = re.fullmatch('[a-zA-Z0-9]*', self.user_input)
        if regex is not None:
            return True
        else:
            return False

    def check_refresh_time(self, input_time):
        """Checks 'Refresh_Time label' - it must consist only of digits or digits with a 'dot'."""
        if input_time == "0":
            return False
        else:
            valid_values = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
            for letter in input_time:
                if letter not in valid_values:
                    return False
                else:
                    continue
            return True

