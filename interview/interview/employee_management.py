class EmployeeManagement:
    def __init__(self):
        self.manager_to_employees = {}  # {A: {B,C}, B: {D}}
        self.employee_to_manager = {}  # {B: A, C: A, D: B}
        self.dummies = set()

    def set_manager(self, manager, employee):
        # if already exist a manager, remove it
        if employee in self.employee_to_manager:
            current_employee_manager = self.employee_to_manager[employee]
            # If the manager is dummy
            if current_employee_manager in self.dummies:
                all_employees = self.manager_to_employees[
                    current_employee_manager
                ] - set(employee)
                for employee_dummy_manager in all_employees:
                    self.employee_to_manager[employee_dummy_manager] = manager
                    if manager not in self.manager_to_employees:
                        self.manager_to_employees[manager] = set()
                    self.manager_to_employees[manager].add(employee_dummy_manager)
                del self.manager_to_employees[current_employee_manager]

            else:
                self.manager_to_employees[current_employee_manager].remove(employee)
                if self.manager_to_employees[current_employee_manager] == set():
                    del self.manager_to_employees[current_employee_manager]

        # set management
        if manager not in self.manager_to_employees:
            self.manager_to_employees[manager] = set()
        self.manager_to_employees[manager].add(employee)
        self.employee_to_manager[employee] = manager

    def set_peers(self, employee_a, employee_b):
        # First case: we already have a designed managers to employee_a or employee_b
        if employee_a in self.employee_to_manager:
            manager_employee_a = self.employee_to_manager[employee_a]
            self.set_manager(manager_employee_a, employee_b)

        elif employee_b in self.employee_to_manager:
            manager_employee_b = self.employee_to_manager[employee_b]
            self.set_manager(manager_employee_b, employee_a)

        # We don't have an already designed manager
        else:
            dummy_manager = f"Manager_{employee_a}_{employee_b}"
            self.dummies.add(dummy_manager)
            self.set_manager(dummy_manager, employee_a)
            self.set_manager(dummy_manager, employee_b)

    def is_in_management_chain(self, employee_a, employee_b):
        # is_in_management_chain(B, D) -> True
        current = employee_b
        while current in self.employee_to_manager:
            manager = self.employee_to_manager[current]
            if manager == employee_a:
                return True
            current = manager

        return False
