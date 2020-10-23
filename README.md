# PythonDecoratorsSample

## Description
This repo provides some useful decorators (some methods are not implemented as decorator).


## Install
You can install this module like this

```
pip install .
```

## How To Use
### Profiler
```python
from DADecorator import Profiler
import time

def hoge(x):
    print(x)
    time.sleep(1.0)


if __name__ == "__main__":
    profiler = Profiler(hoge, x=10)
    profiler.execute(iteration=10)
```

This output will be following.
```
10
10
10
10
10
10
10
10
10
10
Timer unit: 1e-07 s

Total time: 10.0332 s
File: ProfilerTest.py
Function: hoge at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           def hoge(x):
     6        10       4405.0    440.5      0.0      print(x)
     7        10  100327495.0 10032749.5    100.0      time.sleep(1.0)
```

If you don't want to print any result of function, you only set `is_stdout_none` as True
```python
profiler.execute(iteration=10, is_stdout_none=True)
```
