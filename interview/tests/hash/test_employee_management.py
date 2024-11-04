from interview.hash.employee_management import EmployeeManagement


def test_set_manager():
    em = EmployeeManagement()
    em.set_manager("Alice", "Bob")
    em.set_manager("Alice", "Charlie")

    assert em.employee_to_manager["Bob"] == "Alice"
    assert em.employee_to_manager["Charlie"] == "Alice"
    assert em.manager_to_employees["Alice"] == {"Bob", "Charlie"}


def test_set_manager_with_existing_manager():
    em = EmployeeManagement()
    em.set_manager("Alice", "Bob")
    em.set_manager("DummyManager", "Bob")  # Set a dummy manager
    em.set_manager("Alice", "Bob")  # Reassign to Alice

    assert em.employee_to_manager["Bob"] == "Alice"
    assert em.manager_to_employees["Alice"] == {"Bob"}
    assert "DummyManager" not in em.manager_to_employees


def test_set_peers_with_manager():
    em = EmployeeManagement()
    em.set_manager("Alice", "Bob")
    em.set_peers("Bob", "Charlie")  # Charlie should be under Alice

    assert em.employee_to_manager["Charlie"] == "Alice"
    assert em.manager_to_employees["Alice"] == {"Bob", "Charlie"}


def test_set_peers_without_manager():
    em = EmployeeManagement()
    em.set_peers("Eve", "Dave")

    assert "Eve" in em.employee_to_manager
    assert "Dave" in em.employee_to_manager
    manager = em.employee_to_manager["Eve"]

    assert em.employee_to_manager["Dave"] == manager
    assert em.manager_to_employees[manager] == {"Eve", "Dave"}


def test_is_in_management_chain():
    em = EmployeeManagement()
    em.set_manager("Alice", "Bob")
    em.set_manager("Bob", "Charlie")
    em.set_manager("Charlie", "Dave")

    assert em.is_in_management_chain("Alice", "Dave")
    assert em.is_in_management_chain("Alice", "Charlie")
    assert em.is_in_management_chain("Bob", "Dave")
    assert not em.is_in_management_chain("Dave", "Alice")
    assert not em.is_in_management_chain("Charlie", "Bob")


def test_is_in_management_chain_with_peers():
    em = EmployeeManagement()
    em.set_peers("Eve", "Dave")
    em.set_manager("Alice", "Eve")

    assert em.is_in_management_chain("Alice", "Dave")
    assert em.is_in_management_chain("Alice", "Eve")
    assert not em.is_in_management_chain("Eve", "Alice")
