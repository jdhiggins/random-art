import random
from math import *

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def inverse(x):
    return (1 - (1 / (1 + x)))


def avg(x, y):
    """The average of x, y"""
    return (x+y)/2


def extreme(x):
    """Returns 1 for positive values and -1 for negative."""
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def minimal(x):
    """Returns .1 for positive values above .25 and -.1 for negative values
    below -.25.  This can mute the effect of some other functions but still
    can make cool stuff.  I am currently not using it."""
    if x > .25:
        return .1
    elif x < -.25:
        return -.1
    else:
        return x


def power(x, y):
    """Returns absolute value of x to the absolute value of y power."""
    return pow(abs(x), abs(y))


def invert(x):
    """Returns the inverse of x"""
    return -x


def greater(x, y):
    """Returns the greater of x and y."""
    if x > y:
        return x
    else:
        return y


def neg(x):
    """Returns a negative value at all times of x."""
    return -(abs(x))



class ExpressionGenerator:
    """This object class randomly generates a string expression from starter
    input and a series of randomly generated input functions."""
    def __init__(self):
        self.starter_input = ["(x)", "(y)", "(x/2)", "(y/2)", "(x*x)", \
                              "(y*y)", "(x*y)", "(sin(x))", "(cos(y))", \
                              "(pi)", "(-1 * pi )"]
        self.one_input_functions = ["sin(", "cos(", "sin(pi*", "cos(pi*", \
                                    "extreme(", "invert(", "neg("]
        self.two_input_functions = ["avg(", "power(", "greater("]


    def generate(self):
        """This function generates the random large function from the function
        lists.  Creates a self.expression that is a string of the functions
        for use in eval."""
        gen_string = random.choice(self.starter_input)
        length = random.randint(15, 25)
        while length > 0:
            number_of_args = random.choice([1, 1, 1, 2, 2])
            if number_of_args == 1:
                random_function = random.choice(self.one_input_functions)
                gen_string = random_function + gen_string + ")"
                length -= 1
            if number_of_args == 2:
                random_function = random.choice(self.two_input_functions)
                gen_string = random_function + \
                             random.choice(self.starter_input) + ", " \
                             + gen_string + ")"
                length -= 1
        self.expression = gen_string


    def evaluate(self, x, y):
        """Evaluate uses the self.expression string and the x and y passed in
        by create_art.py.  Use this in run_expression(expr, x, y) on the
        object created by create_expression using generate()"""
        return eval(self.expression)


    def __str__(self):
        """The string representation of the expression generated is useful
        for recreating your favorite art."""
        return self.expression



def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    gen = ExpressionGenerator()
    gen.generate()
    return gen


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
