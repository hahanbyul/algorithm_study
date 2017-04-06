import heapq

class Fast_median():
    def __init__(self):
        self.min_heap = list() # bigger
        self.median = None
        self.max_heap = list() # smaller

    def put(self, key):
        if self.median == None:
            self.median = key
            return

        if key >= self.median:
            self.push_min_heap(key)
            if self.is_stable():
                return
            else: # min_heap_size == max_heap_size + 2:
                self.push_max_heap(self.median)
                self.median = self.pop_min_heap()
                return
        else:
            self.push_max_heap(key)
            if self.is_stable():
                return
            else: # min_heap_size + 1 == max_heap_size:
                self.push_min_heap(self.median)
                self.median = self.pop_max_heap()
                return

    def push_min_heap(self, key):
        heapq.heappush(self.min_heap, key)
        return

    def push_max_heap(self, key):
        heapq.heappush(self.max_heap, -key)
        return

    def pop_min_heap(self):
        return heapq.heappop(self.min_heap)

    def pop_max_heap(self):
        return -heapq.heappop(self.max_heap)
            
    def is_stable(self):
        diff = len(self.min_heap) - len(self.max_heap)
        return True if diff == 1 or diff == 0 else False

def generator(a, b):
    A = 1983
    yield A
    while True:
        A = (A*a + b) % 20090711
        yield A

def main():
    C = int(input())                 # num. of cases
    for _ in range(C):
        N, a, b = [int(i) for i in input().split()]

        fast_me = Fast_median()
        gen = generator(a, b)

        part_sum = 0
        for _ in range(N):
            fast_me.put(gen.__next__())
            #print("bigger:  ", fast_me.min_heap)
            #print("smaller: ", fast_me.max_heap)
            #print("median:  ", fast_me.median)
            part_sum += fast_me.median
        print(part_sum % 20090711)

if __name__ == '__main__':
    main()
