import numpy as np

year_temps = np.random.randint(10, 35, (12, 4, 7))  # (Months, Weeks, Days)

max_monthly = np.max(year_temps, axis=(1, 2))
min_monthly = np.min(year_temps, axis=(1, 2))
avg_monthly = np.mean(year_temps, axis=(1, 2))

print("Monthly Max Temperatures:\n", max_monthly)
print("\nMonthly Min Temperatures:\n", min_monthly)
print("\nMonthly Avg Temperatures:\n", avg_monthly)
