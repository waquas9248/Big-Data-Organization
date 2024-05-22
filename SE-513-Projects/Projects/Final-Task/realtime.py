from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask

server = Flask(__name__)
app = Dash(__name__, server=server)

app.layout = html.Div([
    html.H1('Interactive line chart showing real-time crypto prices'),
    dcc.Graph(id="eth-graph"),
    dcc.Interval(
        id='eth-component',
        interval=5000, # in milliseconds
        n_intervals=0
    ),
    dcc.Graph(id="bit-graph"),
    dcc.Interval(
        id='bit-component',
        interval=5000, # in milliseconds
        n_intervals=0
    )
])

@app.callback(Output("eth-graph", "figure"), [Input("eth-component", 'n_intervals')])
def update_eth_graph(n):
    os.system('ls -al /mnt/Google/')
    df = pd.read_csv('/mnt/Google/crypto_info.csv', header='infer')
    df = df[df['Base'].str.contains('ETH')]
    fig = px.line(df, x=df['Time'], y=df['Amount'], color='Base', title="Ethereum Crypto Prices")
    return fig

@app.callback(Output("bit-graph", "figure"), [Input("bit-component", 'n_intervals')])
def update_bit_graph(n):
    os.system('ls -al /mnt/Google/')
    df = pd.read_csv('/mnt/Google/crypto_info.csv', header='infer')
    df = df[df['Base'].str.contains('BTC')]
    fig = px.line(df, x=df['Time'], y=df['Amount'], color='Base', title="Bitcoin Crypto Prices")
    return fig

if __name__=='__main__':
    app.run()
