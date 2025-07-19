from flask import Flask, request, jsonify  
import pickle  
import numpy as np  

# Load Trained Model  
with open('../models/flight_model.pkl', 'rb') as f:  
    model = pickle.load(f)  

app = Flask(__name__)  

@app.route('/predict', methods=['POST'])  
def predict():  
    try:  
        data = request.json  
        input_data = np.array([[data['Airline'], data['Source'], data['Destination'], data['Stops'], data['Duration']]])  
        prediction = model.predict(input_data)  
        return jsonify({'Predicted Price': float(prediction[0])})  
    except Exception as e:  
        return jsonify({'Error': str(e)})  

if __name__ == '__main__':  
    app.run(debug=True)
