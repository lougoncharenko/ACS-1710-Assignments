# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

#**************** Hello World **********************

 #import the flask library
from flask import Flask
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


if __name__ == '__main__':
    app.run(debug=True)