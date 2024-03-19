"""
This script contains a list of helper functions
"""

import turtle


def get_braille_file_name(file_name: str):
    """
    Append the suffix "-braille" at the end of the file name and before the extension
    """
    dot_index = file_name.rfind(".")
    return file_name[0:dot_index] + "-braille" + file_name[dot_index:]


def print_braille(lst):
    """
    Prints the Braille letters in passed list to the screen in a nice format.
    The passed list is a list of lists.  Each sublist must have 6 items with
    values of 1 or 0 representing a Braille character.
    """
    assert type(lst) is list
    for item in lst:
        assert type(item) is list
        assert len(item) == 6

    line1 = ""
    line2 = ""
    line3 = ""
    for item in lst:
        line1 = line1 + str(item[0]) + " "
        line2 = line2 + str(item[1]) + " "
        line3 = line3 + str(item[2]) + " "
        line1 = line1 + str(item[3]) + " "
        line2 = line2 + str(item[4]) + " "
        line3 = line3 + str(item[5]) + " "

    print(line1)
    print(line2)
    print(line3)


def draw_word(trt, lst):
    """
    Uses the passed turtle, draw the Braille characters in passed list
    """
    for item in lst:
        draw_braille_character(trt, item)


def draw_braille_character(trt, bc):
    """
    Uses the passed turtle, draw the passed Braille character
    """
    # TODO: edit this function then remove this line
    radius = 5
    trt.setheading(0)
    trt.penup()
    trt.forward(radius)
    trt.setheading(270)
    trt.pendown()
    for i in range(len(bc)):
        trt.circle(radius)
        trt.up()
        if i % 3 == 2:
            trt.backward(6 * radius)
            trt.left(90)
            trt.forward(3 * radius)
            trt.right(90)
        else:
            trt.forward(3 * radius)
        trt.down()


def write_braille(lst, file_name):
    # TODO: implement the function then remove this line
    pass


if __name__ == '__main__':
    braille_test = [[1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0]]

    print_braille(braille_test)

    screen = turtle.Screen()
    trl = turtle.Turtle()
    draw_word(trl, braille_test)
    screen.mainloop()
