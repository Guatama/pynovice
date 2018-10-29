def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text (challenge from checkio)
    """
    if text.count(symbol) > 1:
        return text.find(symbol, text.find(symbol) + 1)
    else:
        return None

# Cool method with for-loop and if-statements
# def second_index(text: str, symbol: str) -> [int, None]:
#     count = 0
#     for num in range(0,len(text)):
#         if text[num] == symbol:
#             count += 1
#         if count == 2:
#             return num


if __name__ == '__main__':  # Testing
    print('Example:')
    print(second_index("sims", "s")) # return 3
    print(second_index("simcity is really cool game", "m"))  # return 25

