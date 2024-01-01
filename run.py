"""
This is a simple Quiz Game that asks the user a series of questions and checks their answers.
"""

from colored import fg

"""
This is a function that prints out a message with a colored background.
"""

blue = fg('blue')
red = fg('red')
green = fg('green')
yellow = fg('yellow')
white = fg('white')

"""
This is a function that lets player input their name.
"""

user_name = input('Enter your name: ')
print('Welcome ' + user_name + ' to my Quiz Game.')