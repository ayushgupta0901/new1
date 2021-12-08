## Integrating HTML
## HTML get and post



##{%--%} statements and loops
##{{}} expression to print output
## {#--#} fro comments


from flask import Flask, redirect,url_for,render_template,request
import markupsafe
from jinja2 import escape

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index3.html')

@app.route('/success/<int:score>')
def success(score): 
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    exp={'score':score , 'result':res}
    return render_template('result.html',result=exp)
   
@app.route('/fail/<int:score>')
def fail(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    exp={'score':score , 'result':res}
    return render_template('result.html',result=exp)
   ##result checker
@app.route('/result/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))   

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        C=float(request.form['C'])
        Data_Science=float(request.form['DataScience'])
        total_score=(science+maths+C+Data_Science)
    res=''
    if total_score>=50:
        res='success'
    else:
        res='fail'
    return redirect(url_for(res,score=total_score))


if __name__== '__main__':
    app.run(debug=True)

