
class Fibonacci:
    def __init__(self):
        self.cache_solve = {}
        self.cache_0call = {}
        self.cache_1call = {}

    def fibonacci(self, n):
        if self.cache_solve.get(n, False):
            return self.cache_solve[n]

        if n == 0:
            self.cache_0call[0] = 1
            return 0
        elif n == 1:
            self.cache_1call[1] = 1
            return 1
        else:
            ret = self.fibonacci(n-1) + self.fibonacci(n-2)
            self.cache_solve[n] = ret
            self.cache_0call[n] = self.cache_0call.get(n-1, 0) + self.cache_0call.get(n-2, 0)
            self.cache_1call[n] = self.cache_1call.get(n-1, 0) + self.cache_1call.get(n-2, 0)
            return ret

    def solve(self, n):
        self.fibonacci(n)
        return (self.cache_0call.get(n, 0), self.cache_1call.get(n, 0))


def main():
    C = int(input())
    fib = Fibonacci()

    for _ in range(C):
        n = int(input())
        answer = fib.solve(n)
        print(" ".join([str(e) for e in answer]))
        

if __name__ == '__main__':
    main()   
