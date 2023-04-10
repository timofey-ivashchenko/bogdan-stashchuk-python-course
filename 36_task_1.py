def dict_to_list(dict: dict) -> list:
    list = []

    for k, v in dict.items():
        if type(v) is int:
            v *= 2

        list.append((k, v))

    return list


source = {'a': 5, 'b': 3.3}
target = dict_to_list(source)
print(source, '->', target)
