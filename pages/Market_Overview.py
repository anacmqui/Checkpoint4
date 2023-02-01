import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import geopandas as gpd

dash.register_page(__name__, path='/')

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world1 = world[world['continent']!= 'Antarctica'] 
df_countries = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_country2.csv')

def world_wine(df = df_countries):
  return px.choropleth_mapbox(df_countries, geojson=world1, locations='country', color='count',
                           animation_frame="year",
                           color_continuous_scale="Burg",
                           range_color=(1, 2000),
                           mapbox_style="carto-positron",
                           featureidkey="properties.name",
                            zoom=2, 
                          labels={'count':'Nb of wines produced'}, height=800)

layout  =  html.Div(children=[
            dbc.Row(children = [
                    html.H1(
                     children = ['Which countries produce more wine?'], style={'textAlign':'center', "padding": "2rem 1rem"}
                     ), ]),
            dbc.Row([dcc.Graph(figure=world_wine()),])
            ])


