""" ======================================================================
Homework 4 - Collection Data Types & File I/O
File: hw4Code.py
Author: put your name here
"""

# -----------------
import turtle
import string


# ==============================================================
# Question 1

def add_numbers(bd):
    """ Add the digits 1-9 to the Braille dictionary bd"""
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
    """ Add the letters a-z to the Braille dictionary bd"""
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


# ---- Add function to upgrade braille_dictionary from a grade 1 dictionary to a grade 2 ----



def create_braille_dictionary():
    """Creates and returns the Braille dictionary for Question 1"""
    braille_dictionary = {}
    braille_dictionary[" "] = [0, 0, 0, 0, 0, 0]
    add_numbers(braille_dictionary)
    add_letters(braille_dictionary)
    # Add your function call here

    return braille_dictionary


# ==============================================================
# Question 2

def print_braille(lst):
    """prints the Braille letters in lst to the screen
    in a nice format.
    lst is a list of lists.  Each sublist should have 6 items
    with volues of 1 or 0 representing a Braille character."""
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

# ----------- Add your translator function here -----------------




# ==============================================================
# Question 3

def draw_word(trt, lst):
    """Uses a turtle, turt, to draw the Braille characters in lst"""
    for item in lst:
        draw_braille_character(trt, item)

# ------------------ Modify this function for question 3 ---------------------------
def draw_braille_character(trt, bc):
    """Uses a turtle, trt, to draw the Braille character bc"""
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
            trt.backward(6*radius)
            trt.left(90)
            trt.forward(3*radius)
            trt.right(90)
        else:
            trt.forward(3*radius)
        trt.down()

# ==============================================================
# Question 4




#---------------------------------
# Put testing calls here

if __name__ == '__main__':
    print("My tests:")

    # Creating the Braille dictionary for Question 1
    braille_dictionary = create_braille_dictionary()

    ## Test calls to Question 2
    # word_list1 = translator("Hi!", braille_dictionary)
    # print(word_list1)
    # print_braille(word_list1)
    # word_list2 = translator("Hello world!", braille_dictionary)
    # print(word_list2)
    # print_braille(word_list2)
    # word_list3 = translator("knowledge", braille_dictionary)
    # print(word_list3)
    # print_braille(word_list3)

    ## Test calls to Question 3
    # win = turtle.Screen()
    # trt = turtle.Turtle()
    # trt.speed(0)
    # trt.ht()
    # draw_braille_character(trt, braille_dictionary["a"])
    # draw_braille_character(trt, braille_dictionary["z"])
    # draw_braille_character(trt, braille_dictionary["knowledge"])
    # win.exitonclick()

    ## Test calls to Question 4
    # translate_document(braille_dictionary, "alice.txt")

    True  # Make Python happy if everything is commented out