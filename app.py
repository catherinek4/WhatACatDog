from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/header/')
def show_header():
    return render_template('header.html')


@app.route('/signUp/')
def show_signUp():
    return render_template('signUp.html')


@app.route('/signIn/')
def show_signIn():
    return render_template('signIn.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4567)
