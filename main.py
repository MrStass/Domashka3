# 1)
my_list = [200, 12, 23414, 3451, 1, 5]
for numbers in my_list:
    if numbers > 100:
        print(numbers)

#####################################################

# 2)
my_list = [200, 12, 23414, 3451, 1, 5]
my_results = []
for numbers in my_list:
    if numbers > 100:
        my_results.append(numbers)
print(my_results)

#####################################################

# 3)
my_list = [200, 12, 23414, 3451, 1, 5]
if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)
print(my_list)

#####################################################

# 4)

my_string = '0123456789'
result = []
for symb_1 in my_string:
	for symb_2 in my_string:
		result.append(int(symb_1+symb_2))
print(result)