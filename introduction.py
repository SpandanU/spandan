a = [1,2,3,4]
b = [5,6,7,8]
print(a.count(2))
a.append(44)
print(a)

a=[1,2,3,4]
b=[5,6,7,8]

a.clear()
print(a)
b.insert(0,67)
print(b)

data= [
    {'name': 'asas', 'age':18, 'phone':1234576},
    {'name': 'Uwu','age':21, 'phone':8764321},
    {'name': 'twt', 'age':31 ,'phone':134532}
]
print(data[0]['name'])
print(data[1]['age'])
user={
    'name': 'spandan',
    'address':{
    "province":"nepal",
        'city':{
            "name":"kathmandu",
        },
   }
}
print(user['address']['city']['name'])

