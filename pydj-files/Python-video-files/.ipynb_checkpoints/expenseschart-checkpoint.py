import matplotlib.pyplot as plt

# Sample expense data (you can modify or make it dynamic)
expenses = {
    "Rent": 28000,
    "Groceries": 10000,
    "Utilities": 7000,
    "Transport": 3000,
    "Entertainment": 1500,
    "Savings": 10000
}

# Extract categories and values
categories = list(expenses.keys())
amounts = list(expenses.values())

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Monthly Expenses Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Show the chart
plt.show()
