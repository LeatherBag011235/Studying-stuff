import numpy as np

week_temps = np.random.randint(10, 35, 7)
cities_week_temps = np.random.randint(10, 35, (3, 7))
cities_month_temps = np.random.randint(10, 35, (3, 4, 7))

max_week = np.max(week_temps)
min_week = np.min(week_temps)
avg_week = np.mean(week_temps)

max_cities_week = np.max(cities_week_temps, axis=1)
min_cities_week = np.min(cities_week_temps, axis=1)
avg_cities_week = np.mean(cities_week_temps, axis=1)
print(avg_cities_week)

max_cities_month = np.max(cities_month_temps, axis=(1, 2))
min_cities_month = np.min(cities_month_temps, axis=(1, 2))
avg_cities_month = np.mean(cities_month_temps, axis=(1, 2))

print(f"One City (Week) - Max: {max_week}, Min: {min_week}, Avg: {avg_week:.2f}")
print(f"\nPer City (3 Cities, 1 Week) - Max:\n{max_cities_week}")
print(f"\nMin:\n{min_cities_week}")
print(f"\nAvg:\n{avg_cities_week}")

print(f"\nPer City (3 Cities, 4 Weeks) - Max:\n{max_cities_month}")
print(f"\nMin:\n{min_cities_month}")
print(f"\nAvg:\n{avg_cities_month}")
