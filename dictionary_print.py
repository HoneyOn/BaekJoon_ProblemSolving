my_dict= { 'first name': 'Kim', 'last name' : 'Hong Yeon', 'age' : 26, 'address' : 'Seoul, Korea'} 
my_dict['sex'] = 'Male'

print(my_dict)

for v,k in my_dict.items(): 
  print('{!r:15s} : {}'.format(v, k))
