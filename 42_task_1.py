import json

player = {
    'id': 123,
    'name': 'John',
    'photo': None,
    'points': 99.9,
    'active': True
}

dump = json.dumps(player, indent=2, sort_keys=True)

print('Dump:', dump)
print('Dump type:', type(dump))

restored_object = json.loads(dump)

print('Restored object:', restored_object)
print('Restored object type:', type(restored_object))
print('player == restored_object:', player == restored_object)
