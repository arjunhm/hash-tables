from exceptions import KeyError

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"


class ChainingNode(Node):

    def __init__(self, key, value):
        super().__init__(key, value)
        self.next = None


class LPNode(Node):

    def __init__(self, key, value):
        super().__init__(key, value)
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True


class LinkedList:
    def __init__(self, key=None, value=None):
        if key and value:
            node = ChainingNode(key, value)
        else:
            node = None
        self.head = node

    def get(self, key, default=None):
        head = self.head
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return default

    def insert(self, key, value):
        node = ChainingNode(key, value)

        # No head
        if self.head is None:
            self.head = node
            return

        head = self.head
        while head.next is not None:
            # * Update operation
            if head.key == key:
                head.value = value
                return
            head = head.next
        head.next = node

    def delete(self, key):

        # No head
        if self.head is None:
            raise KeyError

        head = self.head
        previous_node = None

        # If head is to be deleted
        if head.key == key:
            self.head = head.next
            return

        # If two nodes
        if head.next is not None and head.next.key == key and head.next is None:
            self.head = head.next
            return

        while head is not None:
            if head.key == key:
                break

            previous_node = head
            head = head.next

        if head is None:
            raise KeyError

        if previous_node is not None:
            previous_node.next = head.next
            head.next = None

    def display(self):
        output_string = self.return_display()
        print(output_string)

    def return_display(self):
        if self.head is None:
            return ""
        head = self.head
        output_string = f"{head} -> "
        while head.next is not None:
            head = head.next
            node = f"{head}"
            if head.next is None:
                output_string += node
            else:
                output_string += f"{node} -> "
        return output_string
