ex_dict = {'name': 'ABCCCCC', 'code': 12345, 'test': 789}

list_key =  (ex_dict.keys())
list_value = (ex_dict.values())

#print (list_key)
#print(list_value)

GLO = 10000

list1 = ['name', 'code', 'address']
list2 = ['Tom', 45678, 'Hanoi']

ret_dict = {}

for ix in range(0,len(list1)):
    ret_dict[list1[ix]] = list2[ix]

print(ret_dict)