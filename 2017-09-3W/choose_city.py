def distance(cities, index):
    this_coord = cities[index][0]

    total = 0
    for that_coord, that_num_people in cities:
        total += abs(that_coord - this_coord) * that_num_people

    return total

def chooseCity(n, cities):
    min_dist  = distance(cities, 0)
    min_coord = cities[0][0]

    for i, city in enumerate(cities):
        cand_dist  = distance(cities, i)
        cand_coord = city[0]

        if cand_dist < min_dist:
            min_dist  = cand_dist
            min_coord = cand_coord

        if cand_dist == min_dist and cand_coord < min_coord:
            min_coord = cand_coord

    return min_coord

def main():
    print(chooseCity(3,[[1,5],[2,2],[3,3]]))

if __name__ == '__main__':
    main()
