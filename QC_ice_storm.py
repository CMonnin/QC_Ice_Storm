
import dash
from dash import dcc, html, dash_table

import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output

from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio

import pandas as pd
import numpy as np

regions = ['Abitibi-Témiscamingue',
 'Bas-Saint-Laurent',
 'Capitale-Nationale',
 'Centre-du-Québec',
 'Chaudière-Appalaches',
 'Côte-Nord',
 'Estrie',
 'Gaspésie - Îles-de-la-Madeleine',
 'Lanaudière',
 'Laurentides',
 'Laval',
 'Mauricie',
 'Montréal',
 'Montérégie',
 'Nord-du-Québec',
 'Outaouais',
 'Saguenay - Lac-Saint-Jean',
 'Across Québec']


df = pd.read_csv('https://raw.githubusercontent.com/CMonnin/QC_Ice_Storm/master/data/wrangled_data.csv?token=GHSAT0AAAAAAB76XZNVLMVYJ3UER45CWGUKZBZ7NKA')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX])
server = app.server
app.layout = dbc.Container([
    dcc.Dropdown(regions,multi=True,id=region_dropdown1),
    dcc.Graph(),
    dcc.Dropdown(regions,multi=True,id=region_dropdown2),
])




@app.callback(
    Output('custo_graph', 'figure'),
    [Input('region_dropdown1', 'value')]
)
def update_graph(values):
    return figure

@app.callback(
    Output('custo_graph', 'figure'),
    [Input('region_dropdown1', 'value')]
)
def update_graph(values):
    return figure

if __name__ == "__main__":
    app.run_server(debug=True)
