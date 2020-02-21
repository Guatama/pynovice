DEC_HEX = {
    '0': 0x7E, '1': 0x30, '2': 0x6D, '3': 0x79, '4': 0x33,
    '5': 0x5B, '6': 0x5F, '7': 0x70, '8': 0x7F, '9': 0x7B,
    'a': 0x77, 'b': 0x1F, 'c': 0x4E, 'd': 0x3D,
    'e': 0x4F, 'f': 0x47,
    'test': 0x6C, 'power': [0x40, 0x20, 0x10, 0x8, 0x4, 0x2]}


def hex_to_bin(hex_number: hex, anode: bool=True) -> list:
    """
        Convert decimal inputy in hex code for display, and then hex-code
        to binary like a list of seven 0 and 1
    """
    display_state: list = [0, 0, 0, 0, 0, 0, 0]

    # Decoding from hex to binary, and deleted '0b' in the begining
    display_command: list = list(bin(hex_number))
    display_command.pop(0)
    display_command.pop(0)

    # TODO deleted this test
    print('First step', display_command)

    display_command.reverse()
    # Change type of '0' and '1' from str --> int in list
    for index in range(len(display_command)-1, -1, -1):
        display_state[index] = int(display_command[index])
    display_state.reverse()

    # TODO deleted this test
    print('Second step: ', display_state)

    # NOTE Change by default 0 to 1, and otherwise
    if anode:
        for i in range(0, len(display_state)):
            if display_state[i] == 0:
                display_state[i] = 1
            else:
                display_state[i] = 0

    # TODO deleted this test
    print('Third step', display_state)

    return display_state


if __name__ == "__main__":
    # Testing
    print(hex_to_bin(DEC_HEX['power'][3]))
