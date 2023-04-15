
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


df = pd.read_csv('https://raw.githubusercontent.com/CMonnin/QC_Ice_Storm/master/data/wrangled_data.csv')
df['time'] = pd.to_datetime(df['time'])
df = df.set_index(df['time'])
df = df.drop(columns='time')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX])
# server = app.server
app.layout = dbc.Container([
    dcc.Dropdown(regions,multi=True,id='region_dropdown1'),
    dcc.Graph(id='custo_graph'),
    dcc.Dropdown(regions,multi=True,id='region_dropdown2'),
    dcc.Graph(id='inter_graph')
])




@app.callback(
    Output('custo_graph', 'fig'),
    [Input('region_dropdown1', 'values')]
)
def update_graph(values):
    # create two subplots
    fig = make_subplots(rows=1, cols=1, subplot_titles=("Customers without Electricity by Region"), vertical_spacing=0.1)

    # loop through the regions and plot the data
    # for region in values:
    fig.update_traces(px.scatter(df,x=df.index, y=df[f'{values} customers'], row=1, col=1, name=f'{values} customers'))

    # set the titles and labels
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=1)

    # set the maximum number of x-axis ticks
    max_ticks = 15
    # fig.update_xaxes(tickmode='linear', nticks=max_ticks, row=1, col=1)
    return fig


@app.callback(
    Output('inter_graph', 'figure'),
    [Input('region_dropdown2', 'values')]
)
def update_graph(values):
    # create two subplots
    fig = make_subplots(rows=1, cols=1, subplot_titles=("Interruptions by Region", "Customers without Electricity by Region"), shared_xaxes=True, vertical_spacing=0.1)

    # loop through the regions and plot the data
    for region in values:
        fig.update_traces(df,x=df.index, y=df[f'{region} interruptions'], row=1, col=1, name=f'{region} interruptions')


    # set the titles and labels
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=1)
  

    # set the maximum number of x-axis ticks
    max_ticks = 15
    fig.update_xaxes(tickmode='linear', nticks=max_ticks, row=1, col=1)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
