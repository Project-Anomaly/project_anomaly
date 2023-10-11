import pandas as pd

def import_logs():
    '''
    imports .txt for use in later function
    '''
    pd.read_csv('anonymized-curriculum-access.txt', sep=' ', header=None)
    return df


def clean_df():
    '''
    imports and renames columns
    '''
    df = import_logs()
    df = df.rename(columns={0:'date',1:'time',2:'page',3:'user', 4:'cohort',5:'ip' })
    return df