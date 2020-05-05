import pandas as pd
import numpy as np
"""
The series data structure
"""
animals = ["Tiger", "Bear", "Moose"]
animals = ['Tiger', 'Bear', None]

#print(pd.Series(animals))

numbers = [1, 2, 3]
numbers = [1, 2, None] #Nan and float numbers
#print(pd.Series(numbers))

#print(np.nan == None) #False
#print(np.nan == np.nan) # False
#print(np.isnan(np.nan)) # True

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
#print(s.index)
s = pd.Series(['Tiger', 'Bear', 'Moose'],
index=['India', 'America', 'Canada'])
#print(s)
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
#print(s)
"""
Querying a series
"""
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
#print(s.iloc[3]) # or s[3]
#print(s.loc["Golf"]) # or s["Golf"]

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
#print(s[0])
s = pd.Series([100.00, 120.00, 101.00, 3.00])
total = 0
for item in s:
    total+=item
#print(total) or
total = np.sum(s)
#print(total)
#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
#print(len(s))
#s+=2 #adds two to each item in s using broadcasting or

for label, value in s.iteritems():
    s.set_value(label, value+2)
#print(s.head())

s = pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label]= value+2
# or < time
s = pd.Series(np.random.randint(0,1000,10000))
s+=2

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
#print(s)

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
#print(original_sports, "\n"*2, all_countries)
#print(all_countries.loc['Cricket'])
"""
The dataframe data structure
"""
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
index=['Store 1', 'Store 1', 'Store 2'])
#print(df.head())
#print(type(df.loc["Store 2"]))
#print(df.loc["Store 1", "Cost"])
#print(df.T)
#print(df.T.loc["Cost"])
#print(df["Cost"]) #better, everything is float
#print(df.loc[:,["Name", "Cost"]])
#print(df.drop("Store 1"))
copy_df = df.copy()
copy_df = copy_df.drop("Store 1")
del copy_df["Name"]
#print(copy_df)
df["Location"] = None
#print(df)

"""
Dataframe indexing and loading
"""
costs = df["Cost"]
costs += 2
#print(costs)
#print(df)

#df = pd.read_csv("olympics.csv")
#print(df.head())
df = pd.read_csv("olympics.csv",
index_col = 0, skiprows=1)
#print(df.columns)
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]},
        inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]},
        inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]},
        inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]},
        inplace=True)
#print(df.head())

"""
Querying a DataFrame
"""
#print(df["Gold"] > 0)
only_gold = df.where(df["Gold"]>0)
#print(only_gold.head())
#print(only_gold["Gold"].count())
#print(df["Gold"].count())
only_gold = only_gold.dropna()
#print(only_gold.head())
only_gold = df[df["Gold"]>0]
#print(only_gold.head())
#print(len(df[(df["Gold"]>0) | (df["Gold.1"] > 0)]))
#print(df[(df["Gold.1"]>0) & (df["Gold"]==0)])

"""
Indexing DataFrames
"""
#print(df.head())
df["country"] = df.index
df = df.set_index("Gold")
#print(df.head())
df = df.reset_index()
#print(df.head())
df = pd.read_csv("census.csv")
#print(df.head())
#print(df["SUMLEV"].unique())
df = df[df["SUMLEV"]==50]
#print(df.head())
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
#print(df.head())
df = df.set_index(["STNAME", "CTYNAME"])
#print(df.head())
#print(df.loc['Michigan', 'Washtenaw County'])
#print(df.loc[ [('Michigan', 'Washtenaw County'),
#         ('Michigan', 'Wayne County')] ])

"""
Missing values
"""
df = pd.read_csv("log.csv")
#print(df)
df = df.set_index("time")
df = df.sort_index()
#print(df)
df = df.reset_index()
df = df.set_index(["time", "user"])
#print(df)
df = df.fillna(method="ffill")
print(df.head())
