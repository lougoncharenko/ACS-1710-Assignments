# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

#**************** Hello World **********************

 #import the flask library
from flask import Flask
import random 
#set our app variable to write routes
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello user! Welcome to the homepage!'

#**************** Favorite Animal **********************
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'{users_animal} is an awesome animal!'

#**************** Favorite Dessert**********************
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'{users_dessert} sounds delicious'


@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'We went camping and ran into a {adjective} {noun}.'

@app.route('/multiply/<number1>/<number2>')
def multiply_2_numbers(number1, number2):
    if (type(number1) == int and type(number2) == int ):
        total = number1 + number2
        return f'{number1} times {number2} is {total}'
    else:
        return 'Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>') 
def say_N_times(word, n):
    if(type(n) == int):
        return f'{word}' * n
    else:
        return 'Invalid input. Please try again by entering a word and a number!'


@app.route('/dicegame')
def dice_game():
    number = random.randint(0,6)
    if (number == 6):
        return f' you rolled a 6. You won!'
    else:
        return f'You rolled a {number}. You lost!'


if __name__ == '__main__':
    app.run(debug=True)