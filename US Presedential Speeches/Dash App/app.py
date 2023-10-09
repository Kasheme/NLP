import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd


# create the app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.VAPOR])

# create framework of the main app
app.layout = html.Div(
    [
        html.Div("U.S. Presedential Speeches on Middle Eastern Conflict 2003-2021", style={'fontSize':40, 'textAlign':'center'}),
        html.Div("Topic Modelling Analysis", style={'fontSize':30, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name'] + " | ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run_server()
