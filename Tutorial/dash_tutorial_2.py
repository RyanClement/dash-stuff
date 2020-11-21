# -*- coding: utf-8 -*-
"""
Program:            Dash Tutorial #2
Tutorial Source:    dash.ploly.com/layout
Example Of:         Bar Graph with more color options than tutorial #1.
@author:            iProgram (RRCC)
Created:            Nov 2020

NOTES:              (1) Run application with 'python dash_tutorial_1.py'.
                    (2) Navigate to 'http://127.0.0.1:8050' in web browser.
"""

import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)

colors = {
    'background': 'black',
    'text': 'red'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = dhtml.Div(style={'backgroundColor': colors['background']}, children=[
    dhtml.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dhtml.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)