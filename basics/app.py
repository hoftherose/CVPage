from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/welcome/<int:usr>')
def welcome(usr):
    return render_template("welcome.html", name=usr)

if __name__ == '__main__':
    app.run(debug=True)