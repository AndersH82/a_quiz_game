from colored import fg

# Define colors
blue = fg('blue')
red = fg('red')
green = fg('green')
yellow = fg('yellow')
white = fg('white')

# Function to get non-blank input
def get_non_blank_input(question):
    while True:
        answer = input(question)
        if answer.strip():
            return answer.lower()
        else:
            print("Please provide an answer.")

# Function to validate user input for yes/no questions
def get_yes_no_input(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Please enter 'yes' or 'no'.")

# Get user name
user_name = input('Enter your name: ')
while not user_name:
    print("You must enter a name. Please try again.")
    user_name = input('Enter your name: ')

print('Welcome ' + user_name + ' to my Quiz Game.')

# Check if user wants to read the rules
if get_yes_no_input(green + 'Do you wanna read the rules? (yes/no) :') == 'yes':
    print(
        green +
        'This is a Quiz Game with 20 questions.'
        'You will type in the answer to the question.'
        'If you get the answer right you will get a point.'
        'If you get the answer wrong you will not.'
        'Answer all your questions in lowercase. Good Luck ' + user_name + '!')

# Check if user is ready to play
if get_yes_no_input(white + 'Are you ready to play my Quiz Game ? (yes/no) :') == 'yes':
    score = 0
    total_questions = 20
    questions = [
        'Who has won the most total Academy Awards? ',
        'What artist has the most streams on Spotify? ',
        'What country drinks the most coffee per capita? ',
        'What sports car company manufactures the 911? ',
        'What character have both Robert Downey Jr. and Benedict Cumberbatch played? ',
        'Who famously crossed the Alps with elephants on the way to war with the Romans? ',
        'What is a group of crows called? ',
        'Which is the only body part that is fully grown from birth? ',
        'What planet is closest to the sun? ',
        'Where is the strongest human muscle located? ',
        'What phone company produced the 3310? ',
        'What is the only continent with land in all four hemispheres? ',
        'What is the capital of Ireland? ',
        'What is the capital of Canada? ',
        'On what continent would you find the city of Baku? ',
        'What is the smallest US state by area? ',
        'What is the state capital of New York? ',
        'Which river flows through the Grand Canyon? ',
        'What is the only flag that does not have four sides? ',
        'Where did sushi originate? '
    ]
    answers = [
        'walt disney',
        'drake',
        'finland',
        'porsche',
        'sherlock holmes',
        'hannibal',
        'a murder',
        'eyes',
        'mercury',
        'jaw',
        'nokia',
        'africa',
        'dublin',
        'ottawa',
        'asia',
        'rhode island',
        'albany',
        'colorado river',
        'nepal',
        'china'
    ]

    for i, question in enumerate(questions, start=1):
        user_answer = get_non_blank_input(yellow + 'Question ' + str(i) + ': ' + question)
        if user_answer == answers[i-1]:
            score += 1
            print(green + 'Correct')
        else:
            print(red + 'Wrong Answer')

    # Calculate and display the score
    score_percentage = (score / total_questions) * 100
    print(
        blue + 'Thanks ' + user_name +
        ' for playing my fun quiz game, you attempted', score,
        "questions correctly!")
    print(user_name, 'you got', score_percentage, 'points.')
    print(yellow + 'Thanks for playing. BYE! BYE!')
else:
    print("Okay, maybe next time.")
