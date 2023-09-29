import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# create the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

# create framework of the main app
app.layout = html.Div(
    [
        html.Div("US Presedential Speeches on Middle Eastern Conflict 2003-2021", style={'fontSize':40, 'textAlign':'center'}),
        html.Div("Topic Modelling and Sentiment Analysis", style={'fontSize':30, 'textAlign':'center'})
    ]
)

if __name__ == '__main__':
    app.run_server()