import pandas as pd
import numpy as np

"""
Merging Dataframes
"""

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
df['Date'] = ['December 1', 'January 1', 'mid-May']
df["Delivered"] = True
df['Feedback'] = ['Positive', None, 'Negative']
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
#print(adf)

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
#print(staff_df.head())
#print()
#print(student_df.head())

merge = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True) # merge everything
merge = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True) # merge without Nan
merge = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True) # merge left without Nan
merge = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True) # merge right without Nan

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
merge = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

#print(merge)

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
merge = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
#print(staff_df)
#print(student_df)
merge = pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
#print(merge)
# Class question
# answer = pd.merge(products, invoices, left_index=True, right_on="Product ID")
"""
Idiomatic Pandas: Making Code Pandorable
"""
df = pd.read_csv('census.csv')
df1 = df.copy()
df1 = (df1.where(df1["SUMLEV"] == 50) # The pandorable way
.dropna()
.set_index(["STNAME", "CTYNAME"])
.rename(columns={"ESTIMATESBASE2010": "Estimates Base 2010"}))
df2 = df.copy()
df2 = df[df["SUMLEV"]==50] # The classic way
df2.set_index(["STNAME", "CTYNAME"], inplace=True)
df2.rename(columns={"ESTIMATESBASE2010": "Estimates Base 2010"})
#print(df2)

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row["max"] = np.max(data) # use return row
    row["min"] = np.min(data) # use return row
    return pd.Series({"min": np.min(data), "max": np.max(data)}) # return the max and min for row in the dataframe that it's applied
    #return row

#print(df.apply(min_max, axis=1))

rows = ['POPESTIMATE2010',
            'POPESTIMATE2011',
            'POPESTIMATE2012',
            'POPESTIMATE2013',
            'POPESTIMATE2014',
            'POPESTIMATE2015']
#print(df.apply(lambda x: np.max(x[rows]), axis=1))

"""
Group by
"""
df3 = df.copy()
df3 = df3[df3["SUMLEV"] == 50]
for state in df3["STNAME"].unique():
    avg = np.average(df3.where(df3["STNAME"]==state).dropna()["CENSUS2010POP"])
    #print("%s: %s" % (state, str(avg)))

for group, frame in df3.groupby("STNAME"):
    avg = np.average(frame["CENSUS2010POP"])
    #print("%s: %s" % (group, str(avg)))

df4 = df.copy()
df4 = df4.set_index("STNAME")

def fun(item):
    if item[0]<"M":
        return 0
    if item[0]<"Q":
        return 1
    return 2

#for group, frame in df4.groupby(fun):
    #print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

df5 = df.copy()
df5 = df5[df5["SUMLEV"]==50]
df5.groupby("STNAME").agg({"CENSUS2010POP": np.average})
#print(type(df5.groupby(level=0)["POPESTIMATE2010", "POPESTIMATE2011"]))
#print(type(df5.groupby(level=0)["POPESTIMATE2010"]))
#print(df5.set_index("STNAME").groupby(level=0)["CENSUS2010POP"].agg({"avg": np.average, "sum": np.sum}))
#print(df5.set_index("STNAME").groupby(level=0)["POPESTIMATE2010", "POPESTIMATE2011"].agg({"avg": np.average, "sum": np.sum}))
#print(df5.set_index("STNAME").groupby(level=0)["POPESTIMATE2010", "POPESTIMATE2011"].agg({"POPESTIMATE2010": np.average, "POPESTIMATE2011": np.sum}))

"""
Scales
"""
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: "Grades"}, inplace=True)
#print(df)
#print(df["Grades"].astype("category").head())
grades = df["Grades"].astype("category", categories=["D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"], ordered=True)
#print(grades.head())
#print(grades>"C")

df6 = pd.read_csv('census.csv')
df6 = df6[df6['SUMLEV']==50]
df6 = df6.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
#print(pd.cut(df6['avg'],10))

"""
Pivot tables
"""
df = pd.read_csv("cars.csv")
#print(df.head())
#print(df.pivot_table(values="(kW)", index="YEAR", columns="Make", aggfunc=np.mean))
#print(df.pivot_table(values="(kW)", index="YEAR", columns="Make", aggfunc=[np.mean, np.min], margins=True))

"""
Date functionality in Pandas
"""
# Timestamp
#print(pd.Timestamp("9/1/2016 10:05AM"))

# Period
#print(pd.Period("1/2016"))
#print(pd.Period("3/5/2016"))

# DatetimeIndex
t1 = pd.Series(list("abc"), [pd.Timestamp("2016-09-01"), pd.Timestamp("2016-09-02"), pd.Timestamp("2016-09-03")])
#print(t1)
# PeriodIndex
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
#print(t2)
# Converting to Datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3.index = pd.to_datetime(ts3.index)
#print(ts3)
#print(pd.to_datetime('4.7.12', dayfirst=True))

# Timedeltas
#print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))
#print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))

# Working with dates in a DataFrame
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
#print(dates)
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
#print(df)
#print(df.index.weekday_name)
#print(df.diff())
#print(df.resample("M").mean())
#print(df["2017"])
#print(df["2016-12"])
print(df.asfreq('W', method='ffill'))
