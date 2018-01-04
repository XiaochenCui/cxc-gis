import unittest
import math

from cxc_gis.models import Point, Location, Line
from cxc_gis.flat_geometry import orientation

from test.test_base import BaseTestCase


class TestLine(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.line = Line(self.location_a, self.location_b)

    def test_len(self):
        assert abs(self.line.length - 617.6743) <= 0.5
