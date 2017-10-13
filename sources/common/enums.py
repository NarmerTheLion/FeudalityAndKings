""" enums
The Enumeration used across this project
"""
from enum import Enum


class UnitTypes(Enum):
    """ UnitTypes
    The defined types that are used in this project
    """
    INF = 'infantry'
    CAV = 'cavalry'
    FART = 'field artilery'
    FOR = 'fortification'