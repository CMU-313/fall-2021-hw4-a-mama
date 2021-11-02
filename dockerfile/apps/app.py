from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer


app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     Medu = request.args.get('Medu')
     Fedu = request.args.get('Fedu')
     traveltime = request.args.get('traveltime')
     failures = request.args.get('failures')
     studytime = request.args.get('studytime')
     famrel = request.args.get('famrel')
     freetime = request.args.get('freetime')
     goout = request.args.get('goout')
     Dalc = request.args.get('Dalc')
     Walc = request.args.get('Walc')
     G1 = request.args.get('G1')
     G2 = request.args.get('G2')
     query_df = pd.DataFrame({ 'age' : pd.Series(age) ,'health' : pd.Series(health) ,'absences' : pd.Series(absences),
                                'Medu': pd.Series(Medu), 
                                'Fedu': pd.Series(Fedu), 'traveltime': pd.Series(traveltime), 'failures': pd.Series(failures),
                                'studytime': pd.Series(studytime), 'famrel': pd.Series(famrel), 'freetime': pd.Series(freetime),
                                'goout': pd.Series(goout), 'Dalc': pd.Series(Dalc), 'Walc': pd.Series(Walc), 'G1': pd.Series(G1), 
                                'G2': pd.Series(G2)})
    
     prediction = clf.predict(query_df)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/bettermodel.pkl')
    app.run(host="0.0.0.0", debug=True)