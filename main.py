import csv
import os
import time
from tabulate import tabulate

# File to store employee data
FILE_NAME = 'employee_database.csv'

# ANSI color codes
RESET = "\033[0m"
AQUA = "\033[96m"
RED = "\033[91m"
GREEN = "\033[92m"


# Clear the console based on the operating system
def cls():
    os.system("cls" if os.name == "nt" else "clear")

# Ensure the CSV file exists
def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Department", "Position", "Salary"])

def add_employee():
    emp_id = input(f"\033[92mEnter Employee ID: \033[0m")
    
    # Check if the ID already exists
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == emp_id:
                print(f"An employee with the ID \033[91m{emp_id}\033[0m is already present.")
                input("Press Enter to continue...")
                return
    
    # If ID does not exist, proceed to add the employee
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        name = input(f"\033[92mEnter Employee Name: \033[0m")
        age = input(f"\033[92mEnter Employee Age: \033[0m")
        department = input(f"\033[92mEnter Department: \033[0m")
        position = input(f"\033[92mEnter Position: \033[0m")
        salary = input(f"\033[92mEnter Salary: \033[0m")
        writer.writerow([emp_id, name, age, department, position, salary])
        print(f"\033[92mEmployee added successfully!\n\033[0m")
        input("Press Enter to continue...")

def view_employees():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) == 1:
            print(f"\033[91mNo employees found.\n\033[0m")
            input("Press Enter to continue...")
        else:
            headers = data[0]
            rows = data[1:]
            print(tabulate(rows, headers, tablefmt="grid"))
            input("Press Enter to continue...")

def search_employee():
    emp_id = input(f"\033[92mEnter Employee ID to search: \033[0m")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        matched_records = [row for row in data if row[0] == emp_id]
        
        if matched_records:
            print(f"\033[92mEmployee(s) Found: \033[0m" + f"\033[96m{len(matched_records)} Records Found\033[0m")
            print(tabulate(matched_records, headers=["ID", "Name", "Age", "Department", "Position", "Salary"], tablefmt="grid"))
        else:
            print(f"\033[91mEmployee not found.\n\033[0m")
        input("Press Enter to continue...")


def update_employee():
    emp_id = input(f"{GREEN}Enter Employee ID to update: {RESET}")
    updated = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == emp_id:
                print(f"{AQUA}Current Record:{RESET}", ', '.join(row))
                name = input(f"{GREEN}Enter new name (leave blank to keep unchanged): {RESET}") or row[1]
                age = input(f"{GREEN}Enter new age (leave blank to keep unchanged): {RESET}") or row[2]
                department = input(f"{GREEN}Enter new department (leave blank to keep unchanged): {RESET}") or row[3]
                position = input(f"{GREEN}Enter new position (leave blank to keep unchanged): {RESET}") or row[4]
                salary = input(f"{GREEN}Enter new salary (leave blank to keep unchanged): {RESET}") or row[5]
                writer.writerow([emp_id, name, age, department, position, salary])
                updated = True
                print(f"{GREEN}Record updated successfully!\n{RESET}")
            else:
                writer.writerow(row)

    if not updated:
        print(f"{RED}Employee not found.\n{RESET}")

def delete_employee():
    emp_id = input(f"{GREEN}Enter Employee ID to delete: {RESET}")
    deleted = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == emp_id:
                print(f"{GREEN}Record deleted successfully!\n{RESET}")
                deleted = True
            else:
                writer.writerow(row)

    if not deleted:
        print(f"{RED}Employee not found.\n{RESET}")

def main():
    initialize_csv()
    while True:
        try:
            cls()
            print("""\033[96m
  ______                   __  __    _____  
 |  ____|                 |  \\/  |  / ____| 
 | |__   _ __ ___  _ __   | \\  / | | (___   
 |  __| | '_ ` _ \\| '_ \\  | |\\/| |  \\___ \\  
 | |____| | | | | | |_) | | |  | |_ ____) | 
 |______|_| |_| |_| .__/  |_|  |_(_)_____(_) 
                  | |                       
                  |_|              by:\033[91m el primero\033[0m\033[96m 
\033[0m""")

            print(f"{AQUA}_____________________________________{RESET}")
            print("1. Add new Employee")
            print("2. View Database of all Employees")
            print("3. Search for an Employee using an ID")
            print("4. Update Record for an Employee")
            print("5. Delete Record of an Employee")
            print("6. Exit")
            print(f"{AQUA}_____________________________________{RESET}")

            choice = input(f"{GREEN}Enter your choice: {RESET}")
            if choice == '1':
                add_employee()
            elif choice == '2':
                view_employees()
            elif choice == '3':
                search_employee()
            elif choice == '4':
                update_employee()
            elif choice == '5':
                delete_employee()
            elif choice == '6':
                print(f"{RED}Exiting Employee Management System. Goodbye!{RESET}")
                exit()
            else:
                print("Invalid choice! Please enter a valid option.")
                for remaining in range(3, 0, -1):
                    print(f"\033[91mReturning to main menu in {remaining}...\033[0m", end="\r")
                    time.sleep(1)  # Wait for 1 second
        except KeyboardInterrupt:
            print("\nByeBye...")
            exit()
if __name__ == "__main__":
    main()
