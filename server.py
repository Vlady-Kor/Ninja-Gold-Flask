from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'activity' not in session:
        session['activity']= []
    return render_template("index.html", rand_num=session['gold'], activities=session['activity'])


@app.route('/process_money',methods=['POST'])
def money():
    farm_money=random.randint(10,20)
    cave_money=random.randint(5,10)
    house_money=random.randint(2,5)
    casino_money=random.randint(-50,50)
    if request.form['building'] =='farm':
        session['gold']+=farm_money
        session['activity'].append('You earned: ' + str(farm_money))
    if request.form['building'] =='cave':
        session['activity'].append('You earned: ' + str(cave_money))
        session['gold']+=cave_money
    if request.form['building'] =='house':
        session['gold']+=house_money
        session['activity'].append('You earned: ' + str(house_money))
    if request.form['building'] =='casino':
        session['gold']+=casino_money
        session['activity'].append('You earned: ' + str(casino_money))
    print(session['gold'])
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)