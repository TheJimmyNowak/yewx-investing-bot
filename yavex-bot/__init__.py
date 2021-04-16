from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signals/')
def signals():
    return render_template('signals.html')


@app.route('/positions/')
def positions():
    return render_template('positions.html')


@app.route('/models/')
def models():
    return render_template('models.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
