from flask import Flask, render_template,request
import pickle
import numpy as np


model = pickle.load(open('modelIshan.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

""" @app.route('/predict', methods=['POST'])
def predict_FoodName():
    Cost = np.double(request.form.get('Cost'))
    Calories = int(request.form.get('Calories'))
    Disease = request.form.get('Disease')

    result = model.predict(np.array([Cost,Calories,Disease])).reshape(-1,1)

    return str(result) """
@app.route('/predict', methods=['POST'])
def predict_FoodName():
    Cost = np.double(request.form.get('Cost'))
    Calories = int(request.form.get('Calories'))

    result = model.predict(np.array([Cost,Calories]).reshape(1, -1))

    return str(result)

if __name__ == '__main__':
    app.run(debug = True)


""" from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('modelIshan.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('file.html')

@app.route('/predict', methods=['POST'])
def predict_FoodName():
    Cost = request.form.get('Cost')
    Calories = request.form.get('Calories')
    Disease = request.form.get('Disease')

    if Disease:
        Disease = int(Disease)
    else:
        Disease = np.nan

    result = model.predict(np.array([Cost,Calories,Disease])).reshape(-1,1)

    return str(result)

if __name__ == '__main__':
    app.run(debug = True) """


#Vikesh Code
""" import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

import model 
# Create Flask app
app = Flask(__name__)

# Load the pickle model
def load_model():
    try:
        with open("modelIshan.pkl", "rb") as f:
            model = pickle.load(f)
        return True, model
    except FileNotFoundError:
        return False, "Model file not found"
    except Exception as e:
        return False, f"Error loading model: {str(e)}"

status, model = load_model()
if status:
    app.model = model
else:
    print(f"Error loading model: {status}")

# Define input validation function
def validate_input(input_data, NUM_FEATURES=None):
    if len(input_data) != NUM_FEATURES:
        return False
    for val in input_data:
        if not isinstance(val, (int, float)):
            return False
    return True

@app.route("/")
def Home():
    return render_template("file.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = [float(x) for x in request.form.values()]
    if not validate_input(input_data):
        return "Invalid input", 400
    features = [np.array(input_data)]
    prediction = model.predict(features)

    return render_template("index.html", prediction_text="Preferred Food is {}".format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True) """
