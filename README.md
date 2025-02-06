# Real-Time Anomaly Detection in Time Series Data

## Project Overview
This project is designed to detect anomalies in real-time within time series data, using the Numenta Anomaly Benchmark (NAB) dataset. It leverages an Isolation Forest algorithm, implemented in Python with Scikit-Learn, and features a simulated streaming module using Apache Kafka to prepare the system for scalable, real-world applications. The results are visualized through an interactive monitoring dashboard built with Plotly and Dash.

## Features
- **Anomaly Detection**: Utilizes an Isolation Forest algorithm to detect anomalies in time series data effectively.
- **Data Processing**: Handles data preprocessing and transformation using Pandas and Numpy.
- **Real-Time Streaming**: Simulates real-time data processing with Apache Kafka.
- **Interactive Dashboard**: Offers a dynamic dashboard using Plotly and Dash for real-time visualization of detected anomalies.

## Built With
- Python
- Pandas, Numpy
- Scikit-Learn
- Apache Kafka
- Plotly, Dash

## Getting Started

### Prerequisites
Ensure you have Python 3.8+ and pip installed on your machine.

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/real-time-anomaly-detection.git
   ```
2. Navigate to the project directory:
   ```
   cd real-time-anomaly-detection
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage
Execute the scripts in the following order:
1. **Prepare the data**:
   ```
   python Data_prep.py
   ```
2. **Train the model and predict anomalies**:
   ```
   python model.py
   ```
3. **Launch the dashboard to visualize the results**:
   ```
   python dashboard.py
   ```


