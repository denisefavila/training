import heapq
from collections import defaultdict
from typing import Collection, Dict, List


class Apartment:
    def __init__(self, apt_number: int, num_rooms: int):
        self.apt_number = apt_number
        self.num_rooms = num_rooms


class Person:
    def __init__(self, name: str, wants_housemates: bool):
        self.name = name  # Unique ID
        self.wants_housemates = wants_housemates


def assign_apartments_to_people(apartments: List[Apartment], people: List[Person]):
    """
    Your organization has hired interns who need to
    relocate for the summer. You are in charge of assigning
    apartments to them. Each intern will get their own room.
    They can choose whether they prefer to share a 2+ room apartment
    or get a one-bedroom to themselves.
    Note that they may not get what they want because the apartments vary
    in the number of rooms that they have.
    """
    assignments = defaultdict(list)

    queue_apartments = []
    for apartment in apartments:
        heapq.heappush(
            queue_apartments,
            (apartment.num_rooms, apartment.num_rooms, apartment.apt_number),
        )

    people_sorted = sorted(people, key=lambda person: person.wants_housemates)

    idx = 0
    while queue_apartments and idx < len(people_sorted):
        num_rooms, available_rooms, apartment_number = heapq.heappop(
            queue_apartments
        )  # Get the apartment with the least rooms

        person = people_sorted[idx]
        assignments[apartment_number].append(person.name)

        idx += 1

        available_rooms -= 1
        if available_rooms > 0:
            heapq.heappush(
                queue_apartments, (num_rooms, available_rooms, apartment_number)
            )

    return assignments
