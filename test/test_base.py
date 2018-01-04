import unittest

from cxc_gis.models import Point, Location, Region


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.location_a = Location(latitude=30.752149, longitude=103.923801)
        self.location_b = Location(latitude=30.74682, longitude=103.925689)
        self.location_c = Location(latitude=30.749955, longitude=103.92835)
        self.location_d = Location(latitude=30.754712, longitude=103.93056)
        self.location_e = Location(latitude=30.75167, longitude=103.933993)
        self.location_f = Location(latitude=30.743473, longitude=103.931236)
        self.location_g = Location(latitude=30.748175, longitude=103.937427)
        self.location_h = Location(latitude=30.747451, longitude=103.919445)
