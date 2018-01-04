from cxc_gis.models import Point, location, Line


def on_segment(point_p, point_q, point_r):
    """
    Given three colinear points p, q, r, the function checks if point q
    lies on line segment "pr"

    :param point_p:
    :type point_p: Point
    :param point_q:
    :type point_q: Point
    :param point_r:
    :type point_r: Point
    :return: if point r on line segment "pr"
    :rtype: bool
    """
    if (point_q.x <= max(point_p.x, point_r.x) and
            point_q.x >= min(point_p.x, point_r.x) and
            point_q.y <= max(point_p.y, point_r.y) and
            point_q.y >= min(point_p.y, point_r.y)):
        return True
    return False


def orientation(point_p, point_q, point_r):
    """
    To find orientation of ordered triplet (p, q, r).

    :param point_p:
    :type point_p: Point
    :param point_q:
    :type point_q: Point
    :param point_r:
    :type point_r: Point
    :return: 0: p, q and r are colinear
             1: clockwise
             2: counterclockwise
    :rtype: int
    """
    # Set https://www.geeksforgeeks.org/orientation-3-ordered-points/
    # for details of below formula.
    r = ((point_q.y - point_p.y) * (point_r.x - point_q.x) -
         (point_q.x - point_p.x) * (point_r.y - point_q.y))
    if r == 0:
        return 0
    return 1 if r > 0 else 2


def is_intersect(line_a, line_b):
    """
    Determine if lina_a intersect with line_b

    :param lina_a:
    :type lina_a: Line
    :param lina_b:
    :type line_b: Line
    :return:
    :rtype: bool
    """
    # Find the four orientations needed for general and special cases
    orientation_1 = orientation(line_a.endpoint_a, line_a.endpoint_b,
                                line_b.endpoint_a)
    orientation_2 = orientation(line_a.endpoint_a, line_a.endpoint_b,
                                line_b.endpoint_b)
    orientation_3 = orientation(line_b.endpoint_a, line_b.endpoint_b,
                                line_a.endpoint_a)
    orientation_4 = orientation(line_b.endpoint_a, line_b.endpoint_b,
                                line_a.endpoint_b)

    # General case
    if (orientation_1 != orientation_2 and orientation_3 != orientation_4):
        return True

    # Special cases
    if (orientation_1 == 0 and on_segment(line_a.endpoint_a, line_b.endpoint_a,
                                          line_a.endpoint_b)):
        return True
    if (orientation_2 == 0 and on_segment(line_a.endpoint_a, line_b.endpoint_b,
                                          line_a.endpoint_b)):
        return True
    if (orientation_3 == 0 and on_segment(line_b.endpoint_a, line_a.endpoint_a,
                                          line_b.endpoint_b)):
        return True
    if (orientation_4 == 0 and on_segment(line_b.endpoint_a, line_a.endpoint_b,
                                          line_b.endpoint_b)):
        return True

    return False


def is_inside(point, region):
    """
    Detemine if point is in region

    :param point:
    :type point: Point
    :param region:
    :type region: Region
    """
    points = region.vertices
    extrame = Point(x=1000000, y=point.y)

    points = points.append(points[0])
    intersect_count = 0
    for i in range(len(points) - 1):
        if is_intersect(Line(point, extrame), Line(points[i], points[i+1])):
            intersect_count += 1
    return intersect_count % 2 == 1
