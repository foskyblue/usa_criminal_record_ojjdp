import pandas as pd
import plotly.graph_objs as go


def data_cleaning(year, offense='All offenses'):
    df = pd.read_csv('data/'+str(year)+'.csv', error_bad_lines=False, encoding='ISO-8859-1',
                     skiprows=[0, 1])[0:31].drop(['Unnamed: 6'], axis=1)
    df.columns = df.columns.str.replace(' ', '_')  # replace space with an underscore for each column name
    df = df.set_index('Offenses')
    df.index.name = None
    df = df[df.columns].replace(',', '', regex=True)  # remove all commas from each column with numbers
    df = df.apply(pd.to_numeric)  # convert objects to float
    df.drop('All_races', axis=1, inplace=True)
    val = df.loc[offense]
    return val


def get_figures(year, offense):
    graph = []
    # offense = 'Robbery'
    data_series = data_cleaning(year, offense=offense)

    # if offense != 'All offenses':
    #     data_series.drop(offense)

    race_list = data_series.index
    crime_val_list = data_series.values

    graph.append(
        go.Bar(
            x=race_list,
            y=crime_val_list,

        )
    )

    layout = dict(title='USA ' + str(year) + ' ' + str(offense) + ' data bar chart',
                  xaxis=dict(title='race'),
                  yaxis=dict(title='percentage'),
                  # , showline = True, mirror = True, ticks = 'outside'
                 )

    figures = [dict(data=graph, layout=layout)]

    return figures
