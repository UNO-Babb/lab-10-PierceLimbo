#MapPlot.py
#Name: Pierce Limbo
#Date: 11/15/2025
#Assignment: Lab 10 Airline CORGIS
import airlines
import pandas as pd
import matplotlib.pyplot as plt

data = airlines.get_airports()
print("Total records:", len(data))

print("\nSample record keys:")
print(data[1].keys())  

try:
    print("\nNested 'Statistics' keys:")
    print(data[1]['Statistics'].keys())
except:
    print("eh something went weird here")

rows = []

for entry in data:
    stats = entry["Statistics"]
    delays = stats["Delays"]

    row = {
        "Airport": entry["Airport"]["Code"], 
        "Year": entry["Time"]["Year"],
        "Month": entry["Time"]["Month"],
        "Total Flights": stats["Flights"]["Total"],
        "Weather Delays": delays.get("Weather", 0),
        "Security Delays": delays.get("Security", 0),
        "NAS Delays": delays.get("National Air System", 0),
        "Late Aircraft Delays": delays.get("Late Aircraft", 0)
    }

    rows.append(row)

df = pd.DataFrame(rows)

print("\nDataFrame Maybe Looks Like This:")
print(df.head(7))  

df = df[df["Total Flights"] > -10] 

df = df[df["Weather Delays"] < 9000]

avg_weather = df.groupby("Year")["Weather Delays"].mean()

plt.figure(figsize=(10,4.8))  
plt.plot(avg_weather.index, avg_weather.values, linewidth=2)  
plt.title("Average Weather Delays By Year (kinda rough estimate)")
plt.xlabel("Year Maybe")
plt.ylabel("Avg Delay Count-ish")
plt.grid(True)
plt.tight_layout()
plt.show()

delay_totals = {
    "Weather": df["Weather Delays"].sum(),
    "Security": df["Security Delays"].sum(),
    "NAS": df["NAS Delays"].sum(),
    "Late Aircraft": df["Late Aircraft Delays"].sum()
}

plt.figure(figsize=(8.7,5))
plt.bar(delay_totals.keys(), delay_totals.values())
plt.title("Total U.S. Flight Delays (All Time-ish)")
plt.ylabel("Total Delays?")
plt.tight_layout()
plt.show()

print("\nYo check out this data... pretty wild honestly.")
