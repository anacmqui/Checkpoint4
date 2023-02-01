import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

dash.register_page(__name__, path='/pinot_noir')

layout = [html.H1(children='Where are tourists coming from?',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),]