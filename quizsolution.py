import pandas as pd


file_path = "employee_data.csv"   
employee_data = pd.read_csv(file_path)


salary_increase_percentage = 0.10


total_increase = 0


new_salaries = {}


for _, row in employee_data.iterrows():
    full_name = f"{row['First Name']} {row['Last Name']}"
    department = row['Department']
    title = row['Title']
    clearance = row['Clearance']
    current_salary = row['Salary']

  
    if department == "Marketing" and title == "CSR" and clearance == "TS":
        new_salary = current_salary * (1 + salary_increase_percentage)
        increase_amount = new_salary - current_salary
        total_increase += increase_amount

       
        new_salaries[full_name] = new_salary

       
        print(f"Employee: {full_name} | Current Salary: ${current_salary:,.2f}")

print("\n" + "="*40 + "\n")

# Print AFTER salary (from dictionary)
for name, new_salary in new_salaries.items():
    print(f"Employee: {name} | New Salary: ${new_salary:,.2f}")

print("\n" + "="*40 + "\n")

# Print total increase
print(f"Total salary increase: ${total_increase:,.2f}")
