def generate_employee_report(employees):
    # Title
    report_title = "Employee Report"
    print(report_title)
    print("=" * len(report_title))

    # Total number of employees
    total_employees = len(employees)
    print(f"Total Employees: {total_employees}")

    # Department counts
    dept_counts = {}
    for emp in employees:
        dept = emp["department"]
        if dept not in dept_counts:
            dept_counts[dept] = 0
        dept_counts[dept] += 1

    print("\nDepartments:")
    for dept, count in dept_counts.items():
        print(f"  {dept}: {count}")

    # Average tenure
    if total_employees > 0:
        total_tenure = sum(emp["tenure"] for emp in employees)
        average_tenure = total_tenure / total_employees
    else:
        average_tenure = 0

    print(f"\nAverage Tenure: {average_tenure:.2f} years")


employees = [
    {"name": "Alice", "department": "HR", "tenure": 3},
    {"name": "Bob", "department": "Finance", "tenure": 5},
    {"name": "Charlie", "department": "HR", "tenure": 2},
    {"name": "Diana", "department": "IT", "tenure": 4},
    {"name": "Eve", "department": "Finance", "tenure": 1}
]

generate_employee_report(employees)