class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.length = 0

    def empty(self):
        return self.head is None

    def append(self, node: Node):
        if self.head is None:
            # We don't have leading element yet
            self.head = node
        else:
            self.get(self.length - 1).next = node

        self.length += 1

    def append_list(self, other):
        if self.head is None:
            self.head = other.head
        else:
            self.get(self.length - 1).next = other.head

        self.length += other.length

    def reverse(self):
        prev = None
        cur = self.head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def insert(self, node: Node, p: int):
        if p == 0:
            node.next = self.head
            self.head = node
            return

        prev = self.get(p - 1)
        node.next = prev.next
        prev.next = node
        self.length += 1

    def delete(self, p: int):
        if p == 0:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
            return

        prev = self.get(p - 1)
        to_remove = prev.next
        prev.next = to_remove.next
        to_remove.next = None

    def get(self, p: int) -> Node:
        current = self.head

        for _ in range(p):
            current = current.next

        return current

    def remove_idx(self):
        last_index = self.length - 1
        cur = self.head
        i = 0
        prev = None

        while cur != None:
            if cur.data == abs(i - last_index):
                if prev == None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur

            cur = cur.next
            i += 1

    def __str__(self):
        res = ""
        current = self.head
        while current is not None:
            res += f"{current} -> "
            current = current.next

        return res


if __name__ == '__main__':
    b = SinglyLinkedList()
    b.append(Node(1))
    b.append(Node(6))
    b.append(Node(2))
    b.append(Node(4))
    b.append(Node(3))
    b.append(Node(3))
    b.append(Node(1))
    b.append(Node(0))

    print("predi ignatius:", b)

    b.remove_idx()

    print("sled ignatius:", b)
