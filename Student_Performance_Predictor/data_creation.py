import pandas as pd
import numpy as np
import random


# Generate synthetic dataset
np.random.seed(42)
num_students = 500

data = {
    "student_id": range(1, num_students + 1),
    "exam_1_marks": np.random.randint(40, 100, num_students),
    "exam_2_marks": np.random.randint(40, 100, num_students),
    "exam_3_marks": np.random.randint(40, 100, num_students),
    "exam_4_marks": np.random.randint(40, 100, num_students),
    "exam_5_marks": np.random.randint(40, 100, num_students),
    "exam_6_marks": np.random.randint(40, 100, num_students),
    "attendance_rate": np.random.uniform(50, 100, num_students),
    "activity_score": np.random.uniform(0, 1, num_students),
}

df = pd.DataFrame(data)
df["future_marks"] = (
    0.3 * df["exam_6_marks"]
    + 0.25 * df["exam_5_marks"]
    + 0.2 * df["exam_4_marks"]
    + 0.1 * df["attendance_rate"]
    + 0.15 * df["activity_score"] * 100
).round()

# Save the dataset
df.to_csv("student_performance.csv", index=False)
print("Dataset created and saved.")
