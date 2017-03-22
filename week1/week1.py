import csv

##################### CSV ############################
with open("mpg.csv") as csvfile:
    mpg = list(csv.DictReader(csvfile))
"""
print(mpg[0])
print(len(mpg))
print(mpg[0].keys())
print(sum(float(d["cty"]) for d in mpg) / len(mpg))
print(sum(float(d["hwy"]) for d in mpg) / len(mpg))
"""
cylinders = set(d["cyl"] for d in mpg)
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
#print(CtyMpgByCyl)

vehicleclass = set(d["class"] for d in mpg) # what are the class types
HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
#print(HwyMpgByClass)
############################ Dates and Times ############################
import datetime as dt
import time as tm

#print(tm.time())
dtnow = dt.datetime.fromtimestamp(tm.time())
#print(dtnow)
#print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)  # get year, month, day, etc.from a datetime
delta = dt.timedelta(days=100) # create a timedelta of 100 days
#print(delta)
today = dt.date.today()
#print(today)
#print(today-delta)
#print(today > today-delta)
########################### Objects and map() ####################################
