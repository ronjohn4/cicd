from flask import Flask

app = Flask(__name__)
counter = 0

@app.route('/')
def index():
    return 'the test endpoint is /count'


@app.route('/count')
def counter_code():
    global counter
    counter = counter + 1
    return str(counter)


if __name__ == '__main__':
    app.run(debug=True)
