from flask import Flask
import time
import random

app = Flask(__name__)


@app.route('/')
def guess():
    return ('<h1> Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


random_number = random.randint(0,9)
print(random_number)


@app.route('/<int:number>')
def check_the_guess(number):
    if int(number) < random_number:
        return ('<h1>Too low, try again !</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif int(number) > random_number:
        return ('<h1>Too high, try again !</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        return ('<h1>You got it right !</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')



if __name__ == "__main__":
    app.run(debug=True)
