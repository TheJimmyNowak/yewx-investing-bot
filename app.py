from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signals/')
def signals():
    pass


@app.route('/positions/')
def positions():
    pass


@app.route('/models/')
def models():
    pass


if __name__ == '__main__':
    app.run()
