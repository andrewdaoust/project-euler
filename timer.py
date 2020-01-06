from datetime import datetime
from problem010 import run  # Change this import to select the solution to time
import numpy as np

runs = 3
times = []

for i in range(runs):
    start = datetime.now()
    run()
    end = datetime.now()
    time = end - start
    times.append(time)
    print('Run {:02d}'.format(i+1), time)

print('Slowest:', max(times))
print('Fastest:', min(times))
print('Average:', np.mean(times))
