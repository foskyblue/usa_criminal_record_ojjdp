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
    df = df.fillna(0)
    # val = df.loc[offense]
    # print(df)
    return df

