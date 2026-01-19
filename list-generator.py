print("== Generator and List in python memory comparision")

import sys
import time 

def get_memory_usage():
    import psutil, os
    return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

#using list(uses more memory)
print("Using list (eager loading..)")
start_mem = get_memory_usage()
start_time = time.time()

numbers_list = [x * 2 for x in range(10000) ]
sum_list = sum(numbers_list)
end_time = time.time()
end_mem = get_memory_usage()

print(f"Result :{sum_list}")
print(f"Time :{end_time-start_time:.2f}seconds")
print(f"Memory used :{end_mem-start_mem}MB")

del numbers_list
import gc; gc.collect()

#using generator 
print("\n Using generators ")
start_mem=get_memory_usage()
start_time=time.time()

numbers_gen =(x * 2 for x in range(10000))
sum_gen = sum(numbers_gen)
end_time=time.time()
end_mem=get_memory_usage()

print(f"Result :{sum_gen}")
print(f"Time : {end_time-start_time}seconds")
print(f"Memory used: {end_mem-start_mem}MB")

