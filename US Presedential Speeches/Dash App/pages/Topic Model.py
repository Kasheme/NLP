import dash

dash.register_page(__name__, path='/') 

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


layout = html.Div([
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("Select a topic:", style={'textAlign':'left', 'font-size': 20}) ) ),
            html.Hr(),
            dbc.Row(dbc.Col(dcc.Dropdown([topic for topic in topic_word_df['topic'].unique()],id='topic_dropdown', value=0, style={'margin-bottom':'2em'}) ) ),
            dbc.Row(dbc.Col(html.Div("Attributed Topic Name:", style={'textAlign':'left', 'font-size': 20, 'margin-bottom': '2em'}) ) ),
            dbc.Row(dbc.Col(html.Div(children=[], id='topic_name_selection', style={'font-size': 28, 'font-weight': 'bold'}) ) )
        ], style={'width':'20%', 'margin-left':'1.25em', 'margin-right':'1.25em'}
    ),
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("Top 50 Topic Words Ordered by Topic Similarity Score", style={'textAlign':'center', 'font-size': 20, 'margin-left':'1.25em'}) ) ),
            html.Hr(),
            dbc.Row(dbc.Col(html.Div(children=[], id='bar_plot') ) )
        ], style={'width': '40%', 'margin-left':'1.25em', 'margin-right':'1.25em'}
    ),
    html.Div(
        [
            #dbc.Container([

                dbc.Row(dbc.Col(html.Div("Top 15 Topic Speech Sentences by Similarity Score", style={'textAlign':'center', 'font-size': 18, 'margin-left':'1.25em'})  ) ),
                html.Hr(),
                dbc.Row(dbc.Col(html.Div(children=[], id='doc_table') ) )
            #])
        ], style={'width': '35%', 'margin-left':'1.25em'}
    )

    ], style={'display': 'flex', 'flex-direction': 'row'}
)
    # 

"""
==================
Callback functions
"""

""" Callback function to return topic name and topic words"""
@callback(
    Output('topic_name_selection', 'children'),
    Output('bar_plot', 'children'),
    Input('topic_dropdown', 'value')
    # ,allow_duplicate=True
    #,prevent_initial_call=True
)
def get_words_bar_chart(topic):

    df = topic_word_df[topic_word_df['topic'] == topic]
    if sum(df['score']) > 0:
        df = df.sort_values(by='score', ascending=True)
    else:
        df = df.sort_values(by='score', ascending=False)
    df['score'] = round(df['score'], 2)

    topic_name = df['topic name'].unique()[0]
    
    sns.set_color_codes("pastel")
    bar_fig = px.bar(df, x='score', y='word', orientation='h', height=1000, width=575, text='score')
    bar_fig.update_layout(  
                            yaxis_title="", xaxis_title="", 
                            paper_bgcolor='rgba(0,100,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            margin=dict(l=1, r=60, b=5, t=5)
                            #,bargap=0.25
                        )
    bar_fig.update_yaxes(color='white', tickfont=dict(size=14))
    bar_fig.update_xaxes(color='white', tickfont=dict(size=14))
    bar_fig.update_traces(textfont_size=36, textangle=0, textposition="outside",textfont_color='white')

    return topic_name, dcc.Graph(figure=bar_fig)

""" Callback function to return topic documents """
@callback(
    Output('doc_table', 'children'),
    Input('topic_dropdown', 'value')
)
def get_docs(topic):
    
    df = topic_doc_df[topic_doc_df['topic_num'] == topic].loc[:,['document', 'doc_score']]
    df['doc_score'] = round(df['doc_score'], 2)

    table_fig = go.Figure(data=[go.Table(
        header=dict(
            values=["Speech<br>Sentence", "Topic<br>Similarity<br>Score"],
            font=dict(size=14,color='whitesmoke'),
            align='left',
            fill_color='darkcyan'
        ),
        cells=dict(
            values=[df[i].tolist() for i in df.columns],
            line_color='whitesmoke',
            fill_color='paleturquoise',
            align='left')
        )
    ])
    table_fig.update_layout(height=600, margin=dict(l=5, r=5, b=5, t=5))

    return dcc.Graph(figure=table_fig)