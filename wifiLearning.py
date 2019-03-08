import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import json
from sklearn.externals import joblib

isLearningMode = False

with open("result_-100.json") as f:
    data = json.load(f)

x = data["question"]
y = data["answer"]

x = np.array(x, dtype=np.float64)
y = np.array(y, dtype=np.float64)
y = np.argmax(y, axis=1)

size = x.shape[0]

logreg = RandomForestClassifier(n_estimators=100)

if isLearningMode:
    logreg.fit(x[:size - 100], y[:size - 100])
    prediction = logreg.predict(x[size - 100:])
    accuracy = np.sum(prediction == y[size - 100:]) / float(100) * 100
    print("accuracy : " + str(accuracy) + "%")
else:
    logreg.fit(x, y)
    joblib.dump(logreg, "model.pkl")


