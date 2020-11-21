# -*- coding: utf-8 -*-
"""
Program:            Dash Tutorial #1
Tutorial Source:    dash.ploly.com/layout
Example Of:         Bar Chart
@author:            iProgram (RRCC)
Created:            Nov 2020

NOTES:              (1) Run application with 'python dash_tutorial_1.py'.
                    (2) Navigate to 'http://127.0.0.1:8050' in web browser.
                    Test!
"""

import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)

# Assume you have a "long-form" data frame.
# See https://plotly.com/python/px-arguments/ for more information.
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = dhtml.Div(children=[
    dhtml.H1(children='Hello Dash'),

    dhtml.Div(children='''
              Dash: A web application framework for Python.
              '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)