import pandas as pd
import numpy as np


def annotate_data(df):
    df['label'] = pd.Series(dtype='str')
    df['note'] = pd.Series(dtype='str')

    for i, row in df.iterrows():
            print(i)
            example = row['example']
            print(example)

            label = input("label: ")
            df.at[i, 'label'] = label

            note = input("note: ")
            df.at[i, 'note'] = note
    return df