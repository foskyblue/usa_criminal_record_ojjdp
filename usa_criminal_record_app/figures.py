import plotly.graph_objs as go
from data_wrangling_scripts.data_wrangling import data_cleaning


def get_figures(year, offense):
    graph_one = []
    data_series = data_cleaning(year, offense=offense)

    graph_one_ds = data_series.loc[offense]

    graph_one_x = graph_one_ds.index
    graph_one_y = graph_one_ds.values

    graph_one.append(
        go.Bar(
            x=graph_one_x,
            y=graph_one_y,

        )
    )
    layout_one = dict(title='USA ' + str(year) + ' data bar chart',
                      xaxis=dict(title='race'),
                      yaxis=dict(title='offence count'),
                 )

    graph_two = []
    for race in data_series.columns:

        # get a list of tuples with the first element as the index and the second element as value
        x_tup = list(data_series[race].items())

        # sort each tuple by the values in an increasing order
        x_tup.sort(key=lambda val: val[1])

        # get a list of all elements in first index except 'All_offenses'
        x_val = [seq[0] for seq in x_tup][:-1]
        # get a list of all elements in second index except value for 'All_offenses'
        y_val = [seq[1] for seq in x_tup][:-1]

        graph_two.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='lines',
                name=race
            )
        )
    layout_two = dict(title='USA ' + str(year) + ' ' + str(offense) + ' entire data line chart',
                      xaxis=dict(autotick=False),
                      yaxis=dict(title='offence count'),
                      )
    graph_three = [
        go.Pie(
            labels=graph_one_x,
            values=graph_one_y,

        )
    ]
    layout_three = dict(title='USA ' + str(year) + ' data Pie chart')

    graph_four = []
    x_val = []
    y_val = []
    for crime in data_series.index:
        x_val.append(sum(data_series.loc[crime].values))
        y_val.append(crime)
    graph_four.append(
        go.Bar(
            x=x_val,
            y=y_val,
            orientation='h',
            width=0.9,
        )
    )

    layout_four = dict(title='USA ' + str(year) + ' data bar chart',
                       xaxis=dict(title='race'),
                       yaxis=dict(title='offence count'),
                       )




    figures = [
        dict(data=graph_two, layout=layout_two),
        dict(data=graph_one, layout=layout_one),
        dict(data=graph_three, layout=layout_three),
        dict(data=graph_four, layout=layout_four)
    ]
    return figures
