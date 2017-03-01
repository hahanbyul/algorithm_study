from SNAIL import SNAIL
import pytest

@pytest.mark.parametrize("n,m,prob", [
    (5, 4, 0.9960937500),
    (5, 3, 0.8437500000),
    (4, 2, 0.5625000000),
    (3, 2, 0.9375000000),
])

def test_example(n, m, prob):
    snail = SNAIL(m=m, n=n, rain_prob=0.75)
    assert abs(snail.start() - prob) <= 0.1 ** 7
