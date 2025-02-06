import pandas as pd

def load_data(url):
    """Load data from a web URL."""
    return pd.read_csv(url)

def preprocess_data(data):
    """Preprocess data by handling missing values, normalizing, etc."""
    data.fillna(method='ffill', inplace=True)  # Forward fill to handle missing values if any
    return data

if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/ambient_temperature_system_failure.csv'
    data = load_data(url)
    processed_data = preprocess_data(data)
    processed_data.to_csv('processed_data.csv', index=False)
