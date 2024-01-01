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

"""
This is a function makes player choosing if thy want to read the rules or not.
"""

answer = input('Do you wanna read the rules? (yes/no) :')
if answer.lower() == 'yes':
  print(
      green +
      'This is a Quiz Game with 20 questions. You will type in the answer to the question. If you get the answer right you will get a point. If you get the answer wrong you will not. Answer all your questions in lowercase. Good Luck '
      + user_name + '!')

"""
This is a function that asks the player if they are ready to play.
"""

answer = input(white + 'Are you ready to play my Quiz Game ? (yes/no) :')
score = 0
total_questions = 20     