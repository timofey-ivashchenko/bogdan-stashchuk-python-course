currencies = {
    'Australian dollar': 'aud',
    'Canadian dollar': 'cad',
    'Danish krone': 'dkk',
    'Euro': 'eur',
    'Japanese yen': 'jpy',
    'Norwegian krone': 'nok',
    'Pound sterling': 'gbp',
    'Swedish krona': 'sek',
    'Ukrainian hryvnia': 'uah',
    'United States dollar': 'usd'
}

print(currencies)

currencies = {k: v.upper() for k, v in currencies.items()}

print(currencies)
