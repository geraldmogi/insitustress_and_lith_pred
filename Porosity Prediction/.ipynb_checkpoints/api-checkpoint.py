import pandas as pd
import joblib
from flask import Flask, request, jsonify
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Create Flask App
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='PHIE:'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    # GET JSON REQUEST
    feat_data = request.json
    # CONVERT JSON to PANDAS DF (col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    # PREDICT
    prediction = list(model.predict(df))
    
    
    return jsonify({'prediction':str(prediction)})


# LOAD MY MODEL and LOAD COLUMN NAMES
if __name__ == '__main__':
    
    model = joblib.load("model.pkl")
    col_names = joblib.load('col_names.pkl')
    
    app.run(debug=True)