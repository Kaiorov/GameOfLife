from flask import Flask
from flask import render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    gol = GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    gen = GameOfLife()
    if gen.counter > 0:
        gen.form_new_generation()
    gen.counter += 1
    return render_template('live.html', world=gen)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)