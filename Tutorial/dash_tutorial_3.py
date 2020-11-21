# -*- coding: utf-8 -*-
"""
Program:            Dash Tutorial #3
Tutorial Source:    dash.ploly.com/layout
Example Of:         Table
@author:            iProgram (RRCC)
Created:            Nov 2020

NOTES:              (1) Run application with 'python dash_tutorial_1.py'.
                    (2) Navigate to 'http://127.0.0.1:8050' in web browser.
"""

import dash
import dash_html_components as dhtml
import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv'
    )


def generate_table(dataframe, max_rows=10):
    """
    NumPy style docstring.

    Parameters
    ----------
    dataframe : TYPE
        DESCRIPTION.
    max_rows : TYPE, optional
        DESCRIPTION. The default is 10.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return dhtml.Table([
        dhtml.Thead(
            dhtml.Tr([dhtml.Th(col) for col in dataframe.columns])
        ),
        dhtml.Tbody([
            dhtml.Tr([
                dhtml.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dhtml.Div(children=[
    dhtml.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)