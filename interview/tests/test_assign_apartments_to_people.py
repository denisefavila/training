from interview.interview.assign_apartments_to_people import (
    Apartment,
    Person,
    assign_apartments_to_people,
)


def test_assign_apartments_to_people():
    # Test case 1: One person wants a housemate in a two-room apartment

    # Test case 3: Multiple people with varying preferences and available apartments
    apartments = [Apartment(103, 1), Apartment(104, 3)]
    people = [
        Person("Charlie", True),  # Wants housemates
        Person("David", False),  # Does not want housemates
        Person("Eva", True),  # Wants housemates
    ]
    result = assign_apartments_to_people(apartments, people)
    assert result == {
        103: ["David"],  # Assigned to one-room apartment
        104: ["Charlie", "Eva"],  # Assigned to three-room apartment
    }

    # Test case 4: All apartments are single room and all people want housemates
    apartments = [Apartment(105, 1), Apartment(106, 1)]
    people = [Person("Fiona", True), Person("George", True)]
    result = assign_apartments_to_people(apartments, people)
    assert result == {
        105: ["Fiona"],  # First person gets the first apartment
        106: ["George"],  # Second apartment is empty
    }

    # Test case 5: No apartments available
    apartments = []
    people = [Person("Hannah", True)]
    result = assign_apartments_to_people(apartments, people)
    assert result == {}

    # Test case 6: No people but apartments available
    apartments = [Apartment(107, 2)]
    people = []
    result = assign_apartments_to_people(apartments, people)
    assert result == {}
