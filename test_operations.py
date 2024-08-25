import unittest
from operations import determine_data_structure

class TestDetermineDataStructure(unittest.TestCase):
    def test_stack(self):
        operations = [("push", 1), ("push", 2), ("pop", 2), ("pop", 1)]
        self.assertEqual(determine_data_structure(operations), "stack")

    def test_queue(self):
        operations = [("push", 1), ("push", 2), ("pop", 1), ("pop", 2)]
        self.assertEqual(determine_data_structure(operations), "queue")

    def test_priority_queue(self):
        operations = [("push", 1), ("push", 2), ("pop", 2), ("pop", 1)]
        self.assertEqual(determine_data_structure(operations), "priority queue")

    def test_impossible(self):
        operations = [("push", 1), ("pop", 1), ("pop", 2)]
        self.assertEqual(determine_data_structure(operations), "impossible")

if __name__ == "__main__":
    unittest.main()
