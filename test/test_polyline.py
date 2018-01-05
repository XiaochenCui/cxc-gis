from cxc_gis.models import Polyline

from test.test_base import BaseTestCase


class TestPolyline(BaseTestCase):
    def test_len(self):
        polyline = Polyline([self.location_a, self.location_b,
                             self.location_c, self.location_d,
                             self.location_e, self.location_f, ])
        assert abs(polyline.length - 3033.505) <= 0.5
