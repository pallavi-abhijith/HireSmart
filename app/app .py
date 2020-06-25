import flask
import dash

from components.Content import *
from components.Queries import *

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

#Initializers
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
HireSmart_colors = {'background': '#212121ff', 'text': '#ffab40'}
server = flask.Flask(__name__)
content = Content()
queries = Queries()
overall_scode = 0

languages=queries.run_custom_query("SELECT language FROM user1 ORDER BY language asc")
language_indicator=languages['language'].unique()
cities = queries.run_custom_query("SELECT city FROM user1 ORDER BY city asc")
city_indicator = cities['city'].unique()
#random_users = queries.run_custom_query("SELECT name FROM user1 limit 5")

@server.route('/api')
def index():
    return 'API fuctions:'

@server.route('/api/<users>')
def hello_name(name):
    return 'Hello %s!' % user

# Dash App Functions
app = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        server=server,
        routes_pathname_prefix='/'
        )

app.layout = html.Div(children=[
    #Header
    html.H1('HireSmart',style={'text-align': 'center', 'padding': '10px', 'background':HireSmart_colors['background'],'color':HireSmart_colors['text']}),

    html.Div([
        html.Div([
            dcc.Dropdown(
                id='input-1-state',
                placeholder='Enter a language',
                options=[{'label':i, 'value':i} for i in language_indicator],
            )
        ],style={'width':'20%', 'margin-right':'15px'}),
        html.Div([
            dcc.Dropdown(
                id='input-2-state',
                placeholder='Enter a major city',
                options=[{'label':i, 'value':i} for i in city_indicator],
            )
        ],style={'width': '20%', 'margin-right': '15px'}),
        html.Button('Submit', style={'background-color': '#a4c2f4'},  id='button'),
    ],style={'margin-right': '4%', 'margin-left': '2%', 'width': '100%', 'display':'flex'}),
    html.Hr(),
    html.Div(id="input-name-output"),

    # table with project information
    html.Div([
        html.Div([
            html.H6("User's Projects", style={'width': 'auto'}),
            html.Div(id='my-div')],
            style={'width': '70%', 'padding': '1%',  'background': '#d3d3d3', 'border-radius': '10px', 'margin-right': '2%'},
            ),
    ],style={'width': '100%', 'padding': '1%',  'border-radius': '10px', 'margin-right': '2%', 'display':'flex'}),
    
    html.Div([
        html.Div([
            dcc.Input(
                style={'width': '100%'},
                id='input-box',
                placeholder='Enter a user name to view more details',
                type='text',
            )],style={'width': '20%', 'margin-right': '15px'}),
        html.Button('Search', style={'background-color': '#a4c2f4'},  id='search'),
        html.Hr(),
        html.Div(id="input-name-output1"),
    ],style={'margin-right': '4%', 'margin-left': '2%', 'width': '100%', 'display':'flex'}),
])
@app.callback(
        Output('input-name-output', 'children'),
        [dash.dependencies.Input('button', 'n_clicks'),
            dash.dependencies.Input('input-1-state', 'value'),   # language
            dash.dependencies.Input('input-2-state', 'value')],  # city
       )

# if inputs such as button being clicked ouccrs, then this method will take in the parameters
# and use them to calculate the overall score, commit percentile, and byte percentile for the user
def update_output_div(button, language, city):
    #if(user_name==None):
    #    return "0.0%", "0.0%", "0.0%", "User does not currently exit in database"
    if(language == None):
        return "User does not select the language"
    elif(city == None):
        return "User does not select the city"
    else:
        print(language,city)
        df=queries.city_language(language, city)
        return content.generate_table(df)

@app.callback(
    Output('input-name-output1', 'children'),
    [dash.dependencies.Input('search','n_clicks'),
        dash.dependencies.Input('input-box','value')]
    )
def genearte_report(search, user_name):
    if(user_name==None):
        return "User name does not exist"
    else:
        df=queries.user(user_name)
        return content.generate_table(df)

if __name__ == '__main__':
    app.run_server(debug=True)


