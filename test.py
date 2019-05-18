import unittest

from main import *


def prepare_list():
    result = LinkedList()

    result.add_in_tail(Node(42))
    result.add_in_tail(Node(33))
    result.add_in_tail(Node(11))
    result.add_in_tail(Node(22))
    result.add_in_tail(Node(15))
    result.add_in_tail(Node(42))
    result.add_in_tail(Node(10))
    result.add_in_tail(Node(32))
    result.add_in_tail(Node(42))
    result.add_in_tail(Node(60))
    result.add_in_tail(Node(70))
    result.add_in_tail(Node(66))

    return result


class LinkedListTests(unittest.TestCase):
    def test_remove_node_present_once(self):
        test_list = prepare_list()
        test_list.remove_with_value(11)
        self.assertEqual(test_list.to_values_list(), [42, 33, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'remove_with_value'. Value in list presents ones")

    def test_remove_node_present_multiple(self):
        test_list = prepare_list()
        test_list.remove_with_value(42)
        self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'remove_with_value'. Value in list presents multiple times")

    def test_remove_node_which_not_present(self):
        test_list = prepare_list()
        test_list.remove_with_value(99)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'remove_with_value'. Value in list not present")

    def test_remove_node_at_last_position(self):
        test_list = prepare_list()
        test_list.remove_with_value(66)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70],
                         "Testing: 'remove_with_value'.Value in list placed in tail")

    # ---------------------------------------------------------------------------------------------

    def test_remove_all_nodes_present_once(self):
        test_list = prepare_list()
        test_list.remove_all_with_value(15)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'remove_all_with_value'. Value in list present once")

    def test_remove_all_nodes_present_multiple(self):
        test_list = prepare_list()
        test_list.remove_all_with_value(42)
        self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 10, 32, 60, 70, 66],
                         "Testing: 'remove_all_with_value'. Value in list present multiple")

    def test_remove_all_nodes_node_at_last_position(self):
        test_list = prepare_list()
        test_list.remove_all_with_value(66)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70],
                         "Testing: 'remove_all_with_value'. Value in list at last position")

    # ---------------------------------------------------------------------------------------------

    def test_clear_with_normal_list(self):
        test_list = prepare_list()
        test_list.clear()
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'clear'. List must be empty")

    def test_clear_with_empty_list(self):
        test_list = LinkedList()
        test_list.clear()
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'clear'. List must be empty")

    # ---------------------------------------------------------------------------------------------

    def test_find_all_with_value_one_value(self):
        test_list = prepare_list()
        result = test_list.find_all_with_value(33)
        self.assertEqual(result, [test_list.get_at(1)],
                         "Testing: 'find_all_with_value'. Present one value")

    def test_find_all_with_value_multiple_values(self):
        test_list = prepare_list()
        result = test_list.find_all_with_value(42)
        self.assertEqual(result, [test_list.get_at(0), test_list.get_at(5), test_list.get_at(8)],
                         "Testing: 'find_all_with_value'. Present multiple values")

    def test_find_all_with_value_value_not_presents(self):
        test_list = prepare_list()
        result = test_list.find_all_with_value(99)
        self.assertEqual(result, [],
                         "Testing: 'find_all_with_value'. Value not presents")

    # ---------------------------------------------------------------------------------------------

    def test_length_normal_list(self):
        test_list = prepare_list()
        result = test_list.length()
        self.assertEqual(result, 12,
                         "Testing: 'length'. Normal case")

    def test_length_empty_list(self):
        test_list = LinkedList()
        result = test_list.length()
        self.assertEqual(result, 0,
                         "Testing: 'length'. Empty list case")

    # ---------------------------------------------------------------------------------------------

    def test_insert_after_standard_node(self):
        test_list = prepare_list()
        test_list.insert_after(Node(36), test_list.get_at(1))
        self.assertEqual(test_list.to_values_list(), [42, 33, 36, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'insert_after'. Inserting node with a standard way")

    def test_insert_after_last_node(self):
        test_list = prepare_list()
        test_list.insert_after(Node(36), test_list.get_at(11))
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66, 36],
                         "Testing: 'insert_after'. Inserting node at last position")

    def test_insert_after_node_not_in_list(self):
        test_list = prepare_list()
        test_list.insert_after(Node(36), Node(42))
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'insert_after'. Inserting node after node not in list")

    # ---------------------------------------------------------------------------------------------

    def test_sum_lists_normal_case(self):
        list1 = prepare_list()
        list2 = prepare_list()
        result = LinkedList.sum_lists(list1, list2)
        self.assertEqual(result.to_values_list(), [84, 66, 22, 44, 30, 84, 20, 64, 84, 120, 140, 132],
                         "Testing: 'sum_lists'. Summarize two lists with same length")

    def test_sum_lists_different_length(self):
        list1 = prepare_list()
        list2 = prepare_list()
        list2.remove_with_value(33)
        result = LinkedList.sum_lists(list1, list2)
        self.assertEqual(result, None,
                         "Testing: 'sum_lists'. Summarize two lists with different length")

    def test_sum_lists_with_zero_length(self):
        list1 = LinkedList()
        list2 = LinkedList()
        result = LinkedList.sum_lists(list1, list2)
        self.assertEqual(result.to_values_list(), [],
                         "Testing: 'sum_lists'. Summarize two lists with zero length")


if __name__ == '__main__':
    unittest.main()