import joblib
import pandas as pd
from flask import Flask,render_template, request, jsonify




# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Initialize Flask app
app = Flask(__name__)
#Starts with our index-page
@app.route('/')
def home():
    return render_template('index.html')
# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Required Fields
    required_fields = [
        'exam_1_marks', 
        'exam_2_marks', 
        'exam_3_marks', 
        'exam_4_marks', 
        'exam_5_marks', 
        'exam_6_marks', 
        'attendance_rate', 
        'activity_score'
    ]
    
    # Ensure all required fields are in the input data
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Extract the features from the JSON data
    features = [
        data['exam_1_marks'],
        data['exam_2_marks'],
        data['exam_3_marks'],
        data['exam_4_marks'],
        data['exam_5_marks'],
        data['exam_6_marks'],
        data['attendance_rate'],
        data['activity_score']
    ]

    # Convert the input data to a DataFrame (for compatibility with the model)
    input_data = pd.DataFrame([features], columns=[
        'exam_1_marks', 'exam_2_marks', 'exam_3_marks', 
        'exam_4_marks', 'exam_5_marks', 'exam_6_marks', 
        'attendance_rate', 'activity_score'
    ])

    # Predict the future marks
    prediction = model.predict(input_data)

    # Return the prediction as a JSON response
    return jsonify({"predicted_future_marks": prediction[0]})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
