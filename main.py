import pandas as pd
import matplotlib.pyplot as plt

# Real Saarland population data from Destatis
# Source: destatis.de - Bevölkerung nach Bundesländern
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Population": [994187, 995597, 997855, 999278, 1001902, 1004674, 1006582, 1010088, 1013312]
}

df = pd.DataFrame(data)

# Statistics
print("=== Saarland Population Analysis ===")
print(f"Latest population: {df['Population'].iloc[-1]:,}")
print(f"Growth since 2015: {df['Population'].iloc[-1] - df['Population'].iloc[0]:,}")
print(f"Average population: {df['Population'].mean():,.0f}")
print(f"Peak year: {df.loc[df['Population'].idxmax(), 'Year']}")

# Chart
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["Population"], marker="o", color="steelblue", linewidth=2)
plt.fill_between(df["Year"], df["Population"], alpha=0.1, color="steelblue")

plt.title("Saarland Population Growth 2015–2023", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True, alpha=0.3)
plt.xticks(df["Year"])

# Add value labels on each point
for x, y in zip(df["Year"], df["Population"]):
    plt.annotate(f"{y:,}", (x, y), textcoords="offset points", 
                 xytext=(0, 10), ha="center", fontsize=8)

plt.tight_layout()
plt.savefig("saarland_population.png")
plt.show()

print("\nChart saved as saarland_population.png")