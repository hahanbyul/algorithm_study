from choose_city import distance
from choose_city import chooseCity

cities = [[1,5],[2,2],[3,3]]

def test_distance():
    assert distance(cities, 0) == 8
    assert distance(cities, 1) == 8
    assert distance(cities, 2) == 12

def test_ex():
    assert chooseCity(3, cities) == 1
