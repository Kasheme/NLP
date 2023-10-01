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
            dbc.Row(dbc.Col(html.Div("Select a topic:", style={'textAlign':'left', 'font-size': 24}) ) ),
            dbc.Row(dbc.Col(dcc.Dropdown([topic for topic in topic_word_df['topic'].unique()], id='topic_dropdown', style={'width':'50%'}) ) )
        ]
    ),
    html.Div(
        [
            html.Div(children=[], id='plot1')
        ]
    )

], style={'display': 'flex', 'flex-direction': 'row', 'width':'30%'}
)

"""
==================
Callback functions
"""

""" Callback function to return Topic Name"""
@callback(
    Output('plot1', 'children'),
    Input('topic_dropdown', 'value')
)
def get_words_bar_chart(topic):

    df = topic_word_df[topic_word_df['topic'] == topic].sort_values(by='score', ascending=False)

    sns.set_color_codes("pastel")
    bar_fig = sns.barplot(data=df, x='score', y='word', label='Word to Topic Similarity Score', color='b')
    plt.title("Top 50 Words in Topic Ordered by Topic Similarity Score")
    plt.rcParams['figure.figsize']= (6,15)

    return dcc.Graph(figure=bar_fig)

