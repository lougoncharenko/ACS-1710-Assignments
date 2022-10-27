from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def display_homepage():
    return render_template('index.html')

#creating a form
@app.route('/form')
def display_form():
    return render_template('form.html')

# the route utilized by the above <form> tag
@app.route('/results', methods=['GET'])
def simple_pizza_results():
    # context object contains all of the needed form data for template
    context = {
        'name': request.args.get('full_name'),
        'users_email': request.args.get('email'),
        'users_phone': request.args.get('phone'),
        'crust_type': request.args.get('crust'),
        'pizza_size': request.args.get('size'),
        'toppings': request.args.get('toppings')
    }
    return render_template('order.html', **context)
 
if __name__ == '__main__':
    app.run(debug=True, port=3000)