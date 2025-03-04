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

# Old laptop win 10:
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

# PC win 11 Turbo Boost:
# recursion: 0.00636 sec
# integer_operations: 0.61755 sec
# float_operations: 0.45269 sec
# string_operations: 0.00000 sec
# numpy_operations: 0.51573 sec
# numpy_sort: 0.55932 sec
# pandas_dataframe_operations: 0.03172 sec
# pandas_merge: 0.01612 sec
# write_csv: 4.80030 sec
# read_csv: 0.66628 sec
# write_json: 1.89160 sec
# read_json: 0.45064 sec
# parallel_processing: 0.85410 sec

# Summary statistics (percentage change from Old Laptop Win 10)
# -------------------------------------------------------------------------------------------------------------
# Task                          | PC Win 11 No Turbo Boost (sec) | Old Laptop Win 10 (sec) | PC Win 11 Turbo Boost (sec) | % Change (PC Win 11 No Turbo Boost) | % Change (PC Win 11 Turbo Boost)
# -------------------------------------------------------------------------------------------------------------
# recursion                     |          0.01008              |          0.20766        |          0.00636            |       -95.15%                        |       -96.94%                    
# integer_operations            |          1.12527              |          1.97350        |          0.61755            |       -42.98%                        |       -68.71%                    
# float_operations              |          0.84567              |          1.59820        |          0.45269            |       -47.09%                        |       -71.68%                    
# string_operations             |          0.00332              |          0.00222        |          0.00000            |       +49.55%                        |      -100.00%                    
# numpy_operations              |          0.99063              |          5.44708        |          0.51573            |       -81.81%                        |       -90.53%                    
# numpy_sort                    |          1.04368              |          1.42523        |          0.55932            |       -26.77%                        |       -60.76%                    
# pandas_dataframe_operations   |          0.04783              |          0.12676        |          0.03172            |       -62.27%                        |       -74.98%                    
# pandas_merge                  |          0.03500              |          0.07176        |          0.01612            |       -51.23%                        |       -77.54%                    
# write_csv                     |          8.61298              |         20.31220        |          4.80030            |       -57.60%                        |       -76.37%                    
# read_csv                      |          1.17074              |          2.76231        |          0.66628            |       -57.62%                        |       -75.88%                    
# write_json                    |          3.42012              |          5.62816        |          1.89160            |       -39.23%                        |       -66.39%                    
# read_json                     |          0.77391              |          1.91254        |          0.45064            |       -59.53%                        |       -76.44%                    
# parallel_processing           |          1.56115              |          1.88637        |          0.85410            |       -17.24%                        |       -54.72%                    
