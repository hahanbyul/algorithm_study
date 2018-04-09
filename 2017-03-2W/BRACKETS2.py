class Brackets2:
    def is_pair(self, string):
        index = 0
        N = len(string)

        br_buf = list()

        br_left  = ['(', '{', '[']
        br_right = [')', '}', ']']

        while index < N:
            #print("index: ", index)
            ch = string[index]
            #print("ch: ", ch)
            if ch in br_left:
                br_buf.append(ch)
            elif ch in br_right:
                if len(br_buf) == 0:
                    return "NO" 

                i = br_left.index(br_buf.pop())
                if ch != br_right[i]:
                    return "NO"
            #print("buf: ", br_buf)
            index = index + 1

        return "YES" if len(br_buf) == 0 else "NO"

def main():
    br = Brackets2()
    C = int(input())
    for i in range(C):
        print(br.is_pair(input()))
    
if __name__ == '__main__':
        main()
