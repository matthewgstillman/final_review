#- You need to know how to write all programs in the labs and homework. - You need the different ways to import a module Import random Import random as rand From random import *
#File read/open/close
#1. Write the following words in a file called "hello_world.txt" Hello World!! I just finished my final.
hello_world = open("hello_world.txt", "w")
with open("hello_world.txt") as fh:
    lines = fh.readlines()
    print("Hello World!! I just finished my final.")

#2. Generate 50 random numbers from 1 to 100 and write them to a file called random numbers. Now separate them into 2 files: even.txt and odd.txt. The program should also output the total of these numbers in each file
import random
random_numbers = open("random_numbers.txt", "w")
random_numbers = open("random_numbers.txt", "r")
file_even = open("even.txt", "w")
file_even = open("even.txt", "r")
file_odd = open("odd.txt", "w")
file_odd = open("odd.txt", "r")
odd_count = 0
even_count = 0
with open("random_numbers.txt") as fh:
    for i in range(1,51):
        random_digit = random.randint(1,101)
        if random_digit % 2 == 0:
            even_append = open("even.txt", "a")
            even_append.write(random_digit)
            even_count += 1
        else:
            odd_append = open("odd.txt", "a")
            odd_append.write(random_digit)
            odd_count += 1

    print("There are {} even numbers and {} odd numbers".format(even_count, odd_count))


#3. You have a list of random baby names. What does the list look like? Now use the choice function to randomly select one of the names and write it to a file called random_name.txt
import random
baby_names = ["Sophia","Olivia","Emma","Ava","Isabella","Aria","Riley","Amelia"]
random_baby_name = random.choice(baby_names)
print("Random Baby Name: {}".format(random_baby_name))
baby_name_text = open("random_name.txt", "w")
baby_name_text = open("random_name.txt", "r")
with open("random_name.txt") as fh:
    lines = fh.readlines()
    name_append = open("random_name.txt", "a")
    name_append.write(random_baby_name)



#4. Write a program that asks the user for the name of the file. The program will display 5 lines only. If the file contains less than five lines, it should display the whole file.
file_name = "article.txt"

file_name = input("What is the name of the file?")
fileh = open(file_name, "r")
with open(file_name) as fh:
    lines = fh.readlines()
    num_lines = sum(1 for line in open(file_name))
    if num_lines <= 5:
        print("The number of lines: {}".format(num_lines))
        print(lines)
    else:
        for i in range(1,6):
            print(lines[i])

#Exceptions:
#1. try/except/else/finally clause
# bill_total = input("What is your total bill")
# tip = bill_total * 0.15
# print ("Your tip should be", tip)
#Does this code work? If not, use try/except/else to improve the code 
#No, the above code doesn't work. You need to make tip equal to int(bill_total) * 0.15

bill_total = input("What is your total bill? ")
if type(bill_total) != 'int':
    try:
        bill_total = int(bill_total)
        tip = bill_total * 0.15
        print ("Your tip should be", tip)
    except:
        print("Bill total must can't be multiplied by a float if it's a string!")

#Map/filter/reduce/lambda
#- Use map to map every single number to the absolute version
number_list = [1,-2,3,4,-5]
absolute_number = map(lambda x: abs(x), number_list)
print("Absolute Number: {}".format(absolute_number))

#- Use map to map every number to the integer version. If the number is 3.5, it should round up to 4
to_integer_list = [1.0, 2.5, 3.2, 2.0]
integers = map(lambda x: int(round(x)), to_integer_list)
print("To Integer List: {}".format(integers))


#- Use map to map every string to the length of the string, followed by uppercase version in a
#Not Quite Right
string_list = ["these", "are", "a", "bunch", "of"]
string_lengths = map(lambda x: x.upper() + " " + str(len(x)), string_list)
print("String Lengths: {}".format(string_lengths))


#tuple. For example, happy becomes (5,HAPPY)
#- Use map to map every letter in a string to the ord value. Return this as a string with commas
tuple_string = "Shitstring"
ord_tuple = map(lambda x: ord(x), tuple_string.upper())
print("Order Tuple: {}".format(ord_tuple))


#- Use filter to filter out only those words with more than 5 characters
strings_list = ["big", "words", "often", "get", "filtered"]
filtered_strings = filter(lambda x: len(x) > 5, strings_list)
print("Filtered Strings: {}".format(filtered_strings))

#- Use filter to filter out only those words starting with "th"
words = ["happy", "new", "year", "this", "that"]
filter_words = list(filter(lambda x: x[0:2]=="th",words))

print(filter_words)

#- Use filter to filter out only those words with "ing"
newer_string_list = ["these", "words", "keep", "coming", "to", "the", "forefront"]
ing_strings = filter(lambda x: "ing" in x, newer_string_list)
print("Strings ending with 'ing': {}".format(ing_strings))

#- Use filter to filter out only those numbers starting with 78 and divisible 4
numbers=[35245,4625,76,784,78748,38,638,68846]
num_filter=list(filter(lambda x: x%4==0 and str(x)[0:2]=="78", numbers))
print(num_filter)


#- Use reduce (maybe filter too) to find the biggest element not exceeding 4 digits
numbers=[35245,4625,76,784,78748,38,638,68846]
filter_num= list(filter(lambda x: x<10000, numbers))

#- Use filter and/or reduce to find the smallest non-negative number in a list
from functools import reduce
biggest = reduce (lambda x, y: x if x>y else y, filter_num)
print(biggest)

#Classes:
#1. Given a class diagram, write the class.
class Automobile(object):
    def __init__(self, __make, __model, __mileage, __price):
        self.__make = __make
        self.__model = __model
        self.__mileage = __mileage
        self.__price = __price

    def set_make(self, __make):
        self.__make = __make
        return self

    def set_model(self, __model):
        self.__model = __model
        return self

    def set_mileage(self, __mileage):
        self.__mileage = __mileage
        return self

    def set_price(self, __price):
        self.__price = __price
        return self

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

class Car(Automobile):
    def __init__(self, __make, __model, __mileage, __price, __doors):
        super(Automobile, self).__init__()
        self.__doors = __doors

    def set_doors(self, __doors):
        self.__doors = __doors
        return self

    def get_doors(self):
        return self.__doors

class Truck(Automobile):
    def __init__(self, __make, __model, __mileage, __price, __drive_type):
        super(Automobile, self).__init__()
        self.__drive_type = __drive_type


    def set_drive_type(self, __drive_type):
        self.__drive_type = __drive_type
        return self

    def get_drive_type(self):
        return self.__drive_type


class SUV(Automobile):
    def __init__(self, __make, __model, __mileage, __price, __pass_cap):
        super(Automobile, self).__init__()
        self.__pass_cap = __pass_cap

    def set_pass_cap(self, __pass_cap):
        self.__pass_cap = __pass_cap
        return self

    def get_pass_cap(self):
        return self.__pass_cap

suv1 = SUV("Toyota", "Highlander", "82000", "12000", "2")
print("SUV # 1 - Make: {}".format(suv1.get_make()))

#GUI:
#1. What is a widget? text box, text entry, label, button, check box, radio button, canvas 
#Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
#Widget - an application, or a component of an interface, that enables a user to perform a function or access a service.

#Text Box - A multilined box with text

#Text Entry - A Box that lets the user input text

#Label - A bit of text that defines or clarifies the name or functionality of a button, textbox, etc.

#Button - A simple button, used to execute a command or other operation.

#Check Box - widgets that permit the user to make multiple selections from a number of different options. This is different to a radio button, where the user can make only one choice. 

#Radio Button - Represents one value of a variable that can have one of many values. Clicking the button sets the variable to that value, and clears all other radiobuttons associated with the same variable.

#Canvas - Structured graphics. This widget can be used to draw graphs and plots, create graphics editors, and to implement custom widgets.

#A text widget is used for multi-line text area. The Tkinter text widget is very powerful and flexible and can be used for a wide range of tasks. Though one of the main purposes is to provide simple multi-line areas, as they are often used in forms, text widgets can also be used as simple text editors or even web browsers. 

#Furthermore, text widgets can be used to display links, images, and HTML, even using CSS styles.

#In most other tutorials and text books, it's hard to find a very simple and basic example of a text widget. That's why we want to start our chapter with a such an example: 

#We create a text widget by using the Text() method. We set the height to 2, i.e. two lines and the width to 30, i.e. 30 characters. We can apply the method insert() on the object T, which the Text() method had returned, to include text. We add two lines of text.
# This program demonstrates a Button widget.
# When the user clicks the Button, an
# info dialog box is displayed.

#CREATING TEXT WIDGET WITH MESSAGE BOX

from Tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
mainloop()

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tkinter.Button(self.main_window, \
                                        text='Click Me!', \
                                        command=self.do_something)

        # Pack the Button.
        self.my_button.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    
    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response', \
                                    'Thanks for clicking the button.')

# # Create an instance of the MyGUI class.
my_gui = MyGUI()

# #2. You need to know how to create each GUI object in python.

# # This program demonstrates a group of Checkbutton widgets.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the checkbuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create three IntVar objects to use with
        # the Checkbuttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        
        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        
        # Create the Checkbutton widgets in the top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.cb_var3)

#         # Pack the Checkbuttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

#     # The show_choice method is the callback function for the
#     # OK button.
    
    def show_choice(self):
        # Create a message string.
        self.message = 'You selected:\n'

        # Determine which Checkbuttons are selected and
        # build the message string accordingly.
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'

        # Display the message in an info dialog box.
        tkinter.messagebox.showinfo('Selection', self.message)



# Create an instance of the MyGUI class.
my_gui = MyGUI()

#3. How do you draw a square/rectangle/circle?
This program draws a rectangle on a Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Draw a rectangle.
        self.canvas.create_rectangle(20, 20, 180, 180)
        
        # Pack the canvas.
        self.canvas.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()

4. How do you create a quit button?
This program has a Quit button that calls
the Tk class's destroy method when clicked.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Click Me!',
                                        command=self.do_something)

        # Create a Quit button. When this button is clicked
        # the root widget's destroy method is called.
        # (The main_window variable references the root widget,
        # so the callback function is self.main_window.destroy.)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)


        # Pack the Buttons.
        self.my_button.pack()
        self.quit_button.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    
    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking the button.')

# Create an instance of the MyGUI class.
my_gui = MyGUI()

5. How do you draw a straight line?
This program demonstrates the Canvas widget.
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Draw two lines.
        self.canvas.create_line(0, 0, 199, 199)
        self.canvas.create_line(199, 0, 0, 199)

        # Pack the canvas.
        self.canvas.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()

6. How do you create a radio button or a check box?

This program demonstrates a group of Radiobutton widgets.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = tkinter.IntVar()
        
        # Set the intVar object to 1.
        self.radio_var.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.radio_var,
                                       value=3)

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the
    # OK button.
    
    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You selected option ' +
                                    str(self.radio_var.get()))

# Create an instance of the MyGUI class.
my_gui = MyGUI()


Programs:
1. Different Constructors. What is the difference? How do you create an instance given each one? What are the attributes?
class Number:
def __init__ (self, value,sign):
self.value = value 
self.sign = sign
number1 = Number(12, "+")

class Number:
def __init__ (self, value, sign):
self.__value = value 
self.__sign = sign

number2 = Number(13, "+")

class Number:
def __init__ (self, value=0, sign = "+"):
self.value = value 
self.sign = sign

number3 = Number()

class Number:
def __init__ (self, value=1, sign = "-"):
self.__value = value
self.__sign = sign

number4 = Number()

class Number:
def __init__ (self, number):
self.value = abs(number) 
self.sign = Sign(number)

number5 = Number(5)

class Number:
def __init__ (self, number=-1):
self.value = abs(number) 
self.sign = Sign(number)

number6 = Number()

def Sign (number):
    if number >= 0:
        return "positive" 
    else:
        return "negative"

2. Superclass 
class Shape:
#return "negative"
#"This is a class for shapes. Default: 10 sides, 10 corners" 
    def __init__ (self,__sides, __corner=10):
        self.__corner=__corner 
        self.__sides=__corner
    #- Now write the get and set methods for the class Shape
    def set_sides(self, __sides):
        self.__sides = __sides

    def set_corner(self, __corner):
        self.__corner = __corner

    def get_sides(self):
        return self.__sides

    def get_corner(self):
        return 

shape1 = Shape(10)
print(shape1.get_sides())
#- Now write a subclass called Square and its constructor. One extra attribute for Square is area(-)
class Square(Shape):
    def __init__(self, __area):
        super(Shape, self).__init__()
        self.__area = __area

    def set_area(self, __area):
        self.__area = __area
        return self

    def get_area(self):
        return self.__area

square1 = Square(10)
print("Square Area: {}".format(square1))

#- Now write a subclass called Triangle and its constructor. One extra attribute for triangle is height(-) - Now create 3 triangles and 4 squares
class Triangle(Shape):
    def __init__(self, __height):
        super(Shape, self).__init__()
        self.__height = __height

    def set_height(self, __height):
        self.__height = __height
        return self

    def get_height(self):
        return self.__height

#- Now print out all the attributes of one of the triangles and one of the squares
#3. Class attribute
class Pet:
__goofy_name = "Goofy" def __init__ (self, name):
self.name = name
self.goofy_name = Pet.__goofy_name 
pet = Pet("Jojo") 
print(pet.goofy_name)



