# _*_ coding: utf-8 _*_
# @Author: Aniruddha Pal
# @time: 26-11-2021 12:37
# @File: hypo.py
# @Software:PyCharm
import pandas as pd
# import numpy as np
from scipy.stats import ttest_ind
import re

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National',
          'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana',
          'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
          'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan',
          'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
          'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa',
          'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana',
          'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California',
          'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island',
          'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia',
          'ND': 'North Dakota', 'VA': 'Virginia'}


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    file = open('university_towns.txt', 'r')
    lines = file.readlines()
    file.close()
    new_lines = []
    state_str = ''
    region_str = ''
    for line in lines:
        if not re.match(r'^\s*$', line):
            new_lines.append(line)
    lines = new_lines.copy()

    for index, line in enumerate(lines):
        lines[index] = line.strip()
    df_result = pd.DataFrame(columns=('State', 'RegionName'))
    i = 0
    for line in lines:
        if '[edit]' in line:
            state_str = line.replace('[edit]', '')
        else:
            region_str = re.sub(r' \(.*', '', line)
            df_result.loc[i] = [state_str, region_str]
            i = i + 1

    return df_result

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    df_gdp = pd.read_excel('gdplev.xls', skiprows=220, usecols='E,G', header=None)
    df_gdp.columns = ['Quarter', 'GDP']
    for i in range(4, len(df_gdp)):
        if (df_gdp.loc[i - 4, 'GDP'] > df_gdp.loc[i - 3, 'GDP']) and (
                df_gdp.loc[i - 3, 'GDP'] > df_gdp.loc[i - 2, 'GDP']) and (
                df_gdp.loc[i - 2, 'GDP'] < df_gdp.loc[i - 1, 'GDP']) and (
                df_gdp.loc[i - 1, 'GDP'] < df_gdp.loc[i, 'GDP']):
            recession_start = i - 4
    result = df_gdp.loc[recession_start, 'Quarter']
    j = recession_start
    while True:
        if (df_gdp.loc[j - 1, 'GDP']) > (df_gdp.loc[j, 'GDP']):
            j = j - 1
        else:
            result = df_gdp.loc[j + 1, 'Quarter']
            break
    return result


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''
    df_gdp = pd.read_excel('gdplev.xls', skiprows=220, usecols='E,G', header=None)
    df_gdp.columns = ['Quarter', 'GDP']
    for i in range(4, len(df_gdp)):
        if (df_gdp.loc[i - 4, 'GDP'] > df_gdp.loc[i - 3, 'GDP']) and (
                df_gdp.loc[i - 3, 'GDP'] > df_gdp.loc[i - 2, 'GDP']) and (
                df_gdp.loc[i - 2, 'GDP'] < df_gdp.loc[i - 1, 'GDP']) and (
                df_gdp.loc[i - 1, 'GDP'] < df_gdp.loc[i, 'GDP']):
            recession_ends = i
    result = df_gdp.loc[recession_ends, 'Quarter']

    return result


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''
    df_gdp = pd.read_excel('gdplev.xls', skiprows=220, usecols='E,G', header=None)
    df_gdp.columns = ['Quarter', 'GDP']
    for i in range(4, len(df_gdp)):
        if (df_gdp.loc[i - 4, 'GDP'] > df_gdp.loc[i - 3, 'GDP']) and (
                df_gdp.loc[i - 3, 'GDP'] > df_gdp.loc[i - 2, 'GDP']) and (
                df_gdp.loc[i - 2, 'GDP'] < df_gdp.loc[i - 1, 'GDP']) and (
                df_gdp.loc[i - 1, 'GDP'] < df_gdp.loc[i, 'GDP']):
            recession_bottom = i - 2
            result = df_gdp.loc[recession_bottom, 'Quarter']
    return result

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''

    df = pd.read_csv('City_Zhvi_AllHomes.csv')
    #replacing the State column values with respective states dictionary values.
    df['State'] = df['State'].replace(states)
    #set State and RegionNames together as index
    df = df.set_index(['State', 'RegionName'])
    #considering columns from the year 2000 only, hence delete the rest
    for col in df.columns:
        if '199' in col:
            del df[col]
    #drop the unnecessary columns
    df = df.drop(['RegionID', 'Metro', 'CountyName', 'SizeRank'], axis=1)
    #convert the columns datatype as datetime with format YY-mm
    df.columns = pd.to_datetime(df.columns, format='%Y-%m')
    #Change the frequency of the time series columns from month-wise to quarter-wise mean
    df = df.resample('Q', axis=1).mean()
    #rename the columns as per quarter numbers in lowercase
    df = df.rename(columns=lambda x: str(x.to_period('Q')).lower())
    #return the cleaned dataframe
    return df


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    hdf = convert_housing_data_to_quarters()
    rec_start = get_recession_start()
    rec_bottom = get_recession_bottom()
    ul = get_list_of_university_towns()
    year_rec_start = int(rec_start[:4]) # year of recession start.i.e 2008
    qtr_rec_start = int(rec_start[-1]) # qtr of recession start,i.e 3
    ''' 1. price_ratio=quarter_before_recession/recession_bottom
        2. hdf.columns.get_loc(rec_start) returns the column index,i.e 34(starting index 0)
        3. we need qtr before recession,i.e 2008q2, hence -1.
        4. hdf.iloc[:, hdf.columns.get_loc(rec_start) - 1], returns all rows of column index 33
        5. .name, return the column name, i.e. 2008q2
        6. divide qtr before recession(2008q2) by recession bottom'''
    hdf['PriceRatio'] = hdf[hdf.iloc[:, hdf.columns.get_loc(rec_start) - 1].name].div(hdf[rec_bottom])
    # to_records convert dataframe into NumPy record array and then convert the same into list.
    ul_list = ul.to_records(index=False).tolist()
    # Retriving the matching rows of ul_list from hdf
    univ_town = hdf.loc[hdf.index.isin(ul_list)]
    # Retriving the non-matching rows of ul_list from hdf
    non_univ_town = hdf.loc[~hdf.index.isin(ul_list)]
    # Calculate the T-test for the means of two independent samples of scores.
    # This is a two-sided test for the null hypothesis that 2 independent samples have identical average (expected) values.
    # This test assumes that the populations have identical variances by default.
    # it returns the calculated t-statistic and a two-tailed p-value.
    # if p-value is <0.01, we reject "Hypothesis: University towns have their mean housing prices less effected by recessions."
    st, p = ttest_ind(univ_town['PriceRatio'], non_univ_town['PriceRatio'], nan_policy='omit')

    different = False
    if p < 0.01:
        different = True

    better = ""
    if non_univ_town['PriceRatio'].mean() < univ_town['PriceRatio'].mean():
        better = 'non-university town'
    else:
        better = 'university town'

    return (different, p, better)

# print(get_list_of_university_towns())
# print(get_recession_start())
# print(get_recession_end())
# print(get_recession_bottom())
# print(convert_housing_data_to_quarters())
print(run_ttest())