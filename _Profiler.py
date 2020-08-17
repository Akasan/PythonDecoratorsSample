from line_profiler import LineProfiler
import os
import sys
from tqdm import tqdm
import subprocess
from contextlib import redirect_stdout



class Profiler:
    PROFILE_TEMP_FOLDER = "./ProfilerTemp/"

    def __init__(self, func, *args, **kwargs):
        """
        Arguments:
        ----------
            func {function} -- function you want to profile
            args -- arguments of function

        Keyword Arguments:
        ------------------
            kwargs -- keyword arguments of function
        """
        self.profiler = LineProfiler()
        self.__func = func
        self.profiler.add_function(func)
        self.__args = args
        self.__kwargs = kwargs

    def execute(self, to_file=False, filename="profile_result.prof", iteration=1, is_stdout_none=False):
        """ execute function 

        Keyword Arguments:
        ------------------
            to_file {bool} -- set this as True when you want to save profile result to file (default: False)
            filename {str} -- file name of profile result (default: profile_result.prof)
            iteration {int} -- iteation for executing function (default: 1)
            is_stdout_none {bool} -- set this as True if you DON'T want to enable print function in specified function (default: False)
        """
        f = open(os.devnull, "w") if is_stdout_none else sys.stdout
        for i in range(iteration):
            if is_stdout_none:
                with redirect_stdout(open(os.devnull, "w")):
                    self.profiler.runcall(self.__func, *self.__args, **self.__kwargs)
            else:
                self.profiler.runcall(self.__func, *self.__args, **self.__kwargs)

        if to_file:
            self.profiler.dump_stats(filename)
        else:
            self.profiler.print_stats()


def hoge():
    print("hoge")

profiler = Profiler(hoge)
profiler.execute(iteration=100, is_stdout_none=True)
