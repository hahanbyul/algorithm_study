class Josephus:
    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.survivors = [i+1 for i in range(N)]

    def iterate2(self):
        ret = list()
        index = 0
        ret.append(self.survivors.pop(index))
        count = self.N-1

        while count > 0:
            print("survivors: ", self.survivors)
            index = (index + self.K % count) % count - 1
            if index == -1:
                index = index + count
            print("i: ", index)
            ret.append(self.survivors.pop(index))
            print("ret: ", ret)
            count = count - 1

        return ret
    
    def get_survivors(self):
        ret = list()
        index = 0
        self.survivors.pop(index)
        count = self.N-1

        while count > 2:
            index = (index + self.K % count) % count - 1
            if index == -1:
                index = index + count
                
            self.survivors.pop(index)
            count = count - 1

        return self.survivors

    def iterate(self):
        index = 0
        ret = list()
        count = self.N
        while index < self.N:
           ret.append(self.survivors[index])
           count = count - 1
           index = index + (self.K % self.N)
        return ret

    #def find_next(K):

def main():
    josephus = Josephus()
if __name__ == '__main__':
    main()
