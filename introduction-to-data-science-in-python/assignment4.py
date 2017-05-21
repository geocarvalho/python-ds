import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    # Use this dictionary to map state names to two letter acronyms
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada',
              'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland',
              'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois',
              'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
              'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii',
              'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey',
              'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
              'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota',
              'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri',
              'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina',
              'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska',
              'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado',
              'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island',
              'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire',
              'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

    '''df = pd.read_table("/home/george/Git-projects/introduction-to-data-science-in-python/data/university_towns.txt", names=["Text"])
    df['State'] = df.loc[df['Text'].str.contains('[edit]', regex=False), 'Text'].str.extract(r'(.*?)\[edit\]', expand=False)
    df['RegionName'] = df.loc[df['State'].isnull(), 'Text'].str.extract(r'(.*?)\s*[\(\[]+.*[\n]*', expand=False)
    df['State'] = df['State'].ffill()
    df = df.dropna()'''
    state_lst, region_lst = [], []
    state, region = '', ''
    with open('/home/george/Git-projects/introduction-to-data-science-in-python/data/university_towns.txt') as file:
        for line in file:
            if '[ed' in line:
                state = line.split('[')[0].strip()
            elif '(' in line:
                region = line.split('(')[0].strip()
            else:
                region = line.strip()
            state_lst.append(state)
            region_lst.append(region)
    df = pd.DataFrame({
        'State': state_lst,
        'RegionName': region_lst
    })
    df = df[['State', 'RegionName']].replace("", np.nan).dropna()
    return df


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''
    df = pd.read_excel(
        '/home/george/Git-projects/introduction-to-data-science-in-python/data/gdplev.xls', skiprows=8, header=None)
    # 'For this assignment, only look at GDP data from the first quarter of 2000 onward'
    df = df.ix[212:, 4:6]
    df.columns = ['Quarterly', 'Current dollars', '2009 dollars']
    # Take the diference between values in 2009 column ('use the chained value
    # in 2009 dollars')
    df['Diff'] = df['2009 dollars'].diff().fillna(0)
    df.reset_index(drop=True, inplace=True)
    # Organize a column with binaries according to increase and decrease
    lst, past = [], 0
    for value in df['Diff']:
        if value == 0:
            lst.append(0)
        else:
            add = value - past
            if add > 0:  # increased
                lst.append(1)
            else:  # declines
                lst.append(0)
    df['Binary'] = lst
    # Take the decline period
    last, row = None, 0
    for value in df['Binary']:
        if value == 0 and last == 0:
            decline = df.ix[row - 1, 0]
            return decline
        row += 1
        last = value


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''
    df = pd.read_excel(
        '/home/george/Git-projects/introduction-to-data-science-in-python/data/gdplev.xls', skiprows=8, header=None)
    # 'For this assignment, only look at GDP data from the first quarter of 2000 onward'
    df = df.ix[212:, 4:6]
    df.columns = ['Quarterly', 'Current dollars', '2009 dollars']
    # Take the diference between values in 2009 column ('use the chained value
    # in 2009 dollars')
    df['Diff'] = df['2009 dollars'].diff().fillna(0)
    df.reset_index(drop=True, inplace=True)
    # Organize a column with binaries according to increase and decrease
    lst, past = [], 0
    for value in df['Diff']:
        if value == 0:
            lst.append(0)
        else:
            add = value - past
            if add > 0:  # increased
                lst.append(1)
            else:  # declines
                lst.append(0)
    df['Binary'] = lst
    # Take the decline period
    last, row = None, 0
    can = False
    for value in df['Binary']:
        # First when happened decline? After that search for recession end
        if value == 0 and last == 0:
            can = True
        if can:
            if value == 1 and last == 1:
                return df.ix[row, 0]
        row += 1
        last = value

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''
    df = pd.read_excel(
        '/home/george/Git-projects/introduction-to-data-science-in-python/data/gdplev.xls', skiprows=8, header=None)
    # 'For this assignment, only look at GDP data from the first quarter of 2000 onward'
    df = df.ix[212:, 4:6]
    df.columns = ['Quarterly', 'Current dollars', '2009 dollars']
    # Take the diference between values in 2009 column ('use the chained value
    # in 2009 dollars')
    df['Diff'] = df['2009 dollars'].diff().fillna(0)
    df.reset_index(drop=True, inplace=True)
    # Organize a column with binaries according to increase and decrease
    lst, past = [], 0
    for value in df['Diff']:
        if value == 0:
            lst.append(0)
        else:
            add = value - past
            if add > 0:  # increased
                lst.append(1)
            else:  # declines
                lst.append(0)
    df['Binary'] = lst
    # Take the decline period
    last, row = None, 0
    can = False
    for value in df['Binary']:
        # First when happened decline? After that search for recession end
        if value == 0 and last == 0:
            can = True
        if can:
            if value == 1 and last == 1:
                return df.ix[row-2, 0]
        row += 1
        last = value

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.'''

    # Use this dictionary to map state names to two letter acronyms
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada',
              'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland',
              'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois',
              'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
              'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii',
              'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey',
              'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
              'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota',
              'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri',
              'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina',
              'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska',
              'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado',
              'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island',
              'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire',
              'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

    df = pd.read_csv(
    '/home/george/Git-projects/introduction-to-data-science-in-python/data/City_Zhvi_AllHomes.csv')
    lst = list(df)
    for i in range(len(lst)):
        if lst[i] == '2000-01':
            index = i
    tdf = df[lst[index:]]
    tdf.columns = pd.to_datetime(tdf.columns)
    mdf = tdf.resample('Q', axis=1).mean().rename(
    columns=lambda x: '{:}q{:}'.format(x.year, x.quarter))
    mdf['RegionName'] = df['RegionName']
    mdf['State'] = df['State'].replace(states)
    mdf.set_index(['State', 'RegionName'], inplace=True)
    return mdf#.loc['Texas'].loc['Austin'].loc['2010q3']

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

    lst = list(hdf)
    for i in range(len(lst)):
        if lst[i] == rec_start:
            qrt_bfr_rec_start = lst[i-1]
    hdf['PriceRatio'] = hdf[qrt_bfr_rec_start].div(hdf[rec_bottom])
    tuple_list = [tuple(x) for x in ul.to_records(index=False)]
    university_towns = hdf.loc[tuple_list]
    non_university_towns = hdf.loc[~hdf.index.isin(tuple_list)]
    ttest = ttest_ind(
    non_university_towns['PriceRatio'],
    university_towns['PriceRatio'],
    nan_policy='omit')
    different = True if ttest[1]<0.01 else False
    p = ttest[1]
    better = "non-university town" if non_university_towns[
    'PriceRatio'].mean() < university_towns['PriceRatio'].mean() else \
    "university town"
    return (different,p,better)

def main():
    data = run_ttest()
    print(data)

if __name__ == "__main__":
    main()
