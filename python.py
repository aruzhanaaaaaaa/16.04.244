#функция,                                                  ооп
#у=f(x)
#def add(x,y):return(кайтару) x+y(xпараметр)              classA: def add (x,y):return x+y 



def add(x,y):return x+y
a=add(4,5)
print(a)




def add_to_list(x):
    list1=[1,2,3,4]
    list1.append(x)
    return list1
print(add_to_list(x))



def add(x):
    listt1=[ {
    "name":"Kanat",
    "last_name":"Erbolov",
    "Age":20},
    {"name":"Askar",
     "last_name":"Erzhanov",
     "Age":15},
    {"name":"Kairat",
     "last_name":"Zhandosov",
     "Age":45}
]
    listt1.append(x)
    return listt1

print(add({"name":"Aslan",
           "last_name":"Askarovich",
           "Age":"19"}))
