from flask import Flask, request, render_template
import random 
app = Flask(__name__)

@app.route('/')
def display_homepage():
    return render_template('homepage.html')

@app.route('/froyo')
def choose_froyo():
    return render_template('froyo-form.html')

@app.route('/results', methods=['GET'])
def froyo_results():
    context = {
        'name': request.args.get('full_name'),
        'users_email': request.args.get('email'),
        'users_phone': request.args.get('phone'),
        'flavor': request.args.get('flavor'),
        'pizza_size': request.args.get('size'),
        'toppings': request.args.get('toppings')
    }
    return render_template('froyo-results.html', **context)


@app.route('/favorites')
def choose_favorites():
    return render_template('fav-form.html')

@app.route('/favorite_results', methods=['GET'])
def favorite_results():
    context = {
        'color': request.args.get('color'),
        'animal': request.args.get('animal'),
        'city': request.args.get('city')
    }
    return render_template('fav-results.html', **context)


@app.route('/secret_message')
def secret_message():
    return render_template('sec-mess-form.html')

@app.route('/message_results', methods=['POST'])
def display_secret_message():
   secret_message = request.form.get('secret_message')
   def sortString(str):
    return ''.join(sorted(str))
   secret_message= sortString(secret_message)

   context = {
    'secret_message': secret_message
   }
   return render_template('sec-mess-results.html', **context)


@app.route('/calculator')
def calculator_form():
    return render_template('calculator-form.html')


@app.route('/calculator_results', methods=['GET'])
def calculator_results():
    operation = request.args.get('operation')
    first_number = request.args.get('first-number')
    second_number = request.args.get('second-number')

    if (operation == 'add'):
        result = int(first_number) + int(second_number)
    elif (operation == 'subtract'):
        result = int(first_number) - int(second_number)
    elif (operation == 'multiply'):
        result = int(first_number) * int(second_number)
    elif (operation == 'division'):
        result = int(first_number) / int(second_number)

    context = {
    'operation': operation,
    'first_number': first_number,
    'second_number': second_number,
    'result': result
    }
    return render_template('calculator-results.html', **context)



@app.route('/horoscope')
def horoscope():
    return render_template('horoscope_form.html')


@app.route('/horoscope_results', methods=['GET'])
def display_horoscope():
    month = request.args.get('month')
    day = request.args.get('day')
    if (month == 'jan'):
        sign = 'Aquarius'
        horoscope = "Will you go out with me? Be careful if a person says yes when you ask that question today, Aquarius. You could take the nature of this situation to the extreme. Saying yes doesn't mean you're suddenly in charge of his or her life. Nor are you responsible for anything that person does or how they feel. If you're still asking the question without getting any positive responses, don't worry. Keep trying."
    if (month == 'feb'):
        sign = 'pisces'
        horoscope = "Powerful issues arise in your life that make it difficult to find peace, Pisces. Perhaps your first tendency is to confide in your partner. More than likely, this person is contributing to the difficulties you're now having. Your best bet is to spend some time alone. If you're already alone, so much the better. Cherish this time instead of letting it make you mad."
    if (month == 'mar'):
        sign = 'aries'
        horoscope = 'You may be trying to get to the end of the road too quickly without really enjoying all the steps along the way'
    if (month == 'apr'):
        sign = 'Taurus'
        horoscope = 'When your heart is gently touched, it feels loving, generous, and supportive of everyone, Taurus. If your heart is lonely, it feels deserted by everyone.'
    if (month == 'may'):
        sign = 'gemini'
        horoscope = "You may be like a giant trying to befriend a small bug, Gemini. You have absolutely nothing in common and don't even speak the same language. With one accidental move, you could easily squash that little bug. This isn't to say that you can't learn to become best friends. Just know that this kind of relationship is going to take some work."
    if (month == 'jun'):
        sign = 'cancer'
        horoscope = "There is irony in today's situation, Cancer. The only real remedy for situations like this is to accept them and joke about it. If you try to take yourself too seriously, especially when it comes to art or romance, you will inevitably fail."
    if (month == 'jul'):
        sign = 'Leo'
        horoscope = "The hungrier you get, the more determined you will become, Leo. Be careful that your determination doesn't turn into desperation and neediness. It's unattractive and will get you nowhere. Keep on the upward spiral, and let determination turn into inspiration and cooperation. You will find this especially true when it comes to matters of the heart. You have a great deal of power. Put it to good use."
    if (month == 'aug'):
        sign = 'virgo'
        horoscope = "If you're in the market for romance, Virgo, whether with a new partner or rekindling the fire with a current partner, be careful. Small issues could rage out control today. Extreme conditions are likely to occur, thanks to your sensitive emotions combined with a surge of energy from the outside. Try not to get too upset when tension rises because of something unimportant."
    if (month == 'sept'):
        sign = 'libra'
        horoscope = "Things may get a bit difficult in your romantic life because of someone in the partnership who isn't necessarily taking a very realistic approach to the situation, Libra. There's a bit of a power play going on as someone tries to throw their weight around without considering the other person's feelings. Tension is brewing, and you'd be wise to deal with it now."
    if (month == 'oct'):
        sign = 'scorpio'
        horoscope = "Your creative juices are flowing freely, Scorpio, but there appears to be a roadblock. Something or someone apparently doesn't want you to continue down the path you're on. Perhaps he or she is scared that you're going to discover a whole new passion in life that they don't necessarily agree with. Don't forget who is running your show - you and no one else."
    if (month == 'nov'):
        sign = 'saggitarius'
        horoscope = "At the end of the day, you're the one who has to look in the mirror and know who you are, Sagittarius. Think about this the next time you're tempted to make a rude comment or spread a displeasing fact about someone else. One side of you may be able to rationalize behavior that the other side simply despises. Today look at both of sides of yourself, not just the one that pleases you."
    if (month == 'dec'):
        sign = 'capricorn'
        horoscope = "When it comes to romance, your body is apt to turn to jelly today. You may be so emotional that you can't function, Capricorn. That's love. And even though it can be heavenly, it can also be debilitating. You could deliberate for hours about an issue because you don't want to make a move without your partner's input. If you don't have a romantic partner now, find one soon, but not today."
    lucky_number = random.randint(1,99)
    context = {
        'name': request.args.get('operation'),
        'horoscope': horoscope,
        'lucky_number': lucky_number
    }
    return render_template('horoscope_result.html', **context)


if __name__ == '__main__':
    app.run(debug=True, port = 3000)

