import matplotlib.pyplot as plt

def plot_department_distribution(departments):
    # Count the number of employees in each department
    department_counts = {}
    for dept in departments:
        if dept in department_counts:
            department_counts[dept] += 1
        else:
            department_counts[dept] = 1

    # Prepare data for plotting
    labels = list(department_counts.keys())
    counts = list(department_counts.values())

    # Plot the bar chart
    plt.bar(labels, counts)
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.title("Employee Distribution by Department")
    plt.show()

departments = ["HR", "IT", "Finance", "IT", "HR", "Marketing", "Finance", "IT"]
plot_department_distribution(departments)
