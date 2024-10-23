working_hours = float(input("Enter your working hours: "))
wage = float(input("Enter your wage: "))

if working_hours > 40:
    overtime_hours = working_hours - 40
    salary = (40 * wage) + (overtime_hours * wage * 1.5)
else:
    salary = working_hours * wage

print(f"Total salary: {salary:.2f}")