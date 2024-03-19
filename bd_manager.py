"""
 This script manages the braille dictionary

 @author: Susan Fox
 @author: Amin G. Alhashim (aalhashi@macalester.edu)
"""


def add_numbers(bd):
    """
    Add the Braille representation for the digits 1-9 to the passed dictionary
    """
    assert type(bd) is dict

    bd['1'] = [1, 0, 0, 0, 0, 0]
    bd['2'] = [1, 1, 0, 0, 0, 0]
    bd['3'] = [1, 0, 0, 1, 0, 0]
    bd['4'] = [1, 0, 0, 1, 1, 0]
    bd['5'] = [1, 0, 0, 0, 1, 0]
    bd['6'] = [1, 1, 0, 1, 0, 0]
    bd['7'] = [1, 1, 0, 1, 1, 0]
    bd['8'] = [1, 1, 0, 0, 1, 0]
    bd['9'] = [0, 1, 0, 1, 0, 0]
    bd['0'] = [0, 1, 0, 1, 1, 0]


def add_letters(bd):
    """
    Add the Braille representation for the letters a-z to the passed dictionary
    """
    assert type(bd) is dict

    bd['a'] = [1, 0, 0, 0, 0, 0]
    bd['b'] = [1, 1, 0, 0, 0, 0]
    bd['c'] = [1, 0, 0, 1, 0, 0]
    bd['d'] = [1, 0, 0, 1, 1, 0]
    bd['e'] = [1, 0, 0, 0, 1, 0]
    bd['f'] = [1, 1, 0, 1, 0, 0]
    bd['g'] = [1, 1, 0, 1, 1, 0]
    bd['h'] = [1, 1, 0, 0, 1, 0]
    bd['i'] = [0, 1, 0, 1, 0, 0]
    bd['j'] = [0, 1, 0, 1, 1, 0]

    bd['k'] = [1, 0, 1, 0, 0, 0]
    bd['l'] = [1, 1, 1, 0, 0, 0]
    bd['m'] = [1, 0, 1, 1, 0, 0]
    bd['n'] = [1, 0, 1, 1, 1, 0]
    bd['o'] = [1, 0, 1, 0, 1, 0]
    bd['p'] = [1, 1, 1, 1, 0, 0]
    bd['q'] = [1, 1, 1, 1, 1, 0]
    bd['r'] = [1, 1, 1, 0, 1, 0]
    bd['s'] = [0, 1, 1, 1, 0, 0]
    bd['t'] = [0, 1, 1, 1, 1, 0]

    bd['u'] = [1, 0, 1, 0, 0, 1]
    bd['v'] = [1, 1, 1, 0, 0, 1]
    bd['x'] = [1, 0, 1, 1, 0, 1]
    bd['y'] = [1, 0, 1, 1, 1, 1]
    bd['z'] = [1, 0, 1, 0, 1, 1]

    bd['w'] = [0, 1, 0, 1, 1, 1]


def add_braille2_words(bd):
    """
    Add Braille 2 words to the passed dictionary
    """
    assert type(bd) is dict

#     TODO: add your code below then remove this line


def get_braille_dictionary():
    """
    Creates and returns the Braille 2 dictionary
    """
    bd = {}
    bd[" "] = [0, 0, 0, 0, 0, 0]    # Braille representation for space
    add_numbers(bd)
    add_letters(bd)
    add_braille2_words(bd)

    return bd


if __name__ == '__main__':
    print(get_braille_dictionary())

