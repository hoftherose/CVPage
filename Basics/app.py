from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/Hello')
def home():
    return "Hello World!"

def say_bye():
    return "Good Bye"

app.add_url_rule('/Bye', view_func=say_bye)

@app.route('/Wassap/<string:name>')
def wassap(name):
    return f"Wassap {name}"

@app.route('/<int:leaving>')
def in_or_out(leaving):
    if leaving:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('say_bye'))

if __name__ == '__main__':
    app.run(debug=True)