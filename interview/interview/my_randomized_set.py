import random


class RandomizedSet:
    """
    Design a data structure that supports insert,
    delete, search and getRandom in constant time.

    random -> list
    insert -> O(1) at the end list,  delete -> O(1) from the end`
    search O(1) ? Dictionary
    """

    def __init__(self):
        self.value_to_idx = {}
        self.values = []

    def insert(self, val):
        if val in self.value_to_idx:
            # already exist
            return False

        # don't exist, add it
        self.value_to_idx[val] = len(self.values)
        self.values.append(val)
        return True

    def delete(self, val):
        if val not in self.value_to_idx:
            # dont exist
            return False

        # swap the current value with the element at the end
        current_idx = self.value_to_idx[val]
        current_last_value = self.values[-1]

        self.values[current_idx] = current_last_value
        self.value_to_idx[current_last_value] = current_idx

        self.values.pop()
        del self.value_to_idx[val]
        return True

    def get_random(self):
        return random.choice(self.values)

    def search(self, val):
        if val in self.value_to_idx:
            return True

        return False
