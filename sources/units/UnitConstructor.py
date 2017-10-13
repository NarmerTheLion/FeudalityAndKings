""" A factory model that constructors unit types
"""
from sources.units.Unit import Unit
from sources.common.enums import UnitTypes
from sources.common.common import switch


def _unit():
    """ Factory that will built a unit
    """
    unit = Unit()
    unit.attack = 1
    return unit


def _default():
    """ Default switch option
    """
    return "Not Implemented yet"


class UnitConstructor:
    """ Factory that combines the creation of units"""
    def __init__(self):
        """ Constructor
        Will set all parameters for the initialization
        """
        pass #

    def create_unit(self, unit_type):
        """ Switch case
        run the function that is selected with the key in the dictionary
        """
        return switch(unit_type, {
            UnitTypes.INF: _unit,
            'default': _default
        })()