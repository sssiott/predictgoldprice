from flask import Blueprint, render_template, request
import numpy as np
import pickle

bp = Blueprint('predict',__name__,url_prefix='/predict')

loaded_model = pickle.load(open("model1.pkl", "rb"))
# with open('model/model1.pkl', 'rb') as file:
#     model = pickle.load(file)

@bp.route('/')
def inputdata():
    return render_template('predict.html')

@bp.route('/result',methods=['POST'])
def printresult():

    kospi = float(request.form['kospi'])
    kosdaq = float(request.form['kosdaq'])
    sp500 = float(request.form['sp500'])
    nasdaq = float(request.form['nasdaq'])
    exchange = float(request.form['exchangerate'])
    bok = float(request.form['bok'])
    btc = float(request.form['btc'])

    data = np.array([kospi,kosdaq,sp500,nasdaq,exchange,bok,btc]).reshape([1,-1])

    pred = loaded_model.predict(data)
    result = int(pred)
   
    return render_template('result.html',data=result)
