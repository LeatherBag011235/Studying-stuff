import numpy as np

cities_month_temps = np.random.randint(10, 35, (3, 4, 7))

max_country = np.max(cities_month_temps)
min_country = np.min(cities_month_temps)
avg_country = np.mean(cities_month_temps)

print(f"Country-Level Statistics:\nMax: {max_country}, Min: {min_country}, Avg: {avg_country:.2f}")
