from cxc_gis.models import Location, Region


def init_locations():
    pass


class TestLocation():
    pass


class TestUtm():

    def test_utm(self):
        location = Location(latitude=51.2, longitude=7.5)
        assert location.latitude == 51.2
        assert location.longitude == 7.5
        assert location.easting == 395201.3103811303
        assert location.northing == 5673135.241182375
        assert location.zone_number == 32
        assert location.zone_letter == "U"
