__author__ = 'Flatline01'
__version__ = '1.0.0'
import RPi.GPIO as GPIO
import time


def seven_segment_display(number: str,
                          anode: bool=True,
                          reset: bool=False,
                          power_mode: bool=False,
                          pin_scheme: dict=None):
    """
        Decode decimal number and pass to 7-segment LED display
        7-segment-scheme == PIN number GPIO (Raspberry Pi 3 B+)
        a == 12 (36)
        b == 11 (32)
        c == 7  (29)
        d == 5  (31)
        e == 3  (13)
        f == 8  (26)
        g == 10  (18)

        P. S. You can change PIN for your scheme in dictionary below
    """
    if type(number) == int:
        number = str(number)
    else:
        number = number.lower()

    if pin_scheme is None:
        DISPLAY_PIN_SCHEME = {
            'a': 36, 'b': 32, 'c': 29, 'd': 31, 'e': 13, 'f': 26, 'g': 18
            }
    else:
        DISPLAY_PIN_SCHEME = pin_scheme

    DEC_HEX = {
        '0': 0x7E, '1': 0x30, '2': 0x6D, '3': 0x79, '4': 0x33,
        '5': 0x5B, '6': 0x5F, '7': 0x70, '8': 0x7F, '9': 0x7B,
        'a': 0x77, 'b': 0x1F, 'c': 0x4E, 'd': 0x3D,
        'e': 0x4F, 'f': 0x47, 'test': 0x6C
        }
    display_state = [0, 0, 0, 0, 0, 0, 0]

    def decimal_hex_state(number: str) -> list:
        """
            Convert decimal input in hex code for display, and then hex-code
            to binary like a list of seven 0 and 1
        """
        # Decoding from hex to binary, and deleted '0b' in the begining
        display_command: list = list(bin(DEC_HEX[number]))
        display_command.pop(0)
        display_command.pop(0)

        # TODO deleted this test
        print(display_command)

        # Change type of '0' and '1' from str --> int in list
        # .reverse in the begining and in the end - for 0,
        #  if number is les then 7 binary digits
        display_command.reverse()
        for index in range(len(display_command)-1, -1, -1):
            display_state[index] = int(display_command[index])
        display_state.reverse()

        # TODO deleted this test
        print(display_state)

        # NOTE Change by default 0 to 1, and otherwise
        if anode:
            for i in range(0, len(display_state)):
                if display_state[i] == 0:
                    display_state[i] = 1
                else:
                    display_state[i] = 0

        # TODO deleted this test
        print(display_state)

        return display_state

    def displaying_number(display_state: list) -> None:
        """
            Send state to the pin in GPIO of Raspberry Pi 3
            and display the number
            BUG For now it's off for testing
        """
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # If in the future will be new interface with
        #  additional pin - for example for 'dot'
        keys_pin_list = list(DISPLAY_PIN_SCHEME.keys())
        keys_pin_list.sort()

        # Activation of PIN with value by key in dictionary
        for key_pin in keys_pin_list:
            GPIO.setup(DISPLAY_PIN_SCHEME[key_pin], GPIO.OUT, initial=0)

        # Cicle for displaying the number
        state_index = 0
        for key_pin in keys_pin_list:
            GPIO.output(
                DISPLAY_PIN_SCHEME[key_pin],
                display_state[state_index]
                )
            state_index += 1

    def start_sequence():
        sequence = [
            [0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, ]
            ]

        for x in range(0, len(sequence)):
            displaying_number(sequence[x])
            time.sleep(0.5)

    # Check, if you want to reset your pin's, or start 'power_mode'
    if reset:
        GPIO.cleanup()
    elif power_mode:
        start_sequence()
    else:
        displaying_number(decimal_hex_state(number))


if __name__ == '__main__':
    # Test sequence
    seven_segment_display(0, power_mode=True)

    display_count = 0
    while display_count < 1:
        for y in range(0, 10):
            seven_segment_display(y)
            time.sleep(1)
        seven_segment_display('a')
        time.sleep(1)
        seven_segment_display('b')
        time.sleep(1)
        seven_segment_display('c')
        time.sleep(1)
        seven_segment_display('d')
        time.sleep(1)
        seven_segment_display('e')
        time.sleep(1)
        seven_segment_display('f')
        time.sleep(1)
        seven_segment_display('test')
        time.sleep(1)
        display_count += 1
    print('End')
    seven_segment_display(0, power_mode=True)
    time.sleep(3)
    seven_segment_display(4, reset=True)
