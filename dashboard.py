import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

data = pd.read_csv('predictions.csv')

fig = px.line(data, x='timestamp', y='value', title='Temperature Anomaly Detection')
fig.add_scatter(x=data['timestamp'], y=data['value'], mode='markers', name='Anomalies',
                marker=dict(color='red', size=10, opacity=0.5), text='anomaly')

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
