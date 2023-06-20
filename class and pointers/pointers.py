a=10
b=a
print(f'a= {a}')
print(f'b= {b}')
print(f'a= {id(a)}')
print(f'b= {id(b)}')
b=12
print(f'now a= {a}')
print(f'now b= {b}')
print(f'now a= {id(a)}')
print(f'now b= {id(b)}')

dict1={
    'value':11,
}
dict2=dict1
print(f'location of dict1 is: {id(dict1)}')
print(f'location of dict2 is: {id(dict2)}')
dict2['value']=45
print(f'location of dict1 is: {id(dict1)}')
print(f'location of dict2 is: {id(dict2)}')
print(f'location of dict1 is: {dict1}')
print(f'location of dict2 is: {dict2}')
print(dict1)
print(dict2)