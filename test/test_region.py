import unittest

from cxc_gis.models import Location, Region
from cxc_gis.exceptions import LocationsTooLittle

from test.test_base import BaseTestCase


class TestRegion(BaseTestCase):
    def test_init(self):
        with self.assertRaises(LocationsTooLittle):
            region = Region([self.location_a, self.location_e])

    def test_json(self):
        region = Region([self.location_a, self.location_b, self.location_c,
                        self.location_d, self.location_e])
        string = region.json
        loaded_region = Region.from_json_string(string)
        assert region == loaded_region
