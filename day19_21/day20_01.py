from itertools import cycle
import time

lights = ['red','red-amber','green','amber']
timings = {'red': 3, 'red-amber': 1, 'green': 5, 'amber': 2}

traffic_lights = cycle(lights)

while True:
    current = next(traffic_lights)
    print(current)
    time.sleep(timings[current])
