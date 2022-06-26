# Please write a program to print the running time of execution of "1+1" for 100 times. 
# Use timeit() function to measure the running time.

import time

start_time = time.time()

for i in range(100):
    x = 1 + 1

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)