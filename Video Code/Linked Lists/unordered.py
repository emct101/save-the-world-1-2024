# linked lists

# unordered

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class UnorderedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head is None # boolean

  def add(self, item):
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node

  def remove(self, item):
    current = self.head
    prev = None
    found = False
    while current and not found:
      if current.data == item:
        found = True
      else:
        prev = current
        current = current.next
    if found:
      if prev is None:
        self.head = current.next
      else:
        prev.next = current.next

  def display(self):
    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next
    print()

# main
ulist = UnorderedList()

ulist.add(5)
ulist.add(2)
ulist.add(7)
ulist.add(1)

ulist.display()

ulist.remove(5)

ulist.display()
