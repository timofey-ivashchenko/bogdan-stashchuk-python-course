def get_value(dict: dict, key: str) -> (int | float | None):
    if key not in dict:
        return None

    value = dict[key]
    value_type = type(value)

    if value_type is not int and value_type is not float:
        return None

    return value if value >= 0 else None


def route_info(route: dict) -> str:
    distance = get_value(route, 'distance')

    if distance is not None:
        return f"Расстояние до пункта назначения составляет {distance} км."

    speed = get_value(route, 'speed')
    time = get_value(route, 'time')

    if speed is not None and time is not None:
        return f"Расстояние до пункта назначения составит {speed * time} км."

    return "Нет информации о расстоянии."


distance_values = ['100', 100, 99.5, 0, 0.0, -1, -1.5]

for distance in distance_values:
    print(route_info({'distance': distance}))

speed_values = ['90', 90, 99.5, 0, 0.0, -1, -1.5]
time_values = ['1', 1, 1.5, 0, 0.0, -1, -1.5]

for speed in speed_values:
    print()

    for time in time_values:
        print(route_info({'speed': speed, 'time': time}))
