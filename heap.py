class Heap(object): # MAX heap

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

  # O(logN)
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

  # O(logN)
  def fixDown(self, index, size):
    parentIndex = index
    leftChildIndex = parentIndex * 2 + 1
    rightChildIndex = parentIndex * 2 + 2

    while (parentIndex < size):

      # ищем сначала возможные индексы детей, для проверки с родителем
      if leftChildIndex <= size: # проверяем, что левый ребенок в границе
        swapChildIndex = None

        if rightChildIndex > size: # если правый ребенок за границей- исключаем его
          swapChildIndex = leftChildIndex
        else: # проверяем какой из детей МАХ, т.к. дерево максимальное
          if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
            swapChildIndex = leftChildIndex # левый ребенок больше
          else:
            swapChildIndex = rightChildIndex # правый больше

        if self.heap[parentIndex] < self.heap[swapChildIndex]: # родитель < ребенка, это нарушает правило Максимальной пирамиды => нужно поменять их местами
          temp = self.heap[parentIndex]
          self.heap[parentIndex] = self.heap[swapChildIndex]
          self.heap[swapChildIndex] = temp
        else: # иначе - пирамида правильная => выходим !
          break
      else: # левый ребенок за границе => выходим !
        break

      parentIndex = swapChildIndex
      leftChildIndex = parentIndex * 2 + 1
      rightChildIndex = parentIndex * 2 + 2


  # O(N * log(N) = O(N))
  def heapsort(self):
    print('heapSort!')
    sortedArray = []
    heap = self.heap

    for i in range(self.currentPosition + 1):
      print(self.heap[0])
      temp = self.heap[0]
      self.heap[0] = self.heap[self.currentPosition - i]
      self.heap[self.currentPosition - i] = temp
      self.fixDown(0, self.currentPosition - i - 1) # -1 т.к. не трогаем уже предпоследний элемент

    print('END heapsort')

  def isFull(self):
    if self.currentPosition >= self.HEAP_SIZE:
      return True
    return False

  def traverse(self):
    for i in range(self.currentPosition + 1):
      print(' %d => %s ' % (i, self.heap[i]))

heap = Heap() # MAX heap

heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(4)
heap.insert(50)
heap.insert(7)
heap.heapsort()

for i in range(heap.currentPosition + 1):
  heap.fixUp(heap.currentPosition - i)

heap.traverse()




