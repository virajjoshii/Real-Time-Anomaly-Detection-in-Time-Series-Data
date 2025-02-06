from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd

def train_model(data):
    """Train the anomaly detection model."""
    scaler = StandardScaler()
    data['value'] = scaler.fit_transform(data[['value']])
    
    model = IsolationForest(n_estimators=100, contamination='auto')
    model.fit(data[['value']])
    return model, scaler

def predict(model, scaler, data):
    """Use the trained model to predict anomalies."""
    data['value'] = scaler.transform(data[['value']])
    return model.predict(data[['value']])

if __name__ == "__main__":
    data = pd.read_csv('processed_data.csv')
    model, scaler = train_model(data)
    predictions = predict(model, scaler, data)
    data['anomaly'] = predictions
    data.to_csv('predictions.csv', index=False)
