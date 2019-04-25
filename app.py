import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['P5', 'P2', 'Y500', 'Y250']

levels = go.Bar(
    x=sales,
    y=[3500, 6000, 8500, 7500],
    name='IBU',
    marker={'color':'red'}
)
alcohol = go.Bar(
    x=sales,
    y=[5.4, 7.1, 9.2, 4.3],
    name='ABV',
    marker={'color':'blue'}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Daily Sales'
)

sales_fig = go.Figure(data=sales_data, layout=sales_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('HCF'),
    dcc.Graph(
        id='hcf',
        figure=sales_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
