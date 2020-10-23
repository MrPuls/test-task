import math
from decimal import Decimal


def convert_dec_degree_to_deg_dec_min(degrees, compass_type='lon'):
    decimals, number = math.modf(degrees)
    deg = int(number)
    minutes = float(format(Decimal.from_float(decimals * 60), '.4')) if decimals != 0 else int(decimals * 60)
    compass = {
        'lat': ('N', 'S'),
        'lon': ('E', 'W')
    }
    compass_str = compass[compass_type][0 if deg >= 0 else 1]
    return '{}^{}{}'.format(abs(deg), abs(minutes), compass_str)
