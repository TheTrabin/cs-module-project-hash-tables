class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} -->'
            curr = curr.next

        return currStr

    def find(self, value):
        # return node w/ value
        # runtinme: O(n) - n = number of nodes
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # deletes node w /given value then returns that node
    # runtime: O(n) where n = number of nodes
    def delete(self, value):
        curr = self.head

        # special case for Head delete
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    #insert node at head of list
    # runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    #overwtire node or insert node at head
    #runtime: O(n)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value) # O(n)
        if existingNode !=None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node) # O(1)



a = Node(1)
b = Node(2)
c = Node(3)

ll = LinkedList()

# ll.insert_at_head()
ll.insert_at_head(c)
ll.insert_at_head(b)
ll.insert_at_head(a)
ll.insert_at_head_or_overwrite(c)
ll.delete(3)
print(ll)