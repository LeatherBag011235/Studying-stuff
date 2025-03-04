import time
import numpy as np
import pandas as pd
import multiprocessing
from multiprocessing import Pool
import json


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.5f} sec")
        return result
    return wrapper

# CPU TESTS
@timer
def nested_loops():
    total = 0
    for i in range(1000):
        for j in range(1000):
            total += i * j
    return total

@timer
def recursion(n):
    if n == 0:
        return 1
    return n * recursion(n - 1)

@timer
def integer_operations():
    total = sum(i * i for i in range(10**7))
    return total

@timer
def float_operations():
    total = sum(i * 0.5 for i in range(10**7))
    return total

@timer
def string_operations():
    s = "abc" * 10**6
    return s[::-1]

# NUMPY TESTS
@timer
def numpy_operations():
    a = np.random.rand(5000, 5000)
    b = np.random.rand(5000, 5000)
    return np.dot(a, b)

@timer
def numpy_sort():
    a = np.random.rand(10**7)
    return np.sort(a)

# PANDAS TESTS
@timer
def pandas_dataframe_operations():
    df = pd.DataFrame({
        'A': np.random.rand(10**6),
        'B': np.random.rand(10**6),
        'C': np.random.randint(0, 100, 10**6)
    })
    return df.groupby('C').agg({'A': 'mean', 'B': 'sum'})

@timer
def pandas_merge():
    df1 = pd.DataFrame({'key': np.arange(10**6), 'value': np.random.rand(10**6)})
    df2 = pd.DataFrame({'key': np.arange(10**6), 'value2': np.random.rand(10**6)})
    return pd.merge(df1, df2, on='key')

# FILE I/O TESTS
@timer
def write_csv():
    df = pd.DataFrame(np.random.rand(10**6, 10))
    df.to_csv("test.csv", index=False)

@timer
def read_csv():
    df = pd.read_csv("test.csv")
    return df

@timer
def write_json():
    data = {str(i): np.random.rand() for i in range(10**6)}
    with open("test.json", "w") as f:
        json.dump(data, f)

@timer
def read_json():
    with open("test.json", "r") as f:
        data = json.load(f)
    return data

# MULTIPROCESSING TEST
def square(x):  # Move this outside the function
    return x * x

@timer
def parallel_processing():
    with Pool(multiprocessing.cpu_count()) as p:
        result = p.map(square, range(10**6))
    return result

if __name__ == "__main__":
    nested_loops()
    recursion(100)
    integer_operations()
    float_operations()
    string_operations()
    numpy_operations()
    numpy_sort()
    pandas_dataframe_operations()
    pandas_merge()
    write_csv()
    read_csv()
    write_json()
    read_json()
    parallel_processing()



# PC win 11 No Turbo boost:
# recursion: 0.01008 sec
# integer_operations: 1.12527 sec
# float_operations: 0.84567 sec
# string_operations: 0.00332 sec
# numpy_operations: 0.99063 sec
# numpy_sort: 1.04368 sec
# pandas_dataframe_operations: 0.04783 sec
# pandas_merge: 0.03500 sec
# write_csv: 8.61298 sec
# read_csv: 1.17074 sec
# write_json: 3.42012 sec
# read_json: 0.77391 sec
# parallel_processing: 1.56115 sec

# Old laptop win 11:
# recursion: 0.20766 sec
# integer_operations: 1.97350 sec
# float_operations: 1.59820 sec
# string_operations: 0.00222 sec
# numpy_operations: 5.44708 sec
# numpy_sort: 1.42523 sec
# pandas_dataframe_operations: 0.12676 sec
# pandas_merge: 0.07176 sec
# write_csv: 20.31220 sec
# read_csv: 2.76231 sec
# write_json: 5.62816 sec
# read_json: 1.91254 sec
# parallel_processing: 1.88637 sec