import numpy as np

week_temps = np.random.randint(10, 35, 7)  # 1D Array: One city, one week
cities_week_temps = np.random.randint(10, 35, (3, 7))  # 2D Array: 3 cities, one week
cities_month_temps = np.random.randint(10, 35, (3, 4, 7))  # 3D Array: 3 cities, 4 weeks

assert week_temps.shape == (7,)
assert cities_week_temps.shape == (3, 7)
assert cities_month_temps.shape == (3, 4, 7)
assert week_temps.dtype == np.int32
assert cities_week_temps.dtype == np.int32
assert cities_month_temps.dtype == np.int32

print("1D Array (One city, One week):\n", week_temps)
print("\n2D Array (3 cities, One week):\n", cities_week_temps)
print("\n3D Array (3 cities, 4 weeks):\n", cities_month_temps)