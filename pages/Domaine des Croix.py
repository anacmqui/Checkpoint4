import dash
from dash import html, dcc, callback, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import datetime as dt

dash.register_page(__name__, path='/best_price', suppress_callback_exceptions=True)

df_domaine = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_domaine.csv')
df_domaine = df_domaine[['title', 'country', 'province', 'region_1', 'variety', 'points' , 'year']]
df_pinot_chard = pd.read_csv('https://raw.githubusercontent.com/anacmqui/Checkpoint5/main/df_pinot_chard.csv')


dropdown_fig_wine = df_domaine['title'].unique()
dropdown_fig_list_country = df_pinot_chard['country'].unique()
dropdown_fig_list_prov = df_pinot_chard['province'].unique()
dropdown_fig_list_reg = df_pinot_chard['region_1'].unique()
dropdown_fig_list_varie = df_pinot_chard['variety'].unique()

def competitors_year(df=df_pinot_chard):
    fig = px.scatter(df, x='year', y='price', color='winery', hover_data=['points'])
    fig.update_layout(xaxis = dict(tickmode = 'linear'))
    fig.update_traces(marker_size=12)
    return fig

layout = dbc.Container([
            html.H1(children='Domaine des Croix',
                        style={'textAlign':'center', "padding": "2rem 1rem", 'color':'#8B1A1A'}
                        ),
            #dcc.Dropdown(options = dropdown_fig_wine, value = '1', id = 'wines-dropdown', 
             #                       placeholder = 'Select a wine to analyse',  style={'width':'60%'}),
            html.Label(['Wines list'],
                        style={'font-weight': 'bold'}),
            html.P(),
            wine_table := dash_table.DataTable(
                                columns=[
                                        {'name': 'Title', 'id': 'title', 'type': 'text'},
                                        {'name': 'Country', 'id': 'country', 'type': 'text'},
                                        {'name': 'Province', 'id': 'province', 'type': 'text'},
                                        {'name': 'Region', 'id': 'region_1', 'type': 'text'},
                                        {'name': 'Grape', 'id': 'variety', 'type': 'text'},
                                        {'name': 'Score', 'id': 'points', 'type': 'numeric'},
                                        {'name': 'Year', 'id': 'year', 'type': 'numeric'},
                                                ],
                                data=df_domaine.to_dict('records'),
                                filter_action='native',
                                page_size=10,
                                style_data={
                                'width': 'auto',#'minWidth': '150px', 'maxWidth': '150px', 
                                'height': 'auto',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',},
                                style_cell_conditional=[ {
                                        'if': {'column_id': c},
                                        'textAlign': 'left'
                                         } for c in ['title']
                                         ],
                                #style_as_list_view=True,
                                #style_cell={'padding': '5px'}
                                ),         
            html.P(),
            html.H2(children='Find the best price for your wine',
                        style={'textAlign':'center', "padding": "2rem 1rem", 'color':'#8B1A1A'}
                        ),
            dbc.Row([
                 dbc.Col([    
                    html.Label(['Select a country:'],
                    style={'font-weight': 'bold'}),
                    html.P(),   
                     dcc.Dropdown(options = dropdown_fig_list_country, value = '1', id = 'countries-dropdown', placeholder = 'Select a country'),  
                        ], width=3),
                    dbc.Col([   
                    html.Label(['Select a province:'],
                    style={'font-weight': 'bold'}),
                    html.P(),     
                     dcc.Dropdown(options = dropdown_fig_list_prov, value = '1', id = 'province-dropdown', placeholder = 'Select a province'),  
                        ], width=3),
                    dbc.Col([  
                    html.Label(['Select a region:'],
                    style={'font-weight': 'bold'}),
                    html.P(),      
                    dcc.Dropdown(options = dropdown_fig_list_reg, value = '1', id = 'region-dropdown', placeholder = 'Select a region'),  
                        ], width=3),
                    ]),
             dbc.Row([
                 dbc.Col([ ], width=3, style = {'height':'50px'}),
                    ]),       
            dbc.Row([
                 dbc.Col([   
                    html.Label(['Select a type of grape:'],
                    style={'font-weight': 'bold'}),
                    html.P(),     
                    dbc.RadioItems(
                          options=[{"label": "Pinot Noir", "value": 'Pinot Noir'},
                                    {"label": "Chardonnay", "value": 'Chardonnay'},
                                  ],
                          value='Pinot Noir',
                          id="radioitems-input",
                            ),  
                        ], width=3),
                    ]),
            dbc.Row([
                 dbc.Col([ ], width=3, style = {'height':'50px'}),
                    ]), 
            dbc.Row([
                 html.Label(['Select a year:'],
                    style={'font-weight': 'bold'}),
                html.P(),
                dcc.RangeSlider(
                             id='my-range-slider', # any name you'd like to give it
                            marks={2002: '2002',2003: '2003',2004: '2004',2005: '2005',2006: '2006',2007: '2007', 2008: '2008', 2009: '2009', 2010: '2010',
                                2011: '2011',2012: '2012',2013: '2013', 2014: '2014', 2015: '2015', 2016: '2016', 2017: '2017', 2018: '2018', 2019: '2019',
                                2020: '2020',2021: '2021', 2022: '2022',
                                 },
                            step=1,                # number of steps between values
                            min=2002,
                            max=2022,
                            value=[2002,2022],     # default value initially chosen
                             dots=True,             # True, False - insert dots, only when step>1
                             allowCross=True,      # True,False - Manage handle crossover
                             disabled=False,        # True,False - disable handle
                             pushable=0,            # any number, or True with multiple handles
                            updatemode='mouseup',  # 'mouseup', 'drag' - update value method
                              included=True,         # True, False - highlight handle
                            vertical=False,        # True, False - vertical, horizontal slider
                             verticalHeight=900,    # hight of slider (pixels) when vertical=True
                             className='None',
                             tooltip={'always_visible':False,  # show current slider values
                                         'placement':'bottom'},
                                 ),
                    ]), 
            dbc.Row([
                 dbc.Col([ ], width=3, style = {'height':'50px'}),
                    ]), 
            dbc.Row([
                 dcc.Graph(figure=competitors_year(), id='line-graph')
                    ]),
            ])


@callback(
    Output(component_id = 'line-graph', component_property = 'figure'),
    Input(component_id = 'countries-dropdown', component_property = 'value'),
    Input(component_id = 'province-dropdown', component_property = 'value'),
    Input(component_id = 'region-dropdown', component_property = 'value'),
    Input(component_id = 'radioitems-input', component_property = 'value'),
    Input(component_id = 'my-range-slider', component_property = 'value'),
)

def update_line_graph(country, prov, reg, grape, year):
    dff = df_pinot_chard.copy()
    dff = dff[(dff['country']==country) &(dff['province']==prov) & (dff['region_1']==reg) 
                & (dff['variety']==grape) & (dff['year']>=year[0]) &(dff['year']<=year[1])]
    return competitors_year(dff)
