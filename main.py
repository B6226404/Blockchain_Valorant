from flask import Flask
from flask import render_template
from flask import request

from block import write_block, check_integrity, view_block

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        map = request.form.get('map')
        team_win = request.form.get('team_win')
        team_lost = request.form.get('team_lost')
        win_score = request.form.get('win_score')
        lost_score = request.form.get('lost_score')
        mvp = request.form.get('mvp')
        
        write_block(map, team_win, team_lost, win_score, lost_score, mvp)

    return render_template('index.html')

@app.route('/check')
def check():
    results = check_integrity()
    return render_template('check.html', checking_results=results)

@app.route('/view')
def view():
    db = view_block()
    return render_template('view.html', view = db)


if __name__=='__main__':
    app.run(debug=True)