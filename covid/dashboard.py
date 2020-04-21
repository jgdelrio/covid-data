import dash
import dash_core_components as dcc
import dash_html_components as html

from covid.data_manager import global_data


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def generate_table(df, max_rows: int=20):
    """Generates an HTML table from a pandas dataframe with the number of rows specified"""
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ])
    ])


app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(children='Graphical View',
                style={'textAlign': 'center', 'color': colors['text']}
                ),

        html.Div(children='Visualization examples',
                 style={'textAlign': 'center', 'color': colors['text']}),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        ),
        generate_table(global_data['Deaths']),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
