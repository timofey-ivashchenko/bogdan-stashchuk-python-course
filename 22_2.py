def update_car_info(**car):
    car['is_available'] = True
    return car


print(update_car_info(brand='Porsche', price=15000))

# TypeError: update_car_info() takes 0 positional arguments but 2 were given
# print(update_car_info('Porsche', 15000))
