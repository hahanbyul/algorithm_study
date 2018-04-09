def get_initial_array(goal):
    i = 1
    summed = 0
    array = []

    while summed < goal:
        array.append(i)
        summed += i
        i += 1

    return array, summed

def move_right(array, summed):
    left  = array.pop(0)
    right = array[-1] + 1
    array.append(right)

    return summed - left + right

def solve_(array, summed, goal):
    if len(array) == 1:
        return 1

    while summed < goal:
        summed = move_right(array, summed)

    answer = solve_(array[:-1], summed - array[-1], goal)
    if summed == goal:
        # print(array)
        answer += 1

    return answer

def expressions(goal):
    array, summed = get_initial_array(goal)
    answer = solve_(array[:-1], summed - array[-1], goal)
    if summed == goal:
        # print(array)
        answer += 1

    return answer
