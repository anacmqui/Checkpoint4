import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

dash.register_page(__name__, path='/best_price')

df_domaine = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_domaine.csv')
df_pinot_chard = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_pinot_chard.csv')

layout = [html.H1(children='Domaine des Croix',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),]