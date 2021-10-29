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
     school = request.args.get('school')
     sex = request.args.get('sex')
     address = request.args.get('address')
     famsize = request.args.get('famsize')
     Pstatus = request.args.get('Pstatus')
     Mjob = request.args.get('Mjob')
     Fjob = request.args.get('Fjob')
     reason = request.args.get('reason')
     guardian = request.args.get('guardian')
     schoolsup = request.args.get('schoolsup')
     famsup = request.args.get('famsup')
     paid = request.args.get('paid')
     activities = request.args.get('activities')
     nursery = request.args.get('nursery')
     higher = request.args.get('higher')
     internet = request.args.get('internet')
     romantic = request.args.get('romantic')
     data = [[age],[health],[absences], [school], [sex], [address], [famsize], [Pstatus], [Mjob], [Fjob], [reason], 
            [guardian], [schoolsup], [famsup], [paid], [activities], [nursery], [higher], [internet], [romantic]]
     query_df = pd.DataFrame({ 'age' : pd.Series(age) ,'health' : pd.Series(health) ,'absences' : pd.Series(absences),
                                'school': pd.Series(school), 'sex': pd.Series(sex), 'address': pd.Series(address),
                                'famsize': pd.Series(famsize), 'Pstatus': pd.Series(Pstatus), 'Mjob': pd.Series(Mjob), 
                                'Fjob': pd.Series(Fjob), 'reason': pd.Series(reason), 'guardian': pd.Series(guardian), 
                                'schoolsup': pd.Series(schoolsup), 'famsup': pd.Series(famsup), 'paid': pd.Series(paid), 
                                'activities': pd.Series(activities), 'nursery': pd.Series(nursery), 'higher': pd.Series(higher), 
                                'internet': pd.Series(internet), 'romantic': pd.Series(romantic)})
    
     Names = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
     for col in Names: 
        jobs_encoder = LabelBinarizer()
        jobs_encoder.fit(query_df[col])
        transformed = jobs_encoder.transform(query_df[col])
        ohe_df = pd.DataFrame(transformed)
        df = pd.concat([query_df, ohe_df], axis=1).drop([col], axis=1)

     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/bettermodel.pkl')
    app.run(host="0.0.0.0", debug=True)