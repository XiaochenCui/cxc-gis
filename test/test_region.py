import unittest

from cxc_gis.models import Location, Region
from cxc_gis.exceptions import LocationsTooLittle

from test.test_base import BaseTestCase


class TestRegion(BaseTestCase):
    def test_init(self):
        with self.assertRaises(LocationsTooLittle):
            region = Region([self.location_a, self.location_e])
