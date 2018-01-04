import unittest
import math

from cxc_gis.models import Point, Location, Line, Region
from cxc_gis.flat_geometry import (on_segment,
                                   orientation,
                                   is_intersect,
                                   )

from test.test_base import BaseTestCase


class TestFlatGeometry(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.point_a = Point(0, 1)
        self.point_b = Point(1, 2)
        self.point_c = Point(2, 3)
        self.point_d = Point(3, 4)

    def test_on_segment(self):
        assert on_segment(self.point_a, self.point_b, self.point_c)
        assert not on_segment(self.point_b, self.point_a, self.point_c)
        assert not on_segment(self.location_a, self.location_b,
                              self.location_c)

    def test_orientation(self):
        assert orientation(self.location_e, self.location_g,
                           self.location_f) == 1
        assert orientation(self.location_a, self.location_b,
                           self.location_c) == 2
        assert orientation(self.point_a, self.point_b, self.point_c) == 0
        assert orientation(self.point_a, self.point_c, self.point_b) == 0

    def test_is_intersect(self):
        assert not is_intersect(Line(self.point_a, self.point_b),
                                Line(self.point_c, self.point_d))
        assert is_intersect(Line(self.point_a, self.point_c),
                            Line(self.point_b, self.point_d))

        assert is_intersect(Line(self.location_a, self.location_g),
                            Line(self.location_b, self.location_d))
        assert is_intersect(Line(self.location_e, self.location_f),
                            Line(self.location_g, self.location_c))
        assert not is_intersect(Line(self.location_a, self.location_b),
                                Line(self.location_c, self.location_d))
        assert not is_intersect(Line(self.location_e, self.location_g),
                                Line(self.location_a, self.location_f))

    def test_location_in_region(self):
        region_1 = Region([self.location_a, self.location_e, self.location_g,
                           self.location_b])
        assert self.location_c in region_1
