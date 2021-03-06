
'''
LIGHTWEIGHT MODULE FOR HANDLING LL97 CALCS.
'''


# CO2 limits per LL97
co2_limits = {
    'A': [0.01074, 0.0042, 0.0014],
    'B_HEALTH':	[0.02381, 0.0133, 0.0014],
    'B_REGULAR': [0.00846, 0.00453, 0.0014],
    'E': [0.00758,	0.00344, 0.0014	],
    'F': [0.00574, 0.00167, 0.0014],
    'H': [0.02381, 0.0133, 0.0014],
    'I1': [0.01138, 0.00598, 0.0014],
    'I2': [0.02381, 0.0133, 0.0014],
    'I3': [0.02381, 0.0133, 0.0014],
    'I4': [0.00758, 0.00344, 0.0014],
    'M': [0.0118, 0.00403, 0.0014],
    'R1': [0.00987, 0.00526, 0.0014],
    'R2': [0.00675, 0.00407, 0.0014],
    'S': [0.0042, 0.0011, 0.0014],
    'U': [0.00426, 0.0011, 0.0014],
}

# kbtu to co2
carbon_conversion_rates = {
    'elec': 0.000084689,
    'gas': 0.00005311,
    'steam': 0.00004493,
    'fuel_two': 0.00007421,
    'fuel_four': 0.00007529
}

# convert kwh / therm / lbs / gal to kbtu
native_to_kbtu_conversion = {
    'elec': 3.412,
    'gas': 100,
    'steam': 1194,
    'fuel_two': 138,
    'fuel_four': 146
}

fine_per_ton_co2 = 268


def get_total_area(bldgtypes):
    area = 0
    for t in bldgtypes:
        area += t[1]
    return area


def get_carbon_limits(bldgtypes):
    limit_2024 = 0
    limit_2030 = 0
    limit_2034 = 0

    for t in bldgtypes:
        tag, area = t
        limits = co2_limits[tag]
        limit_2024 += area * limits[0]
        limit_2030 += area * limits[1]
        limit_2034 += area * limits[2]

    return {
        '2024': limit_2024,
        '2030': limit_2030,
        '2034': limit_2034
    }


def get_total_carbon(consumptiondict):
    carbon = 0
    for key, val in consumptiondict.items():
        consumption_kbtu = native_to_kbtu_conversion[key] * val
        carbon += carbon_conversion_rates[key] * consumption_kbtu
    return carbon


def get_fines(limits, total_carbon):
    fines = {}
    for year, limit in limits.items():
        if total_carbon < limit:
            fines[year] = 0
        else:
            fine = fine_per_ton_co2 * (total_carbon - limit)
            fines[year] = fine
    return fines


def validate_building_types(types):
    isvalid = True
    for t in types:
        if t[0] not in co2_limits:
            isvalid = False
    return isvalid


def get_ll97_summary(bldgtypes, utilityconsumption):
    '''
    main function. 

    arguments:
    - bldgtypes: list of iterables (list or tuple) containing 'type' (str) followed by 'area' (int/float) 
    - utilityconsumption: dictionary with any of 'elec', 'gas', 'steam', 'fuel_two', 'fuel_four' keys

    valid building types:
    A, B_HEALTH, B_REGULAR, E, F, H, I1, I2, I3, I4, M, R1, R2, S, U

    example: 

    mybldgareas = [
            ('I4', 22000),
            ('B_REGULAR', 3340)
    ]

    myutilities = {
        'elec': 1133334, 
        'gas': 3432, 
        'steam': 43,
        'fuel_two': 4443, 
    }

    results = pyll97.get_ll97_summary(mybldgareas, myutilities)

    returns: summary dictionary with fines, limits and total carbon.
    '''

    if not validate_building_types(bldgtypes):
        raise ValueError(
            f'incorrect building types passed. valid types: {[x for x in co2_limits.keys()]}'
        )

    limits = get_carbon_limits(bldgtypes)
    total_carbon = get_total_carbon(utilityconsumption)
    fines = get_fines(limits, total_carbon)

    if get_total_area(bldgtypes) < 20000:
        summary = {
            'limits': {'2024': 0, '2030': 0, '2034': 0},
            'total_carbon': total_carbon,
            'fines': {'2024': 0, '2030': 0, '2034': 0}
        }

    else:
        summary = {
            'limits': limits,
            'total_carbon': total_carbon,
            'fines': fines
        }

    return summary
