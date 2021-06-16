from warnings import catch_warnings
from flask import Flask, render_template, url_for, request, redirect
from flask import Flask
from flask_cors import CORS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import *  
from datetime import datetime  
import datetime as dt  
import time 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn.metrics as sm
from sklearn.neighbors import KNeighborsClassifier

# Init the Flask Application
app = Flask(__name__)
CORS(app)

# Load the data (locally now)
data = pd.read_csv(r'model_data.csv')
pd.set_option('display.max_columns', None)

# Drop unnecessary data for the model
data_mod = data.drop(['DATE', 'ActualDestinationStationCode', 'DepartureStationCode'], axis = 1)

# Split the train and test data
y = data_mod.delay_category
X = data_mod.drop('delay_category', axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state = 0)

# Fit the model
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train,y_train)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    departureCode = request.json['fromStation']
    arrivalCode = request.json['toStation']
    travelDate = request.json['time']

    try:
        result = data[(data['ActualDestinationStationCode'] == arrivalCode) &
             (data['DepartureStationCode'] == departureCode) &
             (data['DATE'] == travelDate)]
        result = result.reset_index().drop('index', axis = 1)
 
        prediction = knn.predict([[result['PlatformChanged'][0], result['Intercity'][0], result['FG'][0], result['FHX'][0], result['FHN'][0], result['FXX'][0], result['numberOfStops'][0]]])
        
        return str(prediction[0])
    except:
        return "There were no related results found.";


if __name__ == "__main__":
    app.run(debug=True)