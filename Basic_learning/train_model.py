import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv('marks_data.csv')
X = df[['maths', 'science', 'history']]
y = df['passed']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')
print(" Model trained and saved as model.pkl")
