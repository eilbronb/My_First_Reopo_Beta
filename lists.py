my_list = [1,2,3,]
print(my_list)
print(my_list[0])

#Appending 

my_list.append(4)
print(my_list)

my_list.append('five')
print(my_list)

#Deleting 

del my_list[3]
print(my_list)

#Nested Lists

nested_list = []
nested_list.append(123)
nested_list.append(22)
nested_list.append('ntp')
nested_list.append('ssh')
print(nested_list)

my_list.append(nested_list)
print(my_list)
print(my_list[3])
print(my_list[4])
print(my_list[4][0])
print(my_list[3][1])
