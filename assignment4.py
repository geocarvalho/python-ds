import pandas as pd
import numpy as np

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
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada',\
     'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', \
     'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', \
     'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', \
     'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', \
     'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', \
     'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', \
     'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', \
     'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', \
     'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', \
     'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', \
     'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', \
     'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', \
     'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', \
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

def main():
    data = get_list_of_university_towns()
    print(data)

if __name__ == "__main__":
    main()
