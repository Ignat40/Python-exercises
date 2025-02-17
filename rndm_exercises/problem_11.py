# A company decides to give bonus of 5% to employee if his/her year of service is more than 5 years
# Ask user for their salalry and year of service and print the net bonus. 

salary = float(input("Enter salary: "))
year_of_service = float(input("Enter service: "))
bonus = 0.05 * salary + salary

def check (salary, year_of_service):
    if year_of_service < 5:
        print("Salary = ", salary)
    else:
        print("Salary = ", bonus)

check(salary, year_of_service)