# ordered

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class OrderedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head is None # boolean

  def add(self, item):
    new_node = Node(item)
    if self.is_empty() or item < self.head.data: # empty linked list
      new_node.next = self.head
      self.head = new_node
    else: # insert largest or in between
      curr = self.head
      while curr.next and item > curr.next.data:
        curr = curr.next
      new_node.next = curr.next
      curr.next = new_node

  def remove(self, item):
    curr = self.head
    prev = None
    found = False
    while curr and not found:
      if curr.data == item:
        found = True
      else:
        prev = curr
        curr = curr.next
    if found:
      if prev is None:
        self.head = curr.next
      else:
        prev.next = curr.next

  def display(self):
    curr = self.head
    while curr:
      print(curr.data, end=' ')
      curr = curr.next
    print()

# main
olist = OrderedList()

olist.add(5)
olist.add(2)
olist.add(7)
olist.add(1)

olist.display()

olist.remove(5)

olist.display()
