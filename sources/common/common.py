""" Full generic and common structures
"""


def switch(x, options):
    """ Switch
    Function
    """
    if x in options:
        return options[x]
    return options['default']