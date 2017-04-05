class Heap:
    def __init__(self):
        self.heap = list()
        self.heap.append(-1)

    def put(self, key):
        i = len(self.heap)
        parent = int(i/2)
        self.heap.append(key)

        while parent > 0:
            if self.heap[parent] >= key:
                break
            self.heap[i] = self.heap[parent]
            i = parent
            parent = int(i/2)

        self.heap[i] = key

    def delete_max(self):
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        N = len(self.heap)

        i = 1
        while 2*i + 1 < N:
            left  = 2*i
            right = left + 1
            bigger = left if self.heap[left] >= self.heap[right] else right

            if self.heap[bigger] <= self.heap[i]:
                break

            self.heap[bigger], self.heap[i] = self.heap[i], self.heap[bigger]
            i = bigger

        return self.get_heap()

    def max(self):
        return self.heap[1]

    def get_heap(self):
        return self.heap[1:]
