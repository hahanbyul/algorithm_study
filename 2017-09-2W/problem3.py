def add_count(x, x_dict):
    if not x in x_dict.keys():
        x_dict[x] = 1
    else:
        x_dict[x] = 2

def find1(x_dict):
    for key in x_dict.keys():
        if x_dict[key] == 1:
            return key

def solution(v):
    xs = dict()
    ys = dict()

    for point in v:
        x, y = point
        add_count(x, xs)
        add_count(y, ys)

    answer = [find1(xs), find1(ys)]
    return answer

