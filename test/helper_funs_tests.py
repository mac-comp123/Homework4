"""
This script contains unit tests for the functions in the helper_funs module

To activate pytest on Pycharm follow these steps:
> go to Pycharm Settings
> Expand Tools
> Click Python Integrated Tools
> Under Testing section: Default test runner, select pytest
> Click Fix to install the module if prompted

@author: Susan Fox
@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""
import time
import turtle
import os
from src.helper_funs import draw_word
from src.helper_funs import write_braille


def getTurtle():
    """
    This is a helper function for testing with the turtle module. It takes no inputs,
    and it returns existing turtle if there is one, otherwise makes
    a new turtle object and returns it.
    """
    existingTurts = turtle.turtles()
    if not existingTurts:
        return turtle.Turtle()
    else:
        return existingTurts[0]


def test_draw_word_all_0():
    screen = turtle.Screen()
    sp = getTurtle()
    sp.speed(0)
    sp.ht()

    bs = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    sp.up()
    sp.goto(-200, 0)
    sp.down()
    draw_word(sp, bs)
    time.sleep(5)
    screen.clear()
    time.sleep(2)


def test_draw_word_all_1():
    screen = turtle.Screen()
    sp = getTurtle()
    sp.speed(0)
    sp.ht()

    bs = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

    sp.up()
    sp.goto(-200, 0)
    sp.down()
    draw_word(sp, bs)
    time.sleep(5)
    screen.clear()
    time.sleep(2)


def test_write_braille_fox():
    bw = [[0, 1, 1, 1, 1, 0],
          [1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 0, 1, 0, 0, 1],
          [0, 1, 0, 1, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 1, 1],
          [1, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 0, 0],
          [1, 0, 1, 0, 1, 0],
          [1, 0, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 1, 0],
          [1, 0, 1, 0, 0, 1],
          [1, 0, 1, 1, 0, 0],
          [1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 0],
          [1, 1, 1, 0, 0, 1],
          [1, 0, 0, 0, 1, 0],
          [1, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0],
          [1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 1],
          [1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [1, 1, 0, 1, 1, 0]]

    file_name = "test_write_braille_fox.txt"
    write_braille(bw, file_name)
    assert os.path.exists(file_name)
    test_file = open(file_name, 'r')
    doc = test_file.read()
    assert len(doc) == 519
    assert doc.count("\n") == 3
    assert doc.find("\n") == 172
    assert (doc[0], doc[201], doc[500]) == ('0', '0', '1')


def test_write_braille_do():
    bw = [[1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 1, 1]]

    file_name = "test_write_braille_do.txt"
    write_braille(bw, file_name)
    assert os.path.exists(file_name)
    test_file = open(file_name, 'r')
    doc = test_file.read()
    assert len(doc) == 111
    assert doc.count("\n") == 3
    assert doc.find("\n") == 36
    assert (doc[0], doc[50], doc[100]) == ('1', ' ', '1')
