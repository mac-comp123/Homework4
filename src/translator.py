"""
The script contain function to help translating English sentences to Braille representation
"""

from src.bd_manager import get_braille_dictionary
from src.helper_funs import print_braille


def translate(sentence, bd):
    """
    TODO: Write a docstring for the function then remove this line
    """
    assert type(sentence) is str
    assert type(bd) is dict

    # TODO: Write your implementation for the function below then remove this line


def translate_document(bd, file_name):
    # TODO: implement the function then remove this line
    pass


if __name__ == '__main__':
    bd = get_braille_dictionary()
    braille_rep = translate("Hi!", bd)
    print(braille_rep)
    print_braille(braille_rep)
