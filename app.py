# -*- coding: utf-8 -*-

# Ticker별 종가 추이를 확인하는 함수
# 날짜 입력, 관심 Ticker를 입력하여 종가 추이를 확인합니다.
# 반응형 그래프를 만들기 위해 Callback 함수를 정의합니다.

import pandas_datareader.data as web
import datetime
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# 시작일자를 입력합니다.
start = datetime.datetime(2020,1,1)
end = datetime.datetime.now()

# 관심 Ticker를 입력합니다.
ticker = 'AAPL'


# dashboard add을 실행합니다.
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Stock price Trend'),
    html.Div(children='''
    Input your Ticker!!
    etc)AAPL, TSLA, MSFT, GOOGL, FB
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])

# Callback함수를 정의합니다. (Input = 'input', Output = 'output_graph')
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

# 반응형 그래프를 위해 Update_value 함수를 정의합니다.
def update_value(input_data):
    df = web.DataReader(input_data, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)

    return dcc.Graph(
        id='price-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)