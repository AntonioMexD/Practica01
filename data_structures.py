import heapq

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

class PriorityQueue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        heapq.heappush(self.items, -item)

    def extract_max(self):
        if not self.is_empty():
            return -heapq.heappop(self.items)
        return None

    def is_empty(self):
        return len(self.items) == 0
