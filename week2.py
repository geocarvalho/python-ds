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
print(all_countries.loc['Cricket'])
"""
The dataframe data structure
"""
