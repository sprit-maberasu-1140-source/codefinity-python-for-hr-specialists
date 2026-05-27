def print_high_turnover_departments(department_turnover, threshold):
    # Write your code here
    for department, turnover in department_turnover.items():
        if turnover > threshold:
            message = f"{department} has high turnover: {turnover:.0%}"
            print(message)

department_turnover = {
    "Finance": 0.07,
    "IT": 0.11,
    "Operations": 0.13,
    "Legal": 0.09
}
threshold = 0.10
print_high_turnover_departments(department_turnover, threshold)
