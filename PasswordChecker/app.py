import re

from flask import Flask, render_template, request

app = Flask(__name__)


def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    # Check for at minimum one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()-_=+{};:,.<>?/\\|`~]', password):
        return False

    return True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if check_password_strength(password):
            result_message = 'Yeayy! You have entered a Strong password'
        else:
            result_message = 'Oops! Weak password. Retry!'
        return render_template('index.html', result_message=result_message)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

