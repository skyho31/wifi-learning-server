import json
from bottle import run, post, request, response, get, route
import os
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

with open("BSSID.json") as f:
    bssidList = json.load(f)

logreg = joblib.load('model.pkl')

def indexOfElem(list, elem):
    index = -1
    for item in list:
        index += 1
        if elem == item:
            return index
    return -1

@post('/upload')
def process():
    try:
        wifiInfo = request.json.get('wifiInfo')
        inputList = [-100.0 for i in range(0, len(bssidList))]
        
        for wifiElem in wifiInfo:
            index = indexOfElem(bssidList, wifiElem['BSSID'])
            if index >= 0:
                inputList[index] = float(wifiElem['level'])
    
        inputList = np.array([inputList])
        prediction = logreg.predict(inputList)
        print(prediction)

        return str(prediction[0])
    except Exception as ex:
        print(ex)
        return "error"

run(host='0.0.0.0', port=8800, debug=True)
