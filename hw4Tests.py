# ====================================================================
#
#  Homework 4 tests
#
# ====================================================================


from hw4Code import *
import turtle
import os.path
import time


# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    test_braille_dictionary()
    test_translator()
    test_draw_braille_character()
    test_write_braille()
    test_translate_document()
    print()
    print("DONE WITH ALL TESTS.")

# ========================================================================
# Test for Question 1 - Braille (Part 1)


def test_braille_dictionary():
    """Tests the braille_dictionary contents."""

    print()
    print("-------------------------------------")
    print("Testing braille_dictionary contents:")
    print("key\tvalue")
    braille_dictionary = create_braille_dictionary()
    for key in braille_dictionary:
        print(key, "\t", braille_dictionary[key])


# ========================================================================
# Test for Question 2 - Braille (Part 2)

def test_translator():
    """Tests the translator function. Note that details about specific test calls are
    printed if the function FAILS the test."""
    
    print()
    print("-------------------------------------")
    print("Testing translator():")

    braille_dictionary = create_braille_dictionary()

    s1 = "the quick brown fox jumps over the lazy dog"
    assert translator(s1, braille_dictionary) == [[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0]]

    s2 = "do it as you will"
    assert translator(s2, braille_dictionary) == [[1, 0, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 1, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 1, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 1, 1]]

    s3 = "from every corner of the planet, people go and seek more knowledge"
    assert translator(s3, braille_dictionary) == [[1, 1, 0, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 0, 0]]

    s4 = "It's possible we can do more with just very little."
    assert translator(s4, braille_dictionary) == [[0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 0, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]]

    s5 = "I have quite the conundrum that may come back to bite us."
    assert translator(s5, braille_dictionary) == [[0, 1, 0, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 0, 1]]

    s6 = "We have to do this so that racoons don't come back again."
    assert translator(s6, braille_dictionary) == [[0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0]]

    s7 = "But rather then start over, why not be more like her and never give up?"
    assert translator(s7, braille_dictionary) == [[1, 1, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 1, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]]

    s8 = "How much is too much?"
    assert translator(s8, braille_dictionary) == [[1, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                  [1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0]]


# ========================================================================
# Test for Question 3 - Braille (Part 3)


def getTurtle():
    """This is a helper function for testing with the turtle module. It takes no inputs,
    and it returns existing turtle if there is one, otherwise makes
    a new turtle object and returns it."""
    existingTurts = turtle.turtles()
    if existingTurts == []:
        return turtle.Turtle()
    else:
        return existingTurts[0]


def test_draw_braille_character():
    """Testing program for the draw_braille_character function, must be visually checked"""
    braille_dictionary = create_braille_dictionary()

    print()
    print("--------------------------------------")
    print("Testing draw_braille_character():         CHECK VISUALLY")

    screen = turtle.Screen()
    sp = getTurtle()
    sp.speed(0)
    sp.ht()

    print("First test, braille of 'Hello, world!'")
    bs = translator("Hello, world!", braille_dictionary)
    sp.up()
    sp.goto(-200, 0)
    sp.down()
    draw_word(sp, bs)
    time.sleep(5.0)
    screen.reset()

    sp.speed(0)
    print("Second test, braille of 'people can do'")
    bs = translator("people can do", braille_dictionary)
    sp.up()
    sp.goto(-200, 0)
    sp.down()
    draw_word(sp, bs)
    screen.exitonclick()



# ========================================================================
# Test for Question 4 - write_braille()
def test_write_braille():
    """ Tests the write_braille function. Note that the details about specific
    test calls are printed if the function FAILS the test."""

    print()
    print("-------------------------------------")
    print("Testing write_braille():")

    #"the quick brown fox jumps over the lazy dog"
    b1 = [[0, 1, 1, 1, 1, 0],
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
    write_braille(b1, "test_read_words_1.txt")
    assert os.path.exists("test_read_words_1.txt")
    test_file = open("test_read_words_1.txt", 'r')
    doc = test_file.read()
    assert len(doc) == 519
    assert doc.count("\n") == 3
    assert doc.find("\n") == 172
    assert (doc[0], doc[201], doc[500]) == ('0', '0', '1')

    #"do it as you will"
    b2 = [[1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 1, 1]]
    write_braille(b2, "test_read_words_2.txt")
    assert os.path.exists("test_read_words_2.txt")
    test_file = open("test_read_words_2.txt", 'r')
    doc = test_file.read()
    assert len(doc) == 111
    assert doc.count("\n") == 3
    assert doc.find("\n") == 36
    assert (doc[0], doc[50], doc[100]) == ('1', ' ', '1')


def test_translate_document():
    """ Tests the translate_document function. Note that the details about specific
    test calls are printed if the function FAILS the test."""

    print()
    print("-------------------------------------")
    print("Testing translate_document():")

    braille_dictionary = create_braille_dictionary()
    translate_document(braille_dictionary, "sample.txt")

    assert os.path.exists("braille-sample.txt")
    test_file = open("braille-sample.txt", 'r')
    doc = test_file.read()
    assert len(doc) == 1923
    assert doc.count("\n") == 3
    assert doc.find("\n") == 640
    assert (doc[0], doc[100], doc[1001]) == ('1', '1', '0')

if __name__ == "__main__":
    runTests()
