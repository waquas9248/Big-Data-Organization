from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import pickle
from flask import Flask

server = Flask(__name__)
app = Dash(__name__, server=server)
df = pd.read_csv('finalFrame.csv', header='infer')

counts=df.groupby('Clusters').count().reset_index()
counts.rename(columns={'Clusters': 'Clusters', 'Feature-1': 'Count', 'Feature-2': 'Count2'}, inplace=True)

app.layout = html.Div([
    html.H4('Interactive scatter plot with image  dataset'),
    dcc.Graph(id="feature-plot1"),
    dcc.Graph(id="feature-plot2"),
    dcc.Graph(id="cluster-count"),
])

@app.callback(Output("feature-plot1", "figure"), [Input("feature-plot1", 'value')])
def update_feature_plot1(value):
    fig = px.scatter(df, x=df['Clusters'], y=df['Feature-1'], color='Clusters', title="First Feature")
    return fig

@app.callback(Output("feature-plot2", "figure"), [Input("feature-plot2", 'value')])
def uupdate_feature_plot2(value):
    fig = px.scatter(df, x=df['Clusters'], y=df['Feature-2'], color='Clusters', title="Second Feature")
    return fig

@app.callback(Output("cluster-count", "figure"), [Input("cluster-count", 'value')])
def update_feature_plot1(value):
    fig = px.bar(counts, x=counts['Clusters'], y=counts['Count'], color='Clusters', title="Cluster Counts")
    return fig

if __name__=='__main__':
    app.run()
