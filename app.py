import pandas as pd
import json
from dash import Dash, dcc, html, dash_table

from pprint import pprint

data = (
    pd.read_csv("avocado.csv")
    .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)


basic_stats = None
input_file = 'data/data.json'


def load_basic_stats(input_file):
    with open(input_file, 'r') as json_file:
        try:
            stats = json.load(json_file)
        except json.JSONDecodeError:
            print("Error decoding")
    return stats


stats = load_basic_stats(input_file)

# Extract the basic_stats dictionary
basic_stats_dict = stats['basic_stats']

# Convert the basic_stats_dict into a list containing a single dictionary
basic_stats_list = [basic_stats_dict]
months_list = stats['months_too_few_places_visited']

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children = [html.H1(children="File Statistics"),
        html.H2(children='Basic Statistics'),
        dash_table.DataTable(
            id='basic_stats_table',
            columns=[
                {"name": "Number of Years of History", "id": "num_of_years"},
                {"name": "Number of Months of History", "id": "num_of_months"},
                {"name": "Number of Empty Files of History", "id": "num_empty_files"},
                {"name": "Number of Empty Data Files of History", "id": "num_empty_data_files"}
            ],
            data=basic_stats_list,
            page_size=10,
            style_cell={'textAlign': 'center', 'font-family': 'Times New Roman'}
        )]
        ),
        html.H2(children='Months with Too Few Places Visited'),
        html.Ul([html.Li(month) for month in months_list])
        
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
