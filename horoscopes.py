from flask import Flask
app = Flask(__name__)

...
from random import choice

horoscopes = ['you will grow lips on your forehead', 'the next ten minutes will be above average', 'here is your chance', 'eat more eggs', 'the west is the best', 'the snake is long, seven miles']

@app.route('/horoscope')
def get_horoscopes():
    horoscope = choice(horoscopes)
    return f'Hello there, user! Your horoscope for today is {horoscope}!'

print (get_horoscopes())

if __name__ == "__main__":
   app.run(debug=True)