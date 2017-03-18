class Brackets2:
    def is_pair(string):
        index = 0
        N = len(string)

        br_buf = list()

        br_left  = ['(', '{', '[']
        br_right = [')', '}', ']']

        while index < N:
            print("index: ", index)
            ch = string[index]
            print("ch: ", ch)
            if ch in br_left:
                br_buf.append(ch)
            elif ch in br_right:
                i = br_left.index(br_buf.pop())
                if ch != br_right[i]:
                    return "NO"
            print("buf: ", br_buf)
            index = index + 1

        return "YES"



