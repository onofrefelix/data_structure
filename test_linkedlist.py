from linkedlist import LinkedList


class TestClass:
    link_list = LinkedList()

    def test_linked_list_instance(self):
        assert isinstance(self.link_list, LinkedList)

    def test_if_head_is_null(self):
        assert link_list.get_head() is None
