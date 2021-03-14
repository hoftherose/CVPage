from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/Hello')
def home():
    return "Hello World!"

def say_bye():
    return "Good Bye"

app.add_url_rule('/Bye', view_func=say_bye)

if __name__ == '__main__':
    app.run(debug=True)