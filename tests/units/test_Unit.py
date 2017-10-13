from unittest import TestCase
from sources.common.enums import UnitTypes
from sources.units.Unit import *


class testUnit(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_id(self):
        unit = Unit()
        id = unit.get_ID()
        id_dir = unit.id
        self.assertEqual(id, id_dir, "The ID of the unit changed")
        id = unit.get_ID()
        self.assertEqual(id, id_dir, "The ID of the unit changed")
        unit.die()

    def test_variable(self):
        units = [Unit(), Cavalry(), Infantry()]
        control = units[0].id
        for unit in units:
            self.assertEqual(control, unit.id)
            unit.die

        # See if the children don't effect the parent
        units = [Cavalry(), Infantry(), Unit()]
        control = units[0].id
        for unit in units:
            self.assertEqual(control, unit.id)
            unit.die

    def test_die(self):
        unit = Unit()
        unit2 = Unit()
        self.assertNotEqual(unit.id+1, unit2.id)

        control_id = unit.id
        unit.die()
        unit2.die()
        unit2 =Unit()
        self.assertEqual(control_id, unit2.id)
        unit2.die()