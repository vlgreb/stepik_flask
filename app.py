from flask import Flask, render_template

from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(width=25, height=25)
    return render_template('index.html')


@app.route('/live')
def live():
    game_of_life = GameOfLife()
    if game_of_life.counter > 0:
        game_of_life.form_new_generation()
    game_of_life.counter += 1
    return render_template('live.html', game_of_life=game_of_life)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
