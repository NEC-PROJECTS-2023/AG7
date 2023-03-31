from flask import Flask,request,render_template,flash

import pickle

app = Flask(__name__)
model = pickle.load(open('final_model.sav','rb'))

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/',methods=['POST'])
def predict():
    gender = request.form['gender']
    age= request.form['age']
    aincome=request.form['aincome']
    spend_score=request.form['spend']
    l=[[gender,age,aincome,spend_score]]
    result = model.predict(l)
    return render_template('hello.html',a="The customer is in cluster "+str(result))

if __name__ == '__main__':
    app.run(debug=True)
