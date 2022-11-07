from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'some key'
import random
@app.route('/')       
def index():
    if session:
        if session['randNumber']:
            return render_template('index.html')
    session['randNumber'] = random.randint(1,100)
    print(session['randNumber'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['randNr']) == int(session['randNumber']):
        [session.pop(key) for key in list(session.keys()) if key == 'lower']
        [session.pop(key) for key in list(session.keys()) if key == 'higher']
        session['correct'] = 'Correct'
        return redirect('/')
    elif int(request.form['randNr']) < int(session['randNumber']):
        [session.pop(key) for key in list(session.keys()) if key == 'higher']
        [session.pop(key) for key in list(session.keys()) if key == 'correct']
        session['lower'] = 'Your nr is lower'
        return redirect('/')
    else:
        [session.pop(key) for key in list(session.keys()) if key == 'lower']
        [session.pop(key) for key in list(session.keys()) if key == 'correct']

        session['higher'] = 'Your nr is higher'
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True) 