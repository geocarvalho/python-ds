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
class Person:
    department = "School of Information"
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name("Christopher Brooks")
person.set_location("Ann Arbor, MI, USA")
"""print("{} live in {} and works in the department {}".format(
person.name, person.location, person.department
))"""

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
#for item in cheapest:   print(item)
##################### Lambda and List comprehensions #####################
my_function = lambda a, b, c: a + b
#print(my_function(1,2,3))
"""my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)"""
#or
my_list = [number for number in range(0, 1000) if number % 2 == 0]
#print(my_list)
############################ NumPy ############################
import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)
y = np.array([4, 5, 6])
m = np.array([[7, 8, 9], [10, 11, 12]])
#print(m.shape) #dimensions from array
n = np.arange(0, 30, 2)
n = n.reshape(3, 5)
o = np.linspace(0, 4, 9)
o.resize(3, 3)
p = np.ones([2, 3], int)
#print(np.ones((3, 2)))
#print(np.zeros((2, 3)))
#print(np.eye(3))
#print(np.diag(y))
#print(np.array([1, 2, 3] * 3))
#print(np.repeat([1, 2, 3], 3))
#print(np.vstack([p, 2*p]))
#print(np.hstack([p, 2*p]))
#print(x + y)
#print(x - y)
#print(x * y)
#print(x / y)
#print(x ** 2)
#print(x.dot(y))
z = np.array([y, y**2])
#print(len(z), z)
#print(z.shape)
#print(z.T, z.T.shape, z.dtype)
z = z.astype("f")
#print(z.dtype)

a = np.array([-4, -2, 1, 3, 5])
#print(a.sum(), a.max(), a.min(), a.mean(), a.std())
#print(a.argmax(), a.argmin())

s = np.arange(13)**2
r = np.arange(36)
r.resize((6, 6))
#print(r)
#print(r[2, 2])
#print(r[3, 3:6])
#print(r[:2, :-1])
#print(r[-1, ::2])
#r[r>30]=30
#print(r)
r2 = r[:3, :3]
r2[:] = 0
#print(r2)
#To avoid this, use `r.copy` to create a copy that will not affect the original array
r_copy = r.copy()
r_copy[:] = 10
#print(r_copy)
#print(r)

test = np.random.randint(0, 10, (4, 3))
print(test)
#for row in test:    print(row)
#for i in range(len(test)):  print(test[i])
#for i, row in enumerate(test):  print("row", i, "is", row)

test2 = test**2
print(test2)
#for i, j in zip(test, test2):   print(i, "+", j, "=", i+j)
################## class questions ########################
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
