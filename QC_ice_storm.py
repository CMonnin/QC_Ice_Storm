
import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio

import pandas as pd
import numpy as np

# set the theme to a simialar seaborn theme
pio.templates.default = "simple_white"

#Creating a list of dictionaries for the dropdowns
regions = [
    {'label': 'Abitibi-Témiscamingue', 'value': 'Abitibi-Témiscamingue'},
    {'label': 'Bas-Saint-Laurent', 'value': 'Bas-Saint-Laurent'},
    {'label': 'Capitale-Nationale', 'value': 'Capitale-Nationale'},
    {'label': 'Centre-du-Québec', 'value': 'Centre-du-Québec'},
    {'label': 'Chaudière-Appalaches', 'value': 'Chaudière-Appalaches'},
    {'label': 'Côte-Nord', 'value': 'Côte-Nord'},
    {'label': 'Estrie', 'value': 'Estrie'},
    {'label': 'Gaspésie - Îles-de-la-Madeleine', 'value': 'Gaspésie - Îles-de-la-Madeleine'},
    {'label': 'Lanaudière', 'value': 'Lanaudière'},
    {'label': 'Laurentides', 'value': 'Laurentides'},
    {'label': 'Laval', 'value': 'Laval'},
    {'label': 'Mauricie', 'value': 'Mauricie'},
    {'label': 'Montréal', 'value': 'Montréal'},
    {'label': 'Montérégie', 'value': 'Montérégie'},
    {'label': 'Nord-du-Québec', 'value': 'Nord-du-Québec'},
    {'label': 'Outaouais', 'value': 'Outaouais'},
    {'label': 'Saguenay - Lac-Saint-Jean', 'value': 'Saguenay - Lac-Saint-Jean'},
    {'label': 'Across Québec', 'value': 'Across Québec'}]

# reading the curated data from github. Preparation of this data is found in the notebook.ipynb file on the github
df = pd.read_csv('https://raw.githubusercontent.com/CMonnin/QC_Ice_Storm/master/data/wrangled_data.csv')
df['time'] = pd.to_datetime(df['time'])
df = df.set_index(df['time'])
df = df.drop(columns='time')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX])
server = app.server
app.layout = dbc.Container([
    dbc.Row([
        html.H1('QC ice storm April 2023'),
        html.Div(children=[
            dcc.Link('Data scraped from Hyrdo Quebec power outages. ',href='https://poweroutages.hydroquebec.com/poweroutages/service-interruption-report/index.html',target='_blank'),
        ]),
        html.Div(children=[
            dcc.Link('Github link ',href='https://github.com/CMonnin/QC_Ice_Storm',target='_blank'),
        ]),
        html.Div(children=['Unfortunately the script only collected data from Sat Apr 8th onwards. ',
                           ]),
            ]),
    dbc.Row([
        dcc.Dropdown(options=regions,multi=True,value=['Montréal','Montérégie','Across Québec'],id='region_dropdown1'),
        dcc.Graph(id='custo_graph'),
        dcc.Dropdown(options=regions,multi=True,value=['Montréal','Montérégie','Across Québec'],id='region_dropdown2'),
        dcc.Graph(id='inter_graph'),
            ]),

])

@app.callback(
    Output('custo_graph', 'figure'),
    [Input('region_dropdown1', 'value')]
)
def update_graph(value):
    value_list = value
    fig = make_subplots(rows=1, cols=1, vertical_spacing=0.1)

    for i in value_list:
        # create a trace for each region
        trace = go.Scatter(x=df.index, y=df[f'{i} customers'], mode='lines', name=f'{i} customers')
        # add the trace to the figure
        fig.add_trace(trace, row=1, col=1)

    # set the titles and labels
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=1)

    # set the maximum number of x-axis ticks
    max_ticks = 15
    fig.update_xaxes(tickmode='linear', nticks=max_ticks, row=1, col=1)
    fig.update_layout(title='Customers without electricity')

    return fig


@app.callback(
    Output('inter_graph', 'figure'),
    [Input('region_dropdown2', 'value')]
)
def update_graph(value):

    value_list = value
    fig = make_subplots(rows=1, cols=1, vertical_spacing=0.1)

    for i in value_list:
        # create a trace for each region
        trace = go.Scatter(x=df.index, y=df[f'{i} interruptions'], mode='lines', name=f'{i} interruptions')
        # add the trace to the figure
        fig.add_trace(trace, row=1, col=1)

    # set the titles and labels
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=1)

    # set the maximum number of x-axis ticks
    max_ticks = 15
    fig.update_xaxes(tickmode='linear', nticks=max_ticks, row=1, col=1)
    fig.update_layout(title='Number of interruptions')

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
