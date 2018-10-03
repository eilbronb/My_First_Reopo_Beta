my_dict =  {}
my_dict['gigE0'] = 'Link to ISP'
print(my_dict)
print(my_dict['gigE0'])

my_list = [1,2,3,]
my_other_dict = {}
my_other_dict['thisisakey'] = 'thisisavalue'
print(my_other_dict)


#Nested Dictionaries
my_dict['nested_list'] = my_list
print(my_dict)
print(my_dict['nested_list'][0])

my_dict['nested_dict'] = my_other_dict
print(my_dict)
print(my_dict['nested_dict']['thisisakey'])
