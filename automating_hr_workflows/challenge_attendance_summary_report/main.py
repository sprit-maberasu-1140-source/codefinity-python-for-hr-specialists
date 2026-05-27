def attendance_summary(all_employee_ids, present_today):
    # Write your code here
    present_header = "Present Employees:"
    absent_header = "Absent Employees:"
    present_employees = []
    absent_employees = []

    for emp_id in all_employee_ids:
        if emp_id in present_today:
            present_employees.append(emp_id)
        else:
            absent_employees.append(emp_id)
    # (User should populate present_employees and absent_employees)
    print(present_header)
    print(present_employees)
    print(absent_header)
    print(absent_employees)

# Sample calls
attendance_summary(["E101", "E102", "E103", "E104"], ["E102", "E104"])
attendance_summary(["A1", "A2", "A3"], ["A1"])
attendance_summary(["B1", "B2"], ["B1", "B2"])
attendance_summary(["C1", "C2"], [])
