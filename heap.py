class Heap(object):

  HEAP_SIZE = 10

  def __init__(self):
    self.heap = [0] * self.HEAP_SIZE
    self.currentPosition = -1

  def insert(self, item):

    if self.isFull():
      print('Heap is full')
      return

    self.currentPosition = self.currentPosition + 1
    self.heap[self.currentPosition] = item
    self.fixUp(self.currentPosition)

  def fixUp(self, index):
    childIndex = index
    parentIndex = int((index - 1) / 2)

    while (parentIndex >= 0 and
      self.heap[parentIndex] < self.heap[childIndex]): # < MAX Tree
      # swap them
      print('swap %s <> %s' % (self.heap[parentIndex], self.heap[childIndex]))
      temp = self.heap[childIndex]
      self.heap[childIndex] = self.heap[parentIndex]
      self.heap[parentIndex] = temp

      childIndex, parentIndex = parentIndex, (int)((parentIndex - 1) / 2)

  def isFull(self):
    if self.currentPosition >= self.HEAP_SIZE:
      return True
    return False

  def traverse(self):
    for i in range(self.currentPosition + 1):
      print(' %d => %s ' % (i, self.heap[i]))

heap = Heap()

heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(4)
heap.insert(50)
heap.insert(7)

heap.traverse()

