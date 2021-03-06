import json
import math
import utm
from collections import namedtuple

from cxc_gis.exceptions import LocationsTooLittle
from cxc_gis import flat_geometry
from cxc_gis.mixins import JsonMixin


Point = namedtuple("Point", ["x", "y"])


class Location(JsonMixin):
    """Location class"""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.easting, self.northing, self.zone_number, self.zone_letter = (
            utm.from_latlon(self.latitude, self.longitude)
        )

    @property
    def x(self):
        return self.longitude

    @property
    def y(self):
        return self.latitude

    @property
    def serializable_representation(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    @classmethod
    def from_json_string(cls, string):
        container = json.loads(string)
        assert isinstance(container, dict)
        return cls(**container)

    def __eq__(self, another):
        if (self.latitude == another.latitude
                and self.longitude == another.longitude):
            return True
        return False

    def __repr__(self):
        return "Location(latitude={latitude}, longitude={longitude})".format(
            latitude=self.latitude, longitude=self.longitude
        )

    __str__ = __repr__


class Line():
    """Line class"""

    def __init__(self, endpoint_a, endpoint_b):
        """
        Init a line segments with endpoint_a and endpoint_b

        :param endpoint_a: one endpoint of line
        :type endpoint_a: Location
        :param endpoint_b: another endpoint of line
        :type endpoint_b: Location
        """
        self.endpoint_a = endpoint_a
        self.endpoint_b = endpoint_b

    @property
    def length(self):
        """
        Return length(meter) of the line

        :return: length(meter) of the line
        :rtype: float
        """
        return math.sqrt(
            (self.endpoint_a.northing - self.endpoint_b.northing) ** 2 +
            (self.endpoint_a.easting - self.endpoint_b.easting) ** 2
        )

    def __repr__(self):
        return "Line({a}, {b})".format(
            a=self.endpoint_a, b=self.endpoint_b
        )

    __str__ = __repr__


class Polyline():
    """Polyline class"""
    def __init__(self, locations):
        """
        Init a polyline with locations

        :param locations: locations of ployline
        :type locations: list[Location]
        """
        if len(locations) < 2:
            raise LocationsTooLittle("Requires three or more vertices to form "
                                     "a polygon")
        self.locations = locations

    @property
    def length(self):
        """
        Calculate total length of the polyline

        :return: total length in meters
        :rtype: float
        """
        total_length = 0
        for location_a, location_b in zip(
                self.locations[:-1], self.locations[1:]):
            total_length += Line(location_a, location_b).length
        return total_length

    def __repr__(self):
        return "Polyline({})".format(self.points)

    __str__ = __repr__


class Region(JsonMixin):
    """Region class"""

    def __init__(self, vertices):
        """
        Init a region with vertices

        :param vertices: vertices of region
        :type vertices: list[Location]
        """
        if len(vertices) < 3:
            raise LocationsTooLittle("Requires three or more vertices to form "
                                     "a polygon")
        self.vertices = vertices

    def __contains__(self, location):
        assert isinstance(location, Location)
        return flat_geometry.is_inside(location, self)

    @property
    def serializable_representation(self):
        return [l.serializable_representation for l in self.vertices]

    @classmethod
    def from_json_string(cls, string):
        container = json.loads(string)
        assert isinstance(container, list)
        vertices = [Location(**location) for location in container]
        return cls(vertices)

    def __eq__(self, another):
        if self.vertices == another.vertices:
            return True
        return False

    def __repr__(self):
        return "Region({})".format(self.vertices)

    __str__ = __repr__
