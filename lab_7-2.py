"""
Create a Python file named lab_7-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a function called greeting()
Add a docstring to the function that explains how the function can only print "Hello World" on one line
Add a statement in the function to print "Hello World!"
Add a statement that returns the docstring for the greeting function
Add another statement to call the function
"""

#Author: Nicholas Yepes 11/16/23

#deffines greeting 
def greeting():
    
    #prints out hello world!
    print("Hello World!") 
    # returns the docstring
    return greeting.__doc__
    
#prints out the returend docstring
print(greeting())