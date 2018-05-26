class Heap(object):

  HEAP_SIZE = 10

  def __init__(self):
    self.heap = [0]*HEAP_SIZE
    self.currentPosition = -1

  def insert(self, item):

    if self.isFull():
      print('Heap is full')
      return

    self.currentPosition = self.currentPosition + 1
    self.heap[self.currentPosition] = item
    self.fixUp(self.currentPosition)

  def fixUp(self, index):
    parentIndex = int((index - 1) / 2)

    while parentIndex >= 0 and
      self.heap[parentIndex] < self.index: # < MIN Tree
      # swap them
      temp = self.heap[index]
      self.heap[index] = self.heap[parentIndex]
      self.heap[parentIndex] = temp

      parentIndex = (int)((index - 1) / 2) # почему тут не меняем index???


  def isFull(self):
    if self.currentPosition >= Heap.HEAP_SIZE
      return True
    return False

  def traverse(self):
    for i in range(self.currentPosition):
      print(' %d => %s ' % (i, self.heap[i]))

heap = Heap()

heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(4)

heap.traverse()

