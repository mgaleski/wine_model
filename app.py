import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle

# load model
model = pickle.load(open('model.pkl', 'rb'))

# app
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api', methods=['POST'])
def get_prediction():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = './model.pkl'
    model = model
    app.run(port=5000, debug=True)