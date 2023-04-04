def merge_lists_to_dict(list_1, list_2):
    return dict(zip(list_1, list_2))


cars = ['BMW', 'Porsche', 'Range Rover']
prices = [95800, 110500, 105100]

print(merge_lists_to_dict(list_2=prices, list_1=cars))

names = ['Тим', 'Егорчик', 'Ванечка']
ages = [42, 9, 8]

print(merge_lists_to_dict(names, list_2=ages))

# SyntaxError: positional argument follows keyword argument
# print(merge_lists_to_dict(list1=names, ages))
