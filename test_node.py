from linkedlist import Node


class TestClass:
    def test_insert_value_in_node(self):
        val_insert = 10
        node = Node(val_insert)
        val_expect = 10
        assert node.get_value() == val_expect

    def test_next_node(self):
        val_insert = None
        node = Node(val_insert)
        val_expect = None
        assert node.get_value() == val_expect

    def test_next_node(self):
        val_insert = 10
        node = Node(val_insert)
        node2 = Node(val_insert+1)
        node.set_next(node2)

        val_expect = 11
        assert node.get_next().get_value() == val_expect


