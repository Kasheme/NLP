import dash

dash.register_page(__name__, path='/')

from dash import html, dcc, callback, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


topic_word_df = pd.read_pickle(r"https://github.com/Kasheme/NLP/raw/develop/US%20Presedential%20Speeches/Dash%20App/datasets/topic_word_final_df.pkl")

layout = html.Div([
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("Select a topic:", style={'textAlign':'left', 'font-size': 20, 'margin-bottom':'2em'}) ) ),
            dbc.Row(dbc.Col(dcc.Dropdown([topic for topic in topic_word_df['topic'].unique()], id='topic_dropdown', value='0', style={'margin-bottom':'5em'}) ) ),
            dbc.Row(dbc.Col(html.Div(children=[], id='topic_name_selection') ) )
        ], style={'width':'20%', 'margin-left':'1.25em'}
    ),
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("Top 50 Words in Topic Ordered by Topic Similarity Score", style={'textAlign':'center', 'font-size': 20, 'margin-left':'1.5em'}) ) ),
            dbc.Row(dbc.Col(html.Div(children=[], id='plot1') ) )
        ], style={'width': '40%', 'margin-left':'1.25em'}
    )

], style={'display': 'flex', 'flex-direction': 'row'}
)

"""
==================
Callback functions
"""

""" Callback function to return Topic Name"""
@callback(
    Output('topic_name_selection', 'children'),
    Output('plot1', 'children'),
    Input('topic_dropdown', 'value')
)
def get_words_bar_chart(topic):

    df = topic_word_df[topic_word_df['topic'] == topic].sort_values(by='score', ascending=True)
    topic_name = str(df['topic name'].unique())
    
    sns.set_color_codes("pastel")
    bar_fig = px.bar(df, x='score', y='word', orientation='h', height=1000, width=600)
    bar_fig.update_layout(  
                            yaxis_title="", xaxis_title="", 
                            paper_bgcolor='rgba(0,100,0,0)', plot_bgcolor='rgba(0,0,0,0)'
                            #,bargap=0.25
                        )
    bar_fig.update_yaxes(color='white', tickfont=dict(size=10))
    bar_fig.update_xaxes(color='white', tickfont=dict(size=10))

    return topic_name, dcc.Graph(figure=bar_fig)

