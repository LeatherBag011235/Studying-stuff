import numpy as np

year_temps = np.random.randint(10, 35, (12, 4, 7))  # (Months, Weeks, Days)

avg_monthly = np.mean(year_temps, axis=(1, 2))

# Identify hot and cold months
hot_months = np.where(avg_monthly > np.mean(avg_monthly) + 2)[0] + 1  # Months index from 1
cold_months = np.where(avg_monthly < np.mean(avg_monthly) - 2)[0] + 1

# Categorizing sports based on weather
sports_season = {
    "Winter Sports": cold_months.tolist(),
    "Summer Sports": hot_months.tolist(),
    "All-Weather Sports": list(set(range(1, 13)) - set(cold_months) - set(hot_months))
}

print(f"Hot Months: {hot_months}")
print(f"Cold Months: {cold_months}")
print("\nSports Categorization:")
for sport, months in sports_season.items():
    print(f"{sport}: {months}")
