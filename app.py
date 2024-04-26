#from flask import Flask , request  , jsonify   #Jsonify is used to jsonify the response.
#user ke input ke liye request use kiya hai
#Form ke through jo data ata hai woh request se handle hoga.


from flask import Flask , request  , jsonify
import pickle
import numpy as np

model = pickle.load(open("modelIshan.pkl", "rb"))
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/predict', methods = ['POST'])
def predict():
    cost = float(request.form.get('Cost'))
    calories = float(request.form.get('Calories'))
    #Disease = request.form.get('Disease')

    input_query = np.array([[cost, calories]])

    result = model.predict(input_query)[0]

    return jsonify({'Food Name': result})

    # result ={'Cost':Cost,'Calories':Calories,'Not for people having:':Disease}

    #return jsonify(result)




if __name__ == '__main__':
    app.run(debug=True)