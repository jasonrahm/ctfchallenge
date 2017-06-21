from app import app
from flask import flash
from flask import render_template


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/challenge/<int:challenge_id>', methods=['GET'])
def challenge(challenge_id):
    if challenge_id == 1:
        return render_template('one.html')
    elif challenge_id == 2:
        return render_template('two.html')
    elif challenge_id == 3:
        return render_template('three.html')
    elif challenge_id == 4:
        return render_template('four.html')
    elif challenge_id == 5:
        return render_template('five.html')
    else:
        flash('Not a valid challenge')
        return render_template('index.html')


@app.errorhandler(404)
def nofile(error):
    return render_template('404.html')