from flask.wrappers import Request
import pandas as pd
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.python.types.core import Value

label_encoder = LabelEncoder()
X_scaler = MinMaxScaler()
model = load_model('finalfinal1.h5')
app = Flask(__name__,template_folder="templates")    

rawdata2 = pd.read_csv('mydata.csv')
X = rawdata2.drop("probable_popularity", axis=1)
y = rawdata2["probable_popularity"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, random_state=0, train_size =0.2)

X_scaler = MinMaxScaler().fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Step 1: Label-encode data set
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
encoded_y_train = label_encoder.transform(y_train)
encoded_y_test = label_encoder.transform(y_test)

# Step 2: Convert encoded labels to one-hot-encoding
y_train_categorical = to_categorical(encoded_y_train)
y_test_categorical = to_categorical(encoded_y_test)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    model.summary()

    # v2 = np.asarray([[float(x) for x in request.form.values()]])
    v2 = criteria_function()
    print(v2)
    
    test_data = X_scaler.transform(v2)
    encoded_predictions = np.argmax(model.predict(test_data),axis=1)
    print(encoded_predictions)

    prediction_labels = label_encoder.inverse_transform(encoded_predictions)
    print(prediction_labels)

    return render_template('index.html', prediction_text=(prediction_labels[0]))
    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    # v3= np.asarray([[float(x) for x in request.form.values()]])
    v3 = criteria_function()
    print(v3)

    test_data = X_scaler.transform(v3)
    encoded_predictions = np.argmax(model.predict(test_data),axis=1)
    print(encoded_predictions)

    prediction_labels = label_encoder.inverse_transform(encoded_predictions)
    return jsonify(prediction_labels[0])

def criteria_function():
    criteria = [[
    float(request.form['a']),
    float(request.form['Danceability']),
    float(request.form['Energy']),
    float(request.form['Instrumentalness']),
    float(request.form['Liveness']),
    float(request.form['Speechiness']),
    float(request.form['Tempo']),
    float(request.form['Valence']),
    float(request.form['key_A']),
    float(request.form['key_A#']),
    float( request.form['key_B']),
    float(request.form['key_C']),
    float(request.form['key_C#']),
    float(request.form['key_D']),
    float(request.form['key_D#']),
    float(request.form['key_E']),
    float(request.form['key_F']),
    float(request.form['key_F#']),
    float(request.form['key_G']),
    float(request.form['key_G#'])
    ]]
    return criteria

if __name__ == "__main__":
    app.run(debug=True)