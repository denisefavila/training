import heapq
from typing import List

from interview.interview.general.euclidian_distance import euclidean_distance


def get_k_closest_points_to_origin(points: List[List[int]], k):
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
    and an integer k, return the k closest points to the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance
    (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique
    (except for the order that it is in).

    https://leetcode.com/problems/k-closest-points-to-origin/description/

    """
    max_heap = []

    for point in points:
        distance_to_origin = euclidean_distance(point, (0, 0))
        heapq.heappush(max_heap, (-distance_to_origin, point))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    answer = [point for _, point in max_heap]
    return answer
