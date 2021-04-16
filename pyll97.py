import os
import re
import pandas as pd

CO2_LIMITS_BY_BUILDING_TYPE = {
    'A':	[0.01074, 0.0042, 0.0014],
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

CARBON_CONVERSION = {
    'elec': 0.000288962,  # tCO2 / kWh
    'gas': 0.005311,  # tCO2 / Therm
    'steam': 0.053646,  # tCO2/MMBtu (from 66.4 kg/MMBtu)
    'fuel_two': '???',
    'fuel_four': '???'
}

KBTU_CONVERSION = {  # convert to kbtu
    'elec': 3.412,
    'gas': 100,
    'steam': 1194,
    'fuel_two': '???',
    'fuel_four': '???'
}


def get_ll97_summary(bldgtypes, utilityconsumption):
    print(bldgtypes)
    return


a = '2'
