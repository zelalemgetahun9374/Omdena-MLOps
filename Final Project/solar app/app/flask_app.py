import numpy as np
import joblib
from flask import Flask, jsonify, request

app = Flask('__name__')

@app.route('/', methods = ['GET', 'POST'])
def get_input():
    """
    A flask script to interface between ml model and the user request.
    """
    # load packets
    packet = request.get_json(force = True)
    # extract and transform the input values
    # input values are Temperature,CloudOpacity,DHI,DNI,Precipitation,Humidity,
    # Pressure,WindDirection,WindSpeed,Sunrise,Sunset,Month,Year,Day
    input_data = list(packet.values())
    # reshape the dataset
    data = np.array(input_data).reshape(1, 14)
    # load the model from disk
    filename = "app/model_gbr.pkl"
    loaded_model = joblib.load(filename)
    # generate prediction
    solar_radiation = loaded_model.predict(data)[0]
  
    return jsonify(packet, {"solar radiance":solar_radiation})
