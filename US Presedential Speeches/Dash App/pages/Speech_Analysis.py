import dash

dash.register_page(__name__, order=2)

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
            dbc.Row(dbc.Col(html.Div("Speech-Topic Cosine Similarity Score Heatmap", style={'font-size':22, 'textAlign':'center'}) ) ),
            html.Hr(),
            dbc.Row(dbc.Col(html.Div(children=[], id='heatmap_plot') ) )
        
        ], style={'width':'90%', 'margin-left':'1.25em', 'margin-right':'1.25em'}
    ),
    html.Div(
        [

            dbc.Row(dbc.Col(dcc.RangeSlider(2003, 2021, 1,
                                       value=[2003, 2021],
                                       marks= {i: '{}'.format(i) for i in heatmap_pivot_df['Year'].unique().tolist()},
                                       id='year_slider', ) ) ),
            html.Br()
        ], style={'width':'81%', 'padding-left':'17%', 'padding-right':'2%'}
    ),
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("Average Topic Similarity Score Overtime", style={'font-size':22, 'textAlign':'center'}) ) ),
            html.Hr(),
            dbc.Row(dbc.Col(html.Div(children=[], id='line_plot'))),
            html.Hr(),
        ], style={'width':'90%', 'margin-left':'1.25em', 'margin-right':'1.25em'}
    )
])

""" heatmap plot callback function"""
@callback(
    Output('heatmap_plot', 'children'),
    Input('year_slider', 'value')
)
def get_heatmap(year):

    df = heatmap_pivot_df
    df = df[df['Year'] >= year[0]][df['Year'] <= year[1]].iloc[:,[0,1,2,3,4,5,6,7,8,9]]
    df = round(df, 2)

    heatmap_fig = px.imshow(df, text_auto=True, aspect='auto')
    heatmap_fig.update_layout(  
                            yaxis_title="", xaxis_title="", 
                            paper_bgcolor='rgba(0,100,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            margin=dict(l=1, r=60, b=5, t=5)
                        )
    heatmap_fig.update_yaxes(color='white', tickfont=dict(size=11))
    heatmap_fig.update_xaxes(color='white', tickfont=dict(size=11))


    return dcc.Graph(figure=heatmap_fig)

""" line plot callback function"""
@callback(
    Output('line_plot', 'children'),
    Input('year_slider', 'value')
)
def get_line_plot(year):

    dff = heatmap_pivot_df[heatmap_pivot_df['Year'] >= year[0]][heatmap_pivot_df['Year'] <= year[1]]
    dff = round(dff, 2)
    dff = pd.DataFrame(pd.pivot(dff, columns='Year').mean()).reset_index().rename(columns={0:'Average Score'})
    dff['Average Score'] = round(dff['Average Score'], 2)

    line_fig = px.line(dff, x='Year', y='Average Score', color='Topic Label', markers=True)
    line_fig.update_layout(  
                                yaxis_title="Average Similarity Score", xaxis_title="", 
                                paper_bgcolor='rgba(0,100,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                                margin=dict(l=1, r=60, b=5, t=5),
                                legend=dict(font=dict(color='white'))
                            )
    line_fig.update_yaxes(color='white', tickfont=dict(size=11))
    line_fig.update_xaxes(color='white', tickfont=dict(size=11))

    return dcc.Graph(figure=line_fig)