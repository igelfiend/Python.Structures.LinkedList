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
    def test_add_first_element(self):
        test_list = LinkedList()
        node = Node(42)
        test_list.add_in_tail(node)
        self.assertEqual(test_list.len(), 1,
                         "Testing: 'add_it_tail'. Incorrect list size")
        self.assertEqual(test_list.head, node,
                         "Testing: 'add_it_tail'. Bad head pointer")
        self.assertEqual(test_list.tail, node,
                         "Testing: 'add_it_tail'. Bad tail pointer")

    # ---------------------------------------------------------------------------------------------

    def test_delete_node_present_once(self):
        test_list = prepare_list()
        test_list.delete(11)
        self.assertEqual(test_list.to_values_list(), [42, 33, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'delete'. Value in list presents ones")

    def test_delete_node_present_multiple(self):
        test_list = prepare_list()
        test_list.delete(42)
        self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'delete'. Value in list presents multiple times")

    def test_delete_node_which_not_present(self):
        test_list = prepare_list()
        test_list.delete(99)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'delete'. Value in list not present")

    def test_delete_node_at_last_position(self):
        test_list = prepare_list()
        test_list.delete(66)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70],
                         "Testing: 'delete'.Value in list removed from tail")

    def test_delete_node_at_head(self):
        test_list = prepare_list()
        test_list.delete(42)
        self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'delete'. Value in list removed from head")

    def test_delete_node_from_list_with_1_element(self):
        test_list = LinkedList()
        test_list.add_in_tail(Node(42))
        test_list.delete(42)
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'delete'. Trying to remove from list with single element. Different arrays size")
        self.assertIs(test_list.head, None,
                      "Testing: 'delete'. Trying to remove from list with single element. Head pointer is not empty")
        self.assertIs(test_list.tail, None,
                      "Testing: 'delete'. Trying to remove from list with single element. Tail pointer is not empty")

    def test_delete_node_from_empty_list(self):
        test_list = LinkedList()
        test_list.delete(12)
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'delete'. Trying to remove from empty list")
        self.assertIs(test_list.head, None,
                      "Testing: 'delete'. Trying to remove from empty list. Head pointer is not empty")
        self.assertIs(test_list.tail, None,
                      "Testing: 'delete'. Trying to remove from empty list. Tail pointer is not empty")

    # ---------------------------------------------------------------------------------------------

    def test_delete_all_nodes_present_once(self):
        test_list = prepare_list()
        test_list.delete(15, all=True)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'delete' with all entries. Value in list present once")

    def test_delete_all_nodes_present_multiple(self):
        test_list = prepare_list()
        test_list.delete(42, all=True)
        self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 10, 32, 60, 70, 66],
                         "Testing: 'delete' with all entries. Value in list present multiple")

    def test_delete_all_nodes_node_at_last_position(self):
        test_list = prepare_list()
        test_list.delete(66, all=True)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70],
                         "Testing: 'delete' with all entries. Value deleted at last position")

    def test_delete_all_nodes_comes_one_by_one_at_last_positions(self):
        test_list = prepare_list()
        test_list.add_in_tail(Node(66))
        test_list.delete(66, all=True)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70],
                         "Testing: 'delete' with all entries. Value deleted which comes one by one at last positions")

    def test_delete_all_nodes_comes_one_by_one_at_first_positions(self):
        test_list = prepare_list()
        node = test_list.find(42)
        test_list.insert(node, Node(42))
        test_list.delete(42, all=True)
        self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 10, 32, 60, 70, 66],
                         "Testing: 'delete' with all entries. Value deleted which comes one by one at last positions")

    def test_delete_all_nodes_comes_one_by_one_at_center_positions(self):
        test_list = prepare_list()
        node = test_list.find(15)
        test_list.insert(node, Node(15))
        test_list.delete(15, all=True)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'delete' with all entries. Value deleted which comes one by one at last positions")

    # ---------------------------------------------------------------------------------------------

    def test_clean_with_normal_list(self):
        test_list = prepare_list()
        test_list.clean()
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'clean'. List must be empty")

    def test_clean_with_empty_list(self):
        test_list = LinkedList()
        test_list.clean()
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'clean'. List must be empty")

    # ---------------------------------------------------------------------------------------------

    def test_find_all_one_value(self):
        test_list = prepare_list()
        result = test_list.find_all(33)
        self.assertEqual(result, [test_list.get_at(1)],
                         "Testing: 'find_all'. Present one value")

    def test_find_all_multiple_values(self):
        test_list = prepare_list()
        result = test_list.find_all(42)
        self.assertEqual(result, [test_list.get_at(0), test_list.get_at(5), test_list.get_at(8)],
                         "Testing: 'find_all'. Present multiple values")

    def test_find_all_value_not_presents(self):
        test_list = prepare_list()
        result = test_list.find_all(99)
        self.assertEqual(result, [],
                         "Testing: 'find_all'. Value not presents")

    # ---------------------------------------------------------------------------------------------

    def test_length_normal_list(self):
        test_list = prepare_list()
        result = test_list.len()
        self.assertEqual(result, 12,
                         "Testing: 'len'. Normal case")

    def test_length_empty_list(self):
        test_list = LinkedList()
        result = test_list.len()
        self.assertEqual(result, 0,
                         "Testing: 'len'. Empty list case")

    # ---------------------------------------------------------------------------------------------

    def test_insert_standard_node(self):
        test_list = prepare_list()
        test_list.insert(test_list.get_at(1), Node(36))
        self.assertEqual(test_list.to_values_list(), [42, 33, 36, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'insert'. Inserting node with a standard way")

    def test_insert_node_after_first_element(self):
        test_list = prepare_list()
        test_list.insert(test_list.get_at(0), Node(36))
        self.assertEqual(test_list.to_values_list(), [42, 36, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'insert'. Inserting node with a standard way")

    def test_insert_node_after_last_element(self):
        test_list = prepare_list()
        test_node = Node(36)
        test_list.insert(test_list.get_at(11), test_node)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66, 36],
                         "Testing: 'insert'. Inserting node at last position")
        self.assertEqual(test_list.tail, test_node,
                         "Testing: 'insert'. Tail pointer incorrect.")

    def test_insert_node_not_in_list(self):
        test_list = prepare_list()
        test_list.insert(Node(36), Node(42))
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66],
                         "Testing: 'insert'. Inserting node after node not in list")

    def test_insert_node_in_empty_list(self):
        test_list = LinkedList()
        test_node = Node(42)
        test_list.insert(None, test_node)
        self.assertEqual(test_list.to_values_list(), [42],
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after None element.\n"
                         "Values error")
        self.assertEqual(test_node, test_list.head,
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after None element.\n"
                         "Bad head pointer")
        self.assertEqual(test_node, test_list.tail,
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after None element.\n"
                         "Bad tail pointer")

    def test_insert_node_in_empty_list_incorrect_usage(self):
        test_list = LinkedList()
        test_node = Node(42)
        test_list.insert(test_node, test_node)
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after not None element.\n"
                         "Values error")

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
        list2.delete(33)
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
