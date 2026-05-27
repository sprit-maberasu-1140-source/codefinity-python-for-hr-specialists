def generate_welcome_messages(employee_list):
    for employee in employee_list:
        message = f"Hello {employee['name']}, welcome to the company! Your email is {employee['email']}."
        print(message)

# Sample data
new_employees = [
    {"name": "Dana", "email": "dana.wilson@company.com"},
    {"name": "Eli", "email": "eli.turner@company.com"}
]

generate_welcome_messages(new_employees)
