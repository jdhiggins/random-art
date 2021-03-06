Welcome to Random Art!!

To run the program, open your terminal and run python3 create-art.py.

If you'd like to run more than one gen at once, add -n and the number you'd like to make.  For example: python3 create-art.py -n 5 will make 5 random drawings at once.

The module at random_art.py is responsible for creating an object that holds a random formula created from a preexisting parts list.  This creation happens
when create_art.py runs create_expression().  The run_expression() function will
evaluate the string held at the object's self.expression, using x and y.  This creates a slower generation of art as the eval function works its way through the very long random formulas.  But it makes cool art!

My favorite 3 are:

Seed-2372483741499200068
color-2372483741499200068-3.png:


Seed: 646786650211422027
color-646786650211422027-0.png:

Seed: 3343935891560701134
color-3343935891560701134-3.png:

See the full formulas at favorites.txt


# Random Art

## Description

Create art using Python's random module and math functions.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Randomness
* The Python `random` module
* The sublime beauty of generated art

### Performance Objectives

After completing this assignment, you should be able to:

* Generate images with Python
* Use randomness to construct new functions

## Details

### Deliverables

* A Git repo called random-art containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a `random_art` module
  * Your favorite piece of art you made, plus instructions
    on how to replicate it.

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

You are going to make random art, inspired by
[random-art.org](http://www.random-art.org/). This project comes
with a file `create_art.py`. This file expects a module called
`random_art` with two functions:

* `create_expression()`: this function takes no arguments and returns
  an expression that will generate a number between -1.0 and 1.0, given
  `x` and `y` coordinates.

* `run_expression(expression, x, y)`: this function takes an expression
  created by `create_expression` and an `x` and `y` value. It runs the
  expression, passing the `x` and `y` values to it and returns a value
  between -1.0 and 1.0.

### What's an expression?

I'm super-glad you asked! It is a way for you to create a formula for your
random art. You can define it however you like. Perhaps it's just a function
and `run_expression` just runs it. Maybe it's an [abstract syntax tree][] and
`run_expression` walks the tree and evaluates it. Maybe it's Python code in
a string that you call `eval` on. You have to figure this part out, and it's
one of the harder parts of this exercise.

### What should my expression do?

The concrete thing it has to do is take an `x` and `y` value and return a new
value between -1.0 and 1.0. That doesn't tell you why or how, though.

You should randomly construct an expression that uses `sin`, `cos`, and any
other functions you want. `sin` and `cos` will definitely help you create
patterns, but you should be creative. Look at other functions available to you
and create your own functions for use.

How you randomly construct the expression is up to you. `random.random()` and
`random.choice()` are both obvious ways to construct it, but you should look
at all the different functions for random distributions and consider them.

![random1](random1.png)

This image was created with the following expression:

```py
sin(pi * sin(pi * sin(pi * (sin(pi * sin(pi * sin(pi * sin(pi *
    cos(pi * y))))) * cos(pi * sin(pi * cos(pi *
    avg(sin(pi * y), (x * x)))))))))
```

[abstract syntax tree]: https://en.wikipedia.org/wiki/Abstract_syntax_tree


## Notes

`create_art.py` takes several command-line parameters you may want to use.

* `--seed SEED` sets the random seed to a particular number. This is great for
being able to generate the same image more than once.

* `-n NUM` or `--number NUM` sets how many images to create. `NUM` is 1 by
default.

* `--gray` or `--color` sets whether the image is in grayscale or color.
Color is default.

## Additional Resources

* [Random Art](http://www.random-art.org/)
* [The `random` module](https://docs.python.org/3.4/library/random.html)
* [The `math` module](https://docs.python.org/3.4/library/math.html)

## Credit

Modified from [a "nifty assignment" from the annual SIGCSE meeting](http://nifty.stanford.edu/2009/stone-random-art/).
This is the readme
