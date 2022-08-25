from linkedlist import LinkedList,Node


class TestClass:
    link_list = LinkedList()

    def test_linked_list_instance(self):
        assert isinstance(self.link_list, LinkedList)

    def test_if_head_is_null(self):
        assert self.link_list.is_empty() is True

    def test_add_item(self):
        self.link_list.add_item(10)
        self.link_list.add_item(20)
        assert self.link_list.is_empty() is False

    def test_size(self):
        self.link_list.add_item(10)
        self.link_list.add_item(20)
        val_expected = 2
        assert self.link_list.size() == val_expected

    def test_if_item_exist(self):
        value = 20
        self.link_list.add_item(10)
        self.link_list.add_item(20)
        val_expected = True
        assert self.link_list.is_value_exist(value) == val_expected

    def test_remove_item(self):
        value = 30
        self.link_list.add_item(10)
        self.link_list.add_item(20)
        self.link_list.add_item(30)
        val_expected = True
        assert self.link_list.remove_item(value) == val_expected




