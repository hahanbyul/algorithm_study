class Fence:
    def __init__(self, N, string):
        self.N = N
        self.fences = [int(i) for i in string.split()]
        self.cache = dict()
        # self.cache_smaller_array = dict()

    def max_rect(self):
        ret = max(self.N, max(self.fences))
        # print("ret: ", ret)
        N = self.N

        for i in range(N-1):
            first_fence = self.fences[i]
            # print("first: ", first_fence)
            second_fence = self.fences[i+1]
            # print("second: ", second_fence)

            height = min(first_fence, second_fence)
            if height == 1:
                continue

            right_idx = i + 2
            while right_idx <= N-1 and self.fences[right_idx] >= height:
                right_idx += 1

            left_idx = i - 1
            while left_idx >= 0 and self.fences[left_idx] >= height:
                left_idx -= 1

            # print("right_idx: ", right_idx)
            # print("left_idx: ", left_idx)

            count = (right_idx - i) + (i - 1 - left_idx)
            area = height * count
            # print("area: ", area)
            if area > ret:
                ret = area

        return ret

    def find_max_continuous_fences(self, fence, height):
        ret = self.cache.get(height, None)
        if ret is not None:
            # print("cached!!")
            return ret

        if fence is None:
            fence = self.fences

        ret = 0
        num = 0

        for i in range(len(fence)):
            if fence[i] >= height:
                num += 1
            else:
                ret = max(ret, num)
                num = 0
        ret = max(ret, num)  # when for statement ends, update ret
        self.cache[height] = ret

        return ret

    def make_smaller_fence(self, fence, height):
        """
        ret = self.cache_smaller_array.get(height, None)
        if ret != None:
            return ret
        """

        new_fence = list()
        is_continuous = False

        for f in fence:
            if f >= height:
                new_fence.append(f)
                is_continuous = True
            elif is_continuous:
                new_fence.append(0)
                is_continuous = False

        # self.cache_smaller_array[height] = new_fence
        return new_fence

    def max_rect_fast(self):
        return self.foo(self.fences, 1, max(self.fences))

    def foo(self, fence, lo, hi):
        # print("fence: %s, lo: %d, hi: %d" % (fence, lo, hi))
        lo_fence_num = self.find_max_continuous_fences(fence, lo)
        hi_fence_num = self.find_max_continuous_fences(fence, hi)
        # print("lo_num: %d, hi_num: %d" % (lo_fence_num, hi_fence_num))

        ret = hi * hi_fence_num
        if lo == hi or lo_fence_num == hi_fence_num or (hi-1)*lo_fence_num < ret:
            return ret

        mid = lo + int((hi - lo) / 2)
        if mid <= lo:
            return max(lo*lo_fence_num, ret)

        # return max(self.foo(self.make_smaller_fence(fence, lo), lo, mid), self.foo(self.make_smaller_fence(fence, mid+1), mid+1, hi))
        return max(self.foo(self.fences, lo, mid), self.foo(self.fences, mid+1, hi))


def main():
    C = int(raw_input())                 # num. of cases
    for _ in range(C):
        N = int(raw_input())             # num. of fences
        f = Fence(N, raw_input())        # heights of fences
        print(f.max_rect_fast())
        # print f.max_rect_fast()
        # print f.max_rect()


if __name__ == '__main__':
    main()
