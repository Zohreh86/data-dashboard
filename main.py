import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
jobs_posted = [120, 135, 148, 162, 170, 185, 201, 210]

plt.figure(figsize=(10, 6))
plt.plot(months, jobs_posted, marker="o", color="green", linewidth=2)
plt.fill_between(months, jobs_posted, alpha=0.1, color="skyblue")

plt.title("IT Job Postings in Saarland - 2024")
plt.xlabel("Month")
plt.ylabel("Number of Jobs")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("saarland_jobs.png")
plt.show()

print("Chart saved as saarland_jobs.png")