from datetime import datetime
from importlib import import_module
import numpy as np


p_num = int(input('Enter problem number to time: '))
p_module = 'problem{:03d}'.format(p_num)
p = import_module(p_module)

# runs = 3
runs = int(input('Enter number of iterations to time: '))

print('\nTiming problem {0}. Running timer {1} time(s).'.format(p_num, runs))

times = []
for i in range(runs):
    start = datetime.now()
    p.run()
    end = datetime.now()
    time = end - start
    times.append(time)
    print('Run {:03d}'.format(i+1), time)

print('\n======== Stats ========')
print('Slowest:', max(times))
print('Fastest:', min(times))
print('Average:', np.mean(times))
# print('Std Dev:', np.std(times))
