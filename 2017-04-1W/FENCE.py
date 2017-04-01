class Fence:
    def __init__(self, N, string):
        self.N = N
        self.fences = [int(i) for i in string.split()]

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

def main():
    C = int(input())                 # num. of cases
    for _ in range(C):
        N = int(input())             # num. of fences
        f = Fence(N, input())           # heights of fences
        print(f.max_rect())

if __name__ == '__main__':
    main()
