def anniversary_notifications(employees, current_month, current_year):
    for employee in employees:
        hire_date = employee["hire_date"]
        name = employee["name"]
        # Write your code here
        hire_year = int(hire_date[:4])
        hire_month = hire_date[5:7]
        if hire_month == current_month:
            years = current_year - hire_year
            # After constructing the message variable, print it
            message = f"{name} celebrates {years} year(s) with the company this month!"
            # Add this line after constructing the message:
            print(message)

# Sample call
employees = [
    {"name": "Alice Smith", "hire_date": "2018-07-10"},
    {"name": "Bob Lee", "hire_date": "2020-03-22"},
    {"name": "Carla Gomez", "hire_date": "2019-07-15"}
]
anniversary_notifications(employees, "07", 2024)