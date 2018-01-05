from cxc_gis.models import Point, Location, Region

from test.test_base import BaseTestCase


class TestLocation(BaseTestCase):
    def test_utm(self):
        location = Location(latitude=51.2, longitude=7.5)
        assert location.latitude == 51.2
        assert location.longitude == 7.5
        assert location.easting == 395201.3103811303
        assert location.northing == 5673135.241182375
        assert location.zone_number == 32
        assert location.zone_letter == "U"

    def test_json(self):
        string = self.location_a.json
        loaded_location = Location.from_json_string(string)
        assert self.location_a == loaded_location
