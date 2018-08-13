#!/usr/bin/python

from pandas import read_csv

## load dataset
df = read_csv('Donors_Data.csv')

##
## remove columns
##
## @axis, 0 for rows and 1 for columns
## @inplace, edit dataframe in place
##
df.drop(
    [
        'Row Id',
        'Row Id.',
        'zipconvert_2',
        'zipconvert_3',
        'zipconvert_4',
        'zipconvert_5'
    ],
    axis=1,
    inplace=True
)
