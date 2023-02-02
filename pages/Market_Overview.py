import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dash.register_page(__name__, path='/')

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world1 = world[world['continent']!= 'Antarctica'] 
df_countries = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_country2.csv')

df_total = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_total.csv')

best_scores = df_total.sort_values(by='points', ascending=False).head(19)
#best_scores[['country' , 'title', 'variety', 'year','points', 'price']]

df_grape = df_total.groupby(['variety']).agg({'points' : 'mean', 'description':'count'}).reset_index().sort_values(by='description', ascending=False)
df_grape_top = df_grape[df_grape['description']>100].sort_values(by='points', ascending=False)
df_grape_top_15 = df_grape_top.head(15).reset_index()
df_grape_top_15 = df_grape_top_15.rename(columns={'description':'count'}) 

df_grape_n = df_grape.sort_values(by='points', ascending=False).head(15)
df_grape_n = df_grape_n.rename(columns={'description':'count'}) 



def world_wine(df = df_countries):
  return px.choropleth_mapbox(df_countries, geojson=world1, locations='country', color='count',
                           animation_frame="year",
                           color_continuous_scale="Burg",
                           range_color=(1, 2000),
                           mapbox_style="carto-positron",
                           featureidkey="properties.name",
                            zoom=2, 
                          labels={'count':'Nb of wines produced'}, height=800)

def points_dist(df=df_total):
    fig0 = make_subplots(rows = 1, cols = 1, shared_xaxes=True)
    fig0.add_traces([go.Box(x=df_total['points'], line = {"color":'#8B1A1A'})])
    return fig0

def best_score(df=best_scores):
    fig1 = px.bar(best_scores, x='country', hover_data=["title", 'variety', 'year', 'price'])
    fig1.update_traces(marker_color='#8B1A1A', opacity=0.6)
    return fig1

def best_grape15(df=df_grape_top_15):
    fig = px.bar(df_grape_top_15, x='variety', y='points',hover_data=['count'])
    fig.update_layout(yaxis=dict(range=[89,95.5]))
    fig.update_xaxes(tickangle=45)
    fig.update_traces(marker_color='#8B1A1A', opacity=0.6)
    return fig

def best_grapen(df=df_grape_n):
    fig2 = px.bar(df_grape_n, x='variety', y='points',hover_data=['count'])
    fig2.update_layout(yaxis=dict(range=[89,95.5]))
    fig2.update_xaxes(tickangle=45)
    fig2.update_traces(marker_color='#8B1A1A', opacity=0.6)
    return fig2

layout  =  html.Div(children=[
            dbc.Row(children = [
                    html.H1(
                     children = ['Which countries produce more wine?'], style={'textAlign':'center', "padding": "2rem 1rem"}
                     ), ]),
            dbc.Row([dcc.Graph(figure=world_wine()),]),
            dbc.Row([
                dbc.Col([
                    html.H1('What is the distribution of the score?', style={'textAlign':'center', "padding": "2rem 1rem"}
                            ),
                     dcc.Graph(figure=points_dist()),
                     ], width=6),
                dbc.Col([html.H1('Where are the wines with 100 points?', style={'textAlign':'center', "padding": "2rem 1rem"}
                     ),
                     dcc.Graph(figure=best_score()), 
                     ], width=6),     
                    ]),

            dbc.Row([
                  dbc.Col([ 
                    dbc.Row([html.H1('What are the grapes with best score?', style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),]),
                     dbc.Row([dcc.Graph(figure=best_grapen())]), 
                  ], width= 6),
                  # dcc.Graph(figure=prevision_value()),
                 dbc.Col([ 
                    dbc.Row([html.H1('What are the top grapes with best score?', style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),]),
                     dbc.Row([dcc.Graph(figure=best_grape15())]),
                    ], width= 6),
                 ]),
              ])


