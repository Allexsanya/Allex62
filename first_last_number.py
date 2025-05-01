first_list = [5, 15, 25, 105]

if len(first_list) > 1:
    second_list = [first_list[-1]] + first_list[:-1]
else:
    second_list = first_list

print(second_list)
