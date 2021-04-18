import pandas as pd
import plotly.graph_objs as go


def data_cleaning(year, offense='All offenses'):
    '''

    :param year: the year of the OJJDP data to wrangle
    :param offense: the offense commited
    :return: cleaned data frame
    '''
    df = pd.read_csv('data/'+str(year)+'.csv', error_bad_lines=False, encoding='ISO-8859-1',
                     skiprows=[0, 1])[0:31].drop(['Unnamed: 6'], axis=1)
    df.columns = df.columns.str.replace(' ', '_')  # replace space with an underscore for each column name
    df = df.set_index('Offenses')
    df.index.name = None
    df = df[df.columns].replace(',', '', regex=True)  # remove all commas from each column with numbers
    df = df.apply(pd.to_numeric)  # convert objects to float
    df.drop('All_races', axis=1, inplace=True)
    # val = df.loc[offense]
    return df


def get_figures(year, offense):
    graph_one = []
    # offense = 'Robbery'
    data_series = data_cleaning(year, offense=offense)

    graph_one_ds = data_series.loc[offense]
    # if offense != 'All offenses':
    #     data_series.drop(offense)

    graph_one_x = graph_one_ds.index
    graph_one_y = graph_one_ds.values

    graph_one.append(
        go.Bar(
            x=graph_one_x,
            y=graph_one_y,

        )
    )

    layout = dict(title='USA ' + str(year) + ' ' + str(offense) + ' data bar chart',
                  xaxis=dict(title='race'),
                  yaxis=dict(title='count'),
                  # , showline = True, mirror = True, ticks = 'outside'
                 )

    graph_two = []
    # graph_two_ds = data_series['White']
    # graph_two_white_x = graph_two_ds.index
    # graph_two_white_y = graph_two_white_x.values

    # print(data_series.columns)
    # data_series.drop('All_races', axis=1, inplace=True)
    for race in data_series.columns:
        x_val = data_series[race].index[1:]
        y_val = data_series[race].values
        graph_two.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='lines',
                name=race
            )
        )

    layout_two = dict(title='USA ' + str(year) + ' ' + str(offense) + ' data line chart',
                      xaxis=dict(autotick=False, dtick=1),
                      yaxis=dict(title='count'),
                      )
    # graph_two.append(
    #     go.Scatter(
    #         x=race_list,
    #     )
    # )

    figures = [
        dict(data=graph_one, layout=layout),
        dict(data=graph_two, layout=layout_two)
    ]
    # figures.append(dict(data=graph_one, layout=layout))
    # figures.append(dict(data=graph_one, layout=layout))

    return figures

# get_figures(2019, 'All offenses')