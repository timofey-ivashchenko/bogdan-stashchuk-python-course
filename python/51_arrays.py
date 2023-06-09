from array import array

# Создаём массив целых чисел a.

numbers = (1904, 1930, 1957, 1958, 1980, 1986, 2011, 2013, 2015)
a = array('i', numbers)

# Сохраняем массив a в бинарном файле.

filename = 'data/years.bin'

with open(filename, 'wb') as file:
    a.tofile(file)

# Создаём массив b и заполняем его целыми числами из файла.

b = array('i')

with open(filename, 'rb') as file:
    b.fromfile(file, len(numbers))

# Проверяем массивы на равенство.

print('a:', a)
print('b:', b)
print('a == b:', a == b)
