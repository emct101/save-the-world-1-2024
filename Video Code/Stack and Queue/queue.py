# Queue

class Queue:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0 # boolean

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop(0)
    else:
      print("Pop from an empty stack")

  def peek(self):
    if not self.is_empty():
      return self.items[0]
    else:
      print("Empty stack")

  def size(self):
    return len(self.items)

# main
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.size())
print(queue.peek())
print(queue.pop())
print(queue.peek())

