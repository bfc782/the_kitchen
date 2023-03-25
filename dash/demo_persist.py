from dash import Dash, dcc, html, Input, Output

CITIES = ['Boston', 'London', 'Montreal']
NEIGHBORHOODS = {
    'Boston': ['Back Bay', 'Fenway', 'Jamaica Plain'],
    'London': ['Canary Wharf', 'Hackney', 'Kensington'],
    'Montreal': ['Le Plateau', 'Mile End', 'Rosemont']
}

app = Dash(__name__)

app.layout = html.Div([
    'Choose a city:',
    dcc.Dropdown(CITIES, 'Montreal', id='persisted-city', persistence=True),
    html.Br(),

    'correlated persistence - choose a neighborhood:',
    html.Div(dcc.Dropdown(id='neighborhood'), id='neighborhood-container'),
    html.Br(),
    html.Div(id='persisted-choices')
])


@app.callback(
    Output('neighborhood-container', 'children'),
    Input('persisted-city', 'value')
)
def set_neighborhood(city):
    neighborhoods = NEIGHBORHOODS[city]
    return dcc.Dropdown(neighborhoods, neighborhoods[0], id='neighborhood',
        persistence_type='session',
        persistence=city
    )


@app.callback(
    Output('persisted-choices', 'children'),
    Input('persisted-city', 'value'), Input('neighborhood', 'value')
)
def set_out(city, neighborhood):
    return f'You chose: {neighborhood}, {city}'


if __name__ == '__main__':
    app.run_server(debug=True)
