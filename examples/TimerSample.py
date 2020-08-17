import sys
sys.path.append("../")
from DADecorator import Timer
import time

timer = Timer()

@timer.timer(iteration=10)
def sleep():
    time.sleep(0.1)

sleep()
# Average time : 0.10917820930480956
# Maximum time : 0.10947155952453613
# Minimum time : 0.10731720924377441
