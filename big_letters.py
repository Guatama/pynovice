__author__ = 'Flatline01'

def print_big_letter(letter):
    patterns = {1:'  *  ', 2:' * * ', 3:'*   *', 4:'*    ', 5:'**** ', 6:'*****', 7:'***  ', 8:'**   '}
    alphabet = { 'A':[1, 2, 6, 3, 3], 'B':[5, 3, 5, 3, 5]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big_letter('B')
print()
print_big_letter('A')
