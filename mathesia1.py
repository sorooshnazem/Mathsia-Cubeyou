import csv
import operator

def gender(data):
    return 'Female' if data[7]=='1' else 'Male'

def states(data):
    st=data[11:63]
    return str(st.index('1')+12)

def race(data):
    st=data[63:67]
    return str(st.index('1')+64)

filepath='/Dataset-CUBE/data.txt'
with open(filepath.rstrip(),'r') as input_data:
    data= [num for num in input_data.readlines()]

data=[x for x in data if not(x[11:63].isspace())]
data=[x for x in data if not(x[63:67].isspace())]

layoutpath = '/Dataset-CUBE/layout.txt'
with open(layoutpath.rstrip(),'r') as input_data:
    layout= [num.split() for num in input_data.readlines()[4:]]

d={}
for i in range(0,len(layout)):
    d[layout[i][3]] = layout[i][2]

users=[]
for i in range(0,len(data)):
    users.append([int(data[i][0:7]),gender(data[i]),int(data[i][9:11]),d[states(data[i])],d[race(data[i])]])

users.sort(key=operator.itemgetter(0))

with open("users.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(users)