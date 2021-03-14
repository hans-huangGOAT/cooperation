
#  CS196 SP21 Debugging Homework
Your task for this week's homework is to debug this bank's software. Use what you've learned in the past few lectures to find and fix all the bugs in this codebase. You may also run into bits of unfinished code. It is your job to finish writing those pieces of code too!

# IMPORTANT NOTE
If you want to run this code on your computer, you will need to install a few python packages. To do so, navigate to this directory in a command line interface (Terminal on MacOS, Powershell on Windows, etc...). Then, run the following command: `pip install -r requirements.txt`.

If the command above does not work, you may need to install the python package manager pip. You can [install pip here](https://pip.pypa.io/en/stable/installing/) if you need to do so. 

# Hints
You will come across some new pieces of Python code that you may not have seen before. Here are a few hints to help you along. Remember, Prof. Google is always your best friend!

## Docstrings
Docstrings are multi-line strings as follows: 
   
     '''Notice the triple single quotes.'''
     
     '''
     This is also valid.
     '''
     
     """
     This is also valid. 
     """

They are used in Python as descriptions for what functions do, the parameters they take, and more. Read the docstrings! They are there to help you.

## Type Hints
Type hints come in 2 forms. Consider this piece of code:

    def test(x: int) -> bool:
	    return x == 1
The first type of type hint is within the parameter declaration. The function signature is telling you that x should be an int. The second type of type hint in this example is the return type hint. The arrow pointing at bool tells you that this function will return a bool.

Type hints can be any data type. An object that you created, a list, a tuple, a dict, an int...the list goes on. Use them to your advantage!

## Decorators
Decorators are used to provide additional functionality to certain functions. Some decorators you will see are `@property` and `@<insert_variable_name>.setter`.

The property decorator allows you to call the function without parentheses. If you have the following function in the class `Test` and the variable `t = Test()`:

    @property
    def example(self):
	    return self._example

...you can call `t.example` to access the variable `_example` from the object `t`. The `@property` decorator acts as a getter. This leads to 'private' variables.

The `@<insert_variable_name>.setter` decorator works in a similar fasion.

## "Private" Variables
Variables can't really be private in Python, BUT there is a convention where you can indicate that certain variables are meant to be treated as private. You may have notices this convention above. We add an underscore in front of a variable if we want it to be private. Ex: `self._example`. We can couple "private" variables in Python with the decorators above for a method of abstraction you may have learned about in Java in CS125.

NOTE: 'private' variables in Python ARE NOT actually private. This is merely a convention to let others know to treat such variables as private. 

## Enums
Enums are essentially labels. That's really all you need to know. As always, you can look up more detailed explanations online.
