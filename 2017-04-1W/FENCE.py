class Fence:
    def __init__(self, N, string):
        self.N = N
        self.fences = [int(i) for i in string.split()]
        self.cache = dict()

    def max_rect(self):
        ret = max(self.N, max(self.fences))
        #print("ret: ", ret)
        N = self.N

        for i in range(N-1):
            first_fence = self.fences[i]
            #print("first: ", first_fence)
            second_fence = self.fences[i+1]
            #print("second: ", second_fence)

            height = min(first_fence, second_fence)
            if height == 1:
                continue

            idx = i + 2
            while idx <= N-1 and self.fences[idx] >= height:
                idx += 1

            #print("idx: ", idx)

            area = height * (idx - i)
            #print("area: ", area)
            if area > ret:
                ret = area

        return ret

    def find_max_continuous_fences(self, fence, height):
        ret = self.cache.get(height, None)
        if ret != None:
            return ret

        if fence == None:
            fence = self.fences

        ret = 0
        num = 0

        for i in range(self.N):
            if fence[i] >= height:
                num += 1
            else:
                ret = max(ret, num)
                num = 0
        ret = max(ret, num) # when for statement ends, update ret
        self.cache[height] = ret

        return ret

    def make_smaller_fence(self, fence, height):
        new_fence = list()
        is_continuous = False

        for f in fence:
            if f >= height:
                new_fence.append(f)
                is_continuous = True
            elif is_continuous:
                new_fence.append(0)
                is_continuous = False

        return new_fence

    def max_rect_fast(self):
        return foo(self.fences, 1, max(self.fences))

    def foo(self, fence, lo, hi):
        lo_fence_num = self.find_max_continuous_fences(fence, lo)
        hi_fence_num = self.find_max_continuous_fences(fence, hi)

        ret = hi * hi_fence_num
        if lo == hi or lo_fence_num == hi_fence_num or (hi-1)*lo_fence_num < ret:
            print("finished!!")
            return ret

        mid = int(hi / 2)
        return max(foo(self.make_smaller_fence(fence, lo), mid), foo(self.make_smaller_fence(fence, mid), hi))

def main():
    C = int(input())                 # num. of cases
    for _ in range(C):
        N = int(input())             # num. of fences
        f = Fence(N, input())        # heights of fences
        print(f.max_rect())

if __name__ == '__main__':
    main()
