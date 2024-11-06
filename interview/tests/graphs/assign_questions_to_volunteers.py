from interview.graph.assign_questions_to_volunteers import \
    assign_questions_to_volunteers


def test_assign_questions_to_volunteers_basic_case():
    questions = [
        {"id": 1, "tags": ["MAC", "VSCODE"]},
        {"id": 2, "tags": ["PY", "AI"]},
        {"id": 3, "tags": ["JAVA", "OS"]},
        {"id": 4, "tags": ["PY", "NW"]},
    ]

    volunteers = [
        {"id": 1, "tags": ["PY", "NW"], "name": "A"},
        {"id": 2, "tags": ["AI"], "name": "B"},
        {"id": 3, "tags": ["JAVA", "NW"], "name": "C"},
        {"id": 4, "tags": ["JAVA", "NW"], "name": "D"},
    ]

    expected_output = {
        2: 2,  # Question 2 is assigned to Volunteer B (tag: "AI")
        3: 3,  # Question 3 is assigned to Volunteer C (tag: "JAVA")
        4: 1,  # Question 4 is assigned to Volunteer A (tag: "PY")
    }

    expected_output1 = {
        2: 1,
        3: 3,
        4: 4,
    }

    result = assign_questions_to_volunteers(questions, volunteers)
    assert result == expected_output or result == expected_output1


def test_assign_questions_to_volunteers_no_matches():
    questions = [
        {"id": 1, "tags": ["CSS", "HTML"]},
        {"id": 2, "tags": ["REACT"]},
    ]

    volunteers = [
        {"id": 1, "tags": ["PYTHON"], "name": "A"},
        {"id": 2, "tags": ["JAVA"], "name": "B"},
    ]

    # No volunteer has matching tags with any question
    expected_output = {}

    assert assign_questions_to_volunteers(questions, volunteers) == expected_output


def test_assign_questions_to_volunteers_all_questions_assigned():
    questions = [
        {"id": 1, "tags": ["AI", "ML"]},
        {"id": 2, "tags": ["PY"]},
    ]

    volunteers = [
        {"id": 1, "tags": ["AI", "ML"], "name": "A"},
        {"id": 2, "tags": ["PY"], "name": "B"},
    ]

    # Each question has a volunteer with matching tags
    expected_output = {
        1: 1,  # Question 1 assigned to Volunteer A
        2: 2,  # Question 2 assigned to Volunteer B
    }

    assert assign_questions_to_volunteers(questions, volunteers) == expected_output


def test_assign_questions_to_volunteers_more_volunteers_than_questions():
    questions = [
        {"id": 1, "tags": ["PY"]},
        {"id": 2, "tags": ["JAVA"]},
    ]

    volunteers = [
        {"id": 1, "tags": ["PY"], "name": "A"},
        {"id": 2, "tags": ["JAVA"], "name": "B"},
        {"id": 3, "tags": ["C++"], "name": "C"},
        {"id": 4, "tags": ["RUBY"], "name": "D"},
    ]

    expected_output = {
        1: 1,  # Question 1 assigned to Volunteer A
        2: 2,  # Question 2 assigned to Volunteer B
    }

    assert assign_questions_to_volunteers(questions, volunteers) == expected_output


def test_assign_questions_to_volunteers_more_questions_than_volunteers():
    questions = [
        {"id": 1, "tags": ["PY"]},
        {"id": 2, "tags": ["JAVA"]},
        {"id": 3, "tags": ["HTML"]},
        {"id": 4, "tags": ["CSS"]},
    ]

    volunteers = [
        {"id": 1, "tags": ["PY"], "name": "A"},
        {"id": 2, "tags": ["JAVA"], "name": "B"},
    ]

    # Only the first two questions have matching volunteers
    expected_output = {
        1: 1,  # Question 1 assigned to Volunteer A
        2: 2,  # Question 2 assigned to Volunteer B
    }

    assert assign_questions_to_volunteers(questions, volunteers) == expected_output


def test_assign_questions_to_volunteers_multiple_possible_matches():
    questions = [
        {"id": 1, "tags": ["PY"]},
        {"id": 2, "tags": ["JAVA"]},
        {"id": 3, "tags": ["HTML"]},
        {"id": 4, "tags": ["CSS"]},
    ]

    volunteers = [
        {"id": 1, "tags": ["PY", "HTML"], "name": "A"},
        {"id": 2, "tags": ["JAVA", "CSS"], "name": "B"},
    ]

    # Multiple tags match multiple questions
    expected_output = {
        1: 1,  # Question 1 assigned to Volunteer A
        2: 2,  # Question 2 assigned to Volunteer B
    }

    assert assign_questions_to_volunteers(questions, volunteers) == expected_output
