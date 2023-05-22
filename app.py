
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("income_classifier.pkl", 'rb'))



@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/income_estimation_api',methods = ['POST'])
def income_estimation_api():
    data = request.json['data']
    data = pd.DataFrame(data,index=['i',])
    prediction = model.predict_proba(data)
    return "Probability of Income >= 50K $: " + str(round(prediction[0][1],2))

@app.route('/income_estimation',methods = ['POST'])
def income_estimation():
    data = [float(x) for x in request.form.values()]
    data = [data]
    prediction = model.predict_proba(data)
    return render_template("home.html",prediction_text = "Probability of Income >= 50K $: " + str(round(prediction[0][1],2)))

if __name__ == '__main__':
    app.run(debug=True)













