import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

dash.register_page(__name__, path='/pinot_noir')

layout = html.Div(children=[
            dbc.Row(children = [
                    html.H1(
                     children = ['Dive into Pinot Noir'], style={'textAlign':'center', "padding": "2rem 1rem"}
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
        ])