# Неправильно:

try:
    raise ValueError()
except Exception:
    print('any error')
except ValueError:
    print('value error')

# Правильно:

try:
    raise ValueError()
except ValueError:
    print('value error')
except Exception:
    print('any error')

# Совсем плохо:

try:
    raise ValueError()
except:
    pass
