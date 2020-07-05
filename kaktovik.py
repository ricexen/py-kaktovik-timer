import numpy

numerals = {
        '0': '\uE5B3',
        "1": '\uE5A0',
        "2": '\uE5A1',
        "3": '\uE5A2',
        "4": '\uE5A3',
        "5": '\uE5A4',
        "6": '\uE5A5',
        "7": '\uE5A6',
        "8": '\uE5A7',
        "9": '\uE5A8',
        "A": '\uE5A9',
        "B": '\uE5AA',
        "C": '\uE5AB',
        "D": '\uE5AC',
        "E": '\uE5AD',
        "F": '\uE5AE',
        "G": '\uE5AF',
        "H": '\uE5B0',
        "I": '\uE5B1',
        "J": '\uE5B2',
}

def convertDec(n):
    kaktovik_number = ''
    for char in numpy.base_repr(n, base=20):
        kaktovik_number += numerals[char]
    return kaktovik_number


