from math import log2
from math import inf
from math import ceil

class Heap:
    def __init__(self):
        self.heap = list()
        self.heap.append(inf)

    def generator(self, a, b):
        A = 1983
        yield A
        while True:
            A = (A*a + b) % 20090711
            yield A

    def put_inorder(self, key):
        N = len(self.heap)
        self.put(key)

        i = N
        parent = int(i/2)
        while i >= 2:
            #print("i: ", i, ", heal[i]", self.heap[i])
            while self.heap[i-1] < self.heap[i]:
                self.heap[i-1], self.heap[i] = self.heap[i], self.heap[i-1]
                i -= 1
            i = parent
            parent = int(i/2)

    def get_median(self):
        #print(self.heap)
        med_idx = ceil(len(self.heap) / 2)
        #print(self.heap[med_idx])
        return self.heap[med_idx]

    def put(self, key):
        N = len(self.heap)
        i = N
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

def main():
    C = int(input())                 # num. of cases
    for _ in range(C):
        N, a, b = [int(i) for i in input().split()]

        h = Heap()
        gen = h.generator(a, b)

        part_sum = 0
        for _ in range(N):
            h.put_inorder(gen.__next__())
            part_sum += h.get_median()
        print(part_sum % 20090711)

if __name__ == '__main__':
    main()
