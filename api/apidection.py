import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def predict(new_data):
  
  data = pd.read_csv('network_traffic_data.csv')

  # Preprocess your data
  X = data.drop('label', axis=1)  # Features
  y = data['label']  # Labels (normal or zombie)
 
  # Train a Random Forest model
  model = RandomForestClassifier()
  model.fit(X, y)

  # Predict on new data
  predictions = model.predict(new_data)