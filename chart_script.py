
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find employees.csv in the same folder as this script
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "employees.csv")

# Check the required columns
required_columns = {"id", "department", "salary"}

if not required_columns.issubset(df.columns):
    raise ValueError(
        f"CSV columns found: {list(df.columns)}. "
        "Expected: id, department, salary."
    )

df["id"] = pd.to_numeric(df["id"], errors="raise")
df["salary"] = pd.to_numeric(df["salary"], errors="raise")

# Chart 1: Average salary by department
avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
bars = plt.bar(avg_salary.index, avg_salary.values)
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.bar_label(bars, fmt="%.2f", padding=3)
plt.tight_layout()
plt.savefig(BASE_DIR / "average_salary_bar.png", dpi=300)
plt.close()

# Chart 2: Salary distribution
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, edgecolor="black")
plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig(BASE_DIR / "salary_histogram.png", dpi=300)
plt.close()

# Chart 3: Employee ID versus salary
plt.figure(figsize=(8, 5))

for department, group in df.groupby("department"):
    plt.scatter(
        group["id"],
        group["salary"],
        label=department,
        s=80
    )

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig(BASE_DIR / "employee_scatter.png", dpi=300)
plt.close()

# Chart 4: Monthly sales line chart (sample data)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales (Jan-Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(BASE_DIR / "monthly_sales_line.png", dpi=300)
plt.close()

print("All four charts were saved successfully!")
print("1. average_salary_bar.png")
print("2. salary_histogram.png")
print("3. employee_scatter.png")
print("4. monthly_sales_line.png")
