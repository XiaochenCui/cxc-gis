import utm


class Location():
    """Location class"""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.easting, self.northing, self.zone_number, self.zone_letter = (
            utm.from_latlon(self.latitude, self.longitude)
        )

    def __repr__(self):
        return "Location(latitude={latitude}, longitude={longitude})".format(
            latitude=self.latitude, longitude=self.longitude
        )

    __str__ = __repr__


class Region():
    """Region class"""

    def __init__(self, vertices):
        """
        Init a region with vertices

        :param vertices: vertices of region
        :type vertices: list[Location]
        """
        pass
