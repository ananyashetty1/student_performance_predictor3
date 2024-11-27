import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error



#Load dataset
data = pd.read_csv("student_performance.csv")

#Marks and target
X = data[[
    "exam_1_marks",
    "exam_2_marks",
    "exam_3_marks",
    "exam_4_marks",
    "exam_5_marks",
    "exam_6_marks",
    "attendance_rate",
    "activity_score",
]]
y = data["future_marks"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_predict = model.predict(X_test)
mse = mean_squared_error(y_test, y_predict)
print(f"Mean Squared Error: {mse}")

# Save the model
joblib.dump(model, "student_performance_model.pkl")
print("Model saved.")
