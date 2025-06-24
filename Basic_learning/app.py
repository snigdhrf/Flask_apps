import joblib
import numpy as np

model = joblib.load('model.pkl')

## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')

    else:
        try:
            maths = float(request.form['maths'])
            science = float(request.form['science'])
            history = float(request.form['history'])

            average_marks = (maths + science + history) / 3

            # ML prediction
            input_data = np.array([[maths, science, history]])
            prediction = model.predict(input_data)[0]

            # Interpret result
            if prediction == 1:
                grade = "ML Predicted Pass"
                remark = "✔️ Congratulations! You passed according to our model."
            else:
                grade = "ML Predicted Fail"
                remark = " The model predicts a fail. Don't give up!"

            return render_template('result.html', results=average_marks, grade=grade, remark=remark)

        except ValueError:
            error_message = " Please enter valid numbers in all fields."
            return render_template('calculate.html', error=error_message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)