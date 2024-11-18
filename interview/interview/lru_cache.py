from typing import Any, Dict
from collections import OrderedDict


class ListNode:
    def __init__(self, key: Any, value: Any):
        self.key: Any = key
        self.value: Any = value
        self.next: ListNode = None
        self.previous: ListNode = None


class LRURache:
    def __init__(self, capacity: int):
        """
        cache = LRUCache(2)
        timestamp = 1, cache.get(key) -> recently use at timestamp = 1
        timestamp = 2, cache.put(key, value) -> recently use at timestamp = 2
        """
        self.capacity: int = capacity
        self.mapping: Dict[Any, ListNode] = {}
        self.head: ListNode = None
        self.tail: ListNode = None

    def _remove_node(self, node: ListNode):
        if node.previous:
            node.previous.next = node.next

        else:
            self.head = node.next  # its head

        if node.next:
            node.next.previous = node.previous

        else:
            self.tail = node.previous

    def _add_to_tail(self, node: ListNode):
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            node.next = None

    def get(self, key: Any):
        """
        Return the value if exists, otherwise -1
        O(1)
        """
        if key in self.mapping:
            # remove the current Node
            current_node = self.mapping[key]
            self._remove_node(current_node)

            # add to the end
            self._add_to_tail(current_node)

            # return value
            return current_node.value

        else:
            return -1

    def put(self, key: Any, value: Any):
        """
        Update the value of the key if the key exists
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation,
        evict the least recently used key.
        O(1)
        """
        if key in self.mapping:
            node = self.mapping[key]
            self._remove_node(node)
            node.value = value
            self._add_to_tail(node)

        else:
            node = ListNode(key=key, value=value)
            self.mapping[key] = node
            self._add_to_tail(node)

            if len(self.mapping) > self.capacity:
                lru = self.head  # Least recently used node
                self._remove_node(lru)
                del self.mapping[lru.key]


class LRURache2:
    def __init__(self, capacity: int):
        """
        cache = LRUCache(2)
        timestamp = 1, cache.get(key) -> recently use at timestamp = 1
        timestamp = 2, cache.put(key, value) -> recently use at timestamp = 2
        """
        self.capacity = capacity
        self.cache = (
            OrderedDict()
        )  # O(1) complexity for insertion, deletion, and updates.

    def get(self, key: Any):
        """
        Return the value if exists, otherwise -1
        O(1)
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

        else:
            return -1

    def put(self, key: Any, value: Any):
        """
        Update the value of the key if the key exists
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation,
        evict the least recently used key.
        O(1)
        """
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value
