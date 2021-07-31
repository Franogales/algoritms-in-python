# this is an example of linear time
import numpy as np
import time
class BigOn:
    def iteration()-> None:
        tic = time.perf_counter()
        array = np.full(100000,"paco")
        
        for n in array:
            print(n)
        toc = time.perf_counter()

        print(toc-tic)

BigOn.iteration()