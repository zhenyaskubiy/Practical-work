import numpy as np
import timeit

array_size = 10000
n_largest = 5

arr = np.random.randint(0, 1000, size=array_size)

def argsort_method():
    return np.sort(arr)[-n_largest:]

def argpartition_method():
    return np.partition(arr, -n_largest)[-n_largest:]

time_argsort = timeit.timeit(stmt=argsort_method, number=1000)
time_argpartition = timeit.timeit(stmt=argpartition_method, number=1000)

print("Час виконання за допомогою np.argsort():", time_argsort)
print("Час виконання за допомогою np.argpartition():", time_argpartition)
