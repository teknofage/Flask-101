from flask import Flask, request

app = Flask(__name__)

...
from random import choice

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    compliment = choice(compliments)
    return f'Hello there, user! You are so {compliment}!'

# print (get_compliment())

if __name__ == "__main__":
    app.run(debug=True)