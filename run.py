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
This is a function that makes players choose if they want to read the rules or not.
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

"""
This is the function of all 20 questions for the players to answer correct or wrong answer.
"""

if answer.lower() == 'yes':
    answer = input(yellow +
                   'Question 1: Who has won the most total Academy Awards? ')
if answer.lower() == 'walt disney':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 2: What artist has the most streams on Spotify? ')
if answer.lower() == 'drake':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow + 
               'Question 3: What country drinks the most coffee per capita? ')
if answer.lower() == 'finland':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 4: What sports car company manufactures the 911? ')
if answer.lower() == 'porsche':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 5: What character have both Robert Downey Jr. and Benedict Cumberbatch played? ')
    
if answer.lower() == 'sherlock holmes':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 6: Who famously crossed the Alps with elephants on the way to war with the Romans? ')
if answer.lower() == 'hannibal':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 7: What is a group of crows called? ')
if answer.lower() == 'a murder':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 8: Which is the only body part that is fully grown from birth? ')
if answer.lower() == 'eyes':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 9: What planet is closest to the sun? ')
if answer.lower() == 'mercury':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 10: Where is the strongest human muscle located? ')
if answer.lower() == 'jaw':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 11: What phone company produced the 3310? ')
if answer.lower() == 'nokia':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 12: What is the only continent with land in all four hemispheres? ')
if answer.lower() == 'africa':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 13: What is the capital of Ireland? ')
if answer.lower() == 'dublin':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 14: What is the capital of Canada? ')
if answer.lower() == 'ottawa':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 15: On what continent would you find the city of Baku? ')
if answer.lower() == 'asia':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 16: What is the smallest US state by area? ')
if answer.lower() == 'rhode island':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 17: What is the state capital of New York? ')
if answer.lower() == 'albany':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 18: Which river flows through the Grand Canyon? ')
if answer.lower() == 'colorado river':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 19: What is the only flag that does not have four sides? ')
if answer.lower() == 'nepal':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

answer = input(yellow +
               'Question 20: Where did sushi originate? ')
if answer.lower() == 'china':
    score += 1
    print(green + 'Correct')
else:
    print(red + 'Wrong Answer')

"""
This is a function that prints out the score and the percentage and thanks the player for playing the game.
""" 

print(
    blue + 'Thanks ' + user_name +
    ' for playing my fun quiz game, you attempted', score,
    "questions correctly!")
(score) = (score / total_questions) * 100
print(user_name, 'you got ' + str(score), 'points.')
print(yellow + 'Thanks for playing. BYE! BYE!')    