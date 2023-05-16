currencies = [
    'Австралийский доллар',
    'AUD',
    'Канадский доллар',
    'CAD',
    'Датская крона',
    'DKK',
    'Евро',
    'EUR',
    'Японская йена',
    'JPY',
    'Норвежская крона',
    'NOK',
    'Фунт стерлингов',
    'GBP',
    'Шведская крона',
    'SEK',
    'Украинская гривня',
    'UAH',
    'Доллар США',
    'USD'
]

currency_codes = [x for x in currencies if len(x) == 3]
currency_names = [x for x in currencies if len(x) > 3]

print('Названия валют:', currency_names)
print('Коды валют:', currency_codes)
