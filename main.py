import pandas as pd
data=pd.read_csv('hotels.csv')
#print(data)
one=input("enter state:")
two=input("Cost or Rating:")
three=input("operation:")
if one.lower()!='india'.lower():
    i=data[(data['State']!=one)].index
    data.drop(i,inplace=True)
#print(data)
c=[]
if two.lower()=='cost'.lower():
    s='Cost'
else:
    s='Ratings'
for i in data[s]:
    c.append(i)
#print(c)
if three=='cheapest':
    b=min(c)
    d=c.index(b)
elif three=='highest':
    b=max(c)
    d=c.index(b)
else:
    b=int(sum(c)/len(c))
    for i in range(1,10):
        if b in c:
            d=c.index(b)
            break
        elif b-i in c:
            d=c.index(b-i)
            break
        elif b+i in c:
            d=c.index(b+i)
            break
e=data.iloc[[d]]

co2=e['Hotel Code']
if two.lower()=='cost':
    co1=e['Cost']
else:
    co1=e['Ratings']
print("Hotel with",three,two,"in",one,"is",co2.to_string(index=False),"with",two,co1.to_string(index=False))