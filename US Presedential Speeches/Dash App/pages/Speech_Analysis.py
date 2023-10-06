import dash

dash.register_page(__name__)

from dash import html, dcc, callback, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

topic_word_df = pd.read_pickle(r"https://github.com/Kasheme/NLP/raw/develop/US%20Presedential%20Speeches/Dash%20App/datasets/topic_word_df.pkl")
topic_doc_df = pd.read_pickle(r"https://github.com/Kasheme/NLP/raw/develop/US%20Presedential%20Speeches/Dash%20App/datasets/topic_doc_df.pkl")
heatmap_pivot_df = pd.read_pickle(r"https://github.com/Kasheme/NLP/raw/develop/US%20Presedential%20Speeches/Dash%20App/datasets/heatmap_pivot_df.pkl")

layout = html.Div([
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("Speech-Topic Cosine Similarity Score Heatmap", style={'font-size':20, 'textAlign':'left'}) ) ),
            dbc.Row(dbc.Col(html.Div(children=[], id='heatmap_plot') ) )
        
        ], style={'width':'90%', 'margin-left':'1.25em', 'margin-right':'1.25em'}
    )
])
#     ,html.Div(
#         [

#             dbc.Row(dbc.Col(dcc.Slider(2011, 2021, 1,
#                                        value=2021,
#                                        id='year_slider', )))
#         ], style={'width':'75%', 'margin-left':'1.25em', 'margin-right':'1.25em'}
#     )

# ])
# @callback(
#     Output('heatmap_plot', 'children'),
#     Input('year_slider', 'value')
# )
# def get_heatmap(year):

#     df = heatmap_pivot_df
#     df = df[df['Year'] <= year].iloc[:,[0,1,2,3,4,5,6,7,8,9]]

#     heatmap_fig = sns.heatmap(df, annot=True)
#     # heatmap_fig.set(xlabel=None)
#     # heatmap_fig.set(ylabel=None)

#     return dcc.Graph(heatmap_fig)