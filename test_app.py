from flask import Flask, render_template, request
import pandas as pd
import pickle


app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':

        return(render_template('home_test.html'))

    else:

        fixed_acidity = request.form['fixed acidity']
        volatile_acidity = request.form['volatile acidity']
        citric_acid = request.form['citric acid']
        residual_sugar = request.form['residual sugar']
        chlorides = request.form['chlorides']
        free_sulfur_dioxide = request.form['free sulfur dioxide']
        total_sulfur_dioxide = request.form['total sulfur dioxide']
        pH = request.form['pH']
        sulphates = request.form['sulphates']
        alcohol = request.form['alcohol']

        datapoints = pd.DataFrame([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                                    free_sulfur_dioxide, total_sulfur_dioxide, pH, sulphates, alcohol]],
                                    columns=['fixed_acidity', 'volatile_acidity', 'citric_acid',
                                             'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
                                             'total_sulfur_dioxide', 'pH', 'sulphates', 'alcohol'], dtype=float)


        # Predicting the Wine Quality using the loaded model
        prediction = model.predict(datapoints)[0]
        if prediction == 'bad':
            prediction = "Low Wine Quality"
        else:
            prediction = "High Wine Quality"

        return render_template('home_test.html', result=test)


if __name__ == '__main__':
    app.run(debug=True)