<h1 style="text-align: center;"><strong>QUIZ GAME</strong></h1>

<p align="center">
<img src="image-readme/responsive.png" alt="Responsive Image" style="border-radius: 100px; width: 400px; height: 350px;">
</p>

# Overview

Welcome to the Quiz Game! This is a simple yet engaging command-line quiz game developed in Python. The game consists of 20 questions, covering a wide range of topics from pop culture to geography. The objective is to answer the questions correctly to earn points. The game is designed to be fun and educational, making it a great way to test your knowledge or learn something new.
<br>
<br>
<p align="center">
<img src="image-readme/landingpage.png" alt="Responsive Image" style="border-radius: 20px; width: 400px; height: 350px;">
</p>

## Features

- Colorful Interface: The game uses the colored library to display text in different colors, making it more visually appealing and easier to follow.
- User Input Validation: The game includes functions to validate user input, ensuring that the user provides a valid answer for each question.
- Quiz Rules and Instructions: Before starting the game, users have the option to read the rules. This includes information about the game's structure, scoring system, and how to answer questions.
- Score Calculation: At the end of the game, the user's score is calculated based on the number of correct answers, and the percentage of correct answers is displayed.
- Unit Testing: The game includes unit tests to ensure the functionality of the input validation functions works as expected.

## Rules
- Here u have the rules of the game.
- You can choose to read the rules or not.
- The rules are simple.

![](image-readme/rules.png)

## Installation

To play the Quiz Game, you need to have Python installed on your system. The game uses the `colored` library for colored output, so you will need to install it using pip:

```
pip install colored
```

## Usage
- Here you can find the repository [click here](https://github.com/AndersH82/a_quiz_game.git)
- Clone the repository or download the `run.py` file.
- Open your terminal or command prompt.
- Navigate to the directory containing `run.py`.
- Run the game by executing the following command:

```
python run.py
```
- Follow the on-screen instructions to play the game.

- If you don't want to play in the terminal, you can go [here](https://a-quiz-game-69878e1225dc.herokuapp.com/)  and there to play via the browser.

## Program and libraries used

- Codeanywear - codeanywhere.com for coding
- Github - github.com for deployment
- Replit - replit.com for coding
- Grammarly - grammarly.com for grammar and spelling
- Mentimeter - mentimeter.com for questions
- Studytonight - studytonight.com  for coloring the text
- W3schools - w3schools.com for input codes
- Youtube - youtube.com for research
- Codewof - codewof.co.nz for checking the PEP8 style
- Heroku - heroku.com for deployment
- Unittest - for testing the code
- Pycodstyle - testing of code style

## Testing

#### Unittest

The `test.py` script uses the `unittest` framework for structuring and running the tests. It also leverages the `unittest.mock` library to simulate user input during testing, ensuring that the tests are deterministic and do not depend on actual user interaction.

#### Test Cases

`test_get_yes_no_input_yes`: Tests the `get_yes_no_input` function with a mocked input of 'yes'.
`test_get_yes_no_input_no`: Tests the `get_yes_no_input` function with a mocked input of 'no'.
`test_get_yes_no_input`: Tests the `get_yes_no_input` function with a mocked input of 'yes' for a different prompt.
`test_get_non_blank_input`: Tests the `get_non_blank_input` function with a mocked input of 'john'.

#### Running the test
To run the tests, execute the following command in your terminal:

```
python -m unittest test.py
```

#### Dependencies

Python 3.3 or higher
unittest and unittest.mock libraries (included in the Python Standard Library)

#### Result

<img src="image-readme/test.png">

### PEP8 test

#### How to run pycodestyle test

To run a `pycodestyle` test, you can either use the command line interface or integrate it into your Python code for automated testing. Here's how to do both:

#### Using the Command Line Interface

- Installation: First, ensure `pycodestyle` is installed. If not, you can install it using pip:

```
pip install pycodestyle
```

- Running pycodestyle: To check a Python file or directory for PEP 8 compliance, use the following command:

```
pycodestyle run.py
```
## Deployment

Quiz Game is deployed on Heroku.com and you can see the app here [click here](https://a-quiz-game-69878e1225dc.herokuapp.com/) 

## Contributing
Contributions to the Quiz Game are welcome! If you have suggestions for new questions or improvements to the game, please feel free to open an issue or submit a pull request.