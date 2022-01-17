from app.bmi_calculator import BMI_calculator
from flask import Flask, jsonify, request

app = Flask('__name__')

@app.route('/', methods = ['GET', 'POST'])
def get_input():
    """ A function to get request using flask, evaluate and return result."""

    packet = request.get_json(force = True)
    weight = packet['weight']
    height = packet['height']

    bmi = BMI_calculator(weight, height)

    return jsonify(bmi)
