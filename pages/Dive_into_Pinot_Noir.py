import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np
from PIL import Image

dash.register_page(__name__, path='/pinot_noir')

df_pinot_noir_year = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_pinot_noir_year1.csv')


def pinot_noir_year(df=df_pinot_noir_year):
    fig = px.line(df_pinot_noir_year, x='year', y='points', hover_data=['count'])
    fig.update_layout(xaxis = dict(tickmode = 'linear'))
    fig.update_traces(line_color='#8B1A1A', opacity=0.6)
    return fig

layout = html.Div(children=[
            dbc.Row(children = [
                    html.H1(
                     children = ['Dive into Pinot Noir'], style={'textAlign':'center', "padding": "2rem 1rem", 'color':'#8B1A1A'}
                     ), 
                     ]),
            dbc.Row([
                dbc.Col([], width=3),
                dbc.Col([dbc.Alert("Produced in 24 Countries", color="danger", style={'textAlign':'center'})
                    ], width=3),
                dbc.Col([dbc.Alert("Avg score: 89.4", color="danger", style={'textAlign':'center'})
                    ], width=3),
                dbc.Col([], width=3),
                ]),
            dbc.Row(children = [
                    html.H2(
                     children = ['Pinot Noir throughout the years'], style={'textAlign':'center', "padding": "2rem 1rem"}
                     ), 
                     ]),
            dbc.Row([dcc.Graph(figure=pinot_noir_year()),]),
            dbc.Row(children = [
                    html.H2(
                     children = ['How to describe Pinot Noir?'], style={'textAlign':'center', "padding": "2rem 1rem"}
                     ), 
                     ]),
            dbc.Row([
                dbc.Col([ ], width=3),
                dbc.Col([html.Img(src='https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/wordmap_pinot.png',
                            style= {'width':'80%', 'align':'center'})
                        ]),
                dbc.Col([ ], width=3),
                    ]),
        ])