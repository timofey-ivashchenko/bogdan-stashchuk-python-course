def merge_lists_to_dict(list_1, list_2):
    return dict(zip(list_1, list_2))


cars = ['BMW', 'Porsche', 'Range Rover']
prices = [95800, 110500, 105100]

print(merge_lists_to_dict(list_2=prices, list_1=cars))

first_names = ['John', 'Paul', 'George', 'Ringo']
last_names = ['Lennon', 'McCartney', 'Harrison', 'Starr']

print(merge_lists_to_dict(first_names, list_2=last_names))

# SyntaxError: positional argument follows keyword argument
# print(merge_lists_to_dict(list1=first_names, last_names))
