""" Formatter
Collection of function that return formatter version of the input
"""
from sources.common.common import switch

def int_to_counted(int_in):
    """
    Formats a number with it's english count word e.g. 1 => 1st
    :param int_in: the integer number
    :return: string
    """
    dict_str = {
        1: ' st',
        2: ' nd',
        3: ' rd',
        'default': ' th'
    }
    if int_in % 100 >20:
        number = int_in % 10
    else:
        number = int_in % 20
    return str(int_in) + switch(number, dict_str)
