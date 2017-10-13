""" Unit
The Base unit type
"""
from sources.common.location import Location
from sources.common.enums import UnitTypes
from sources.common.formatter import int_to_counted
import json, sys

stats = {
    UnitTypes.INF: {
        'max_hp': 100,
        'attack': 5,
        'defence': 5,
        'upkeep': 500,
    }
}


class Unit:
    """ The Basic unit type
    """
    UsedID = {1: False}
    def __init__(self, unit_type=UnitTypes.INF):
        """ Constructor
        Args:
            type: (UnitType) The type of unit this is
        """
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.maxhp = 0
        self.upkeep = 0
        self.location = Location(0, 0)
        self.type = unit_type
        self.id = None

        # Further setup functions
        self.get_ID()

    def __del__(self):
        self.die()

    def get_ID(self):
        """ nextID
        Get a free and next id for this type
        """
        if self.id is None:
            for idnumber in self.UsedID:
                if not self.UsedID[idnumber]:
                    self.UsedID[idnumber] = True
                    self.id = idnumber
                    return self.id
            self.UsedID[self.UsedID.__len__() + 1] = False
            self.id = self.get_ID()
        return self.id

    def die(self):
        """ die
        Call to kill the unit
        """
        self.UsedID[self.id] = False

    def print(self):
        """ print
        Return a string representation
        """
        str_repres = 'The %s %s regiment' % (int_to_counted(self.id), self.type.value)
        return str_repres


class Infantry(Unit):
    """ Infantry
    The Base Infantry class
    """
    UsedID = {}

    def __init__(self):
        Unit.__init__(self, UnitTypes.INF)


class Cavalry(Unit):
    """ Infantry
    The Base Infantry class
    """
    UsedID = {}

    def __init__(self):
        Unit.__init__(self, UnitTypes.CAV)

if __name__ == '__main__':
    for i in range(0, 500):
        infantry = Unit(UnitTypes.INF)
        print(infantry.print())
        infantry = Infantry()
        print(infantry.print())
        cav = Cavalry()
        print(cav.print())

    unit = Unit()
    for atr in stats[UnitTypes.INF]:
        print(atr, stats[UnitTypes.INF][atr])
        unit.__setattr__(atr, stats[UnitTypes.INF][atr])
    print(unit)
