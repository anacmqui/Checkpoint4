import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
#import geopandas as gpd

dash.register_page(__name__, path='/')

layout  =  html.Div(children=[
            dbc.Row(children = [
            html.H1(
                children = ['Avg overnight stays'], style={'textAlign':'center', "padding": "2rem 1rem"}
                ), ]),
            ])


