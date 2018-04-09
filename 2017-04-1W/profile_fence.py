import cProfile
import random
from FENCE import Fence

fences = [str(random.randint(0, 10000 + 1)) for _ in range(20000)]
f1 = Fence(len(fences), " ".join(fences))

pr = cProfile.Profile()
pr.enable()

f1.max_rect()

pr.disable()
pr.print_stats(sort='time')

pr = cProfile.Profile()
pr.enable()

f1.max_rect_fast()

pr.disable()
pr.print_stats(sort='time')
