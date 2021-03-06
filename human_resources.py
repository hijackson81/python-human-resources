import sqlite3
connection = sqlite3.connect("human_resources.db")
cursor = connection.cursor()
# Main menu
def menu():
    print("********** HUMAN RESOURCES MANAGEMENT SYSTEM **********")
    print("Please choose options below: ")
    print("1. Show List of Employees")
    print("2. Show List of Deparments")
    print("3. Show List of Departments and Members of Departments")
    print("4. Add New Employee")
    print("5. Add New Department")
    print("6. Add New Department and Employee")
    print("7. Find Employee")
    print("8. Quit")
    print("====================================")

# Menu Module 7
def menu7():
    print("Please choose options below: ")
    print("1. Find by name")
    print("2. Find by position")
    print("3. Find by employee id")
  
# Option 1 Module    
def show_employees():
    dash = '-' * 100
    cursor.execute("SELECT e.id as Employee_ID, e.name as Name, e.position as Position, e.age as Age, e.address as Address, d.name as Department FROM Employee as e, Department as d WHERE e.department_id = d.id;")
    header = [description[0] for description in cursor.description]
    result = cursor.fetchall()
    
    # Employee Header
    ajustment = "{:^15} {: ^25} {:<15} {:<5} {:^15} {:<15}"
    print (ajustment.format(header[0],header[1],header[2],header[3],header[4],header[5]))
    print(dash)
    
    # Employee Data
    for i in result:
        Employee_ID, Name, Position, Age, Address, Department = i
        print (ajustment.format( Employee_ID, Name, Position, Age, Address, Department))

# Option 2 Module 
def show_departments():
    dash = '-' * 50
    cursor.execute("SELECT  d.id as Department_ID, d.name as Department FROM Department as d;")
    header = [description[0] for description in cursor.description]
    result = cursor.fetchall()
    
    # Department Header
    ajustment = "{:^20} {: <25}"
    print (ajustment.format(header[0],header[1]))
    print(dash)

    # Deaprtment Data
    for i in result:
        Department_ID, Department_Name = i
        print (ajustment.format(Department_ID,Department_Name))

# Option 3 Module 
def dept_total_members():
    dash = '-' * 60
    cursor.execute("SELECT  d.id as Department_ID, d.name as Department, count(e.id) as Total_Members FROM Department as d, Employee as e WHERE e.department_id = d.id group by d.id;")
    header = [description[0] for description in cursor.description]
    result = cursor.fetchall()
    
    # Department Header
    ajustment = "{:^20} {: <10} {: ^25}"
    print (ajustment.format(header[0],header[1],header[2]))
    print(dash)

    # Deaprtment Data
    for i in result:
        Department_ID, Department_Name, Total_Members = i
        print (ajustment.format(Department_ID,Department_Name,Total_Members))  

# Option 4 Module 
def add_employee(name, position, age, address):
    cursor.execute(f"INSERT INTO Employee(name, position, age, address) VALUES ('{name}','{position}','{age}','{address}');")
    try:
            connection.commit()
            print(f"Employee added successfully: Name: {name}, Position: {position}, age: {age}, address: {address}")
    except sqlite3.IntegrityError as e:
        print(e)
        connection.rollback()

# Option 4 Advance      
def add_to_department(employee_id,department_id):
    cursor.execute(f"Update employee set department_id = '{department_id}' where id = {employee_id};")
    try:
            connection.commit()
    except sqlite3.IntegrityError as e:
        print(e)
        connection.rollback()  
          
# Option 5 Module 
def add_department(department_name,floor):
    cursor.execute(f"INSERT INTO Department(name,floor) VALUES ('{department_name}','{floor}');")
    try:
            connection.commit()
            print(f"Department added successfully: Name: {department_name}, floor {floor}")
    except sqlite3.IntegrityError as e:
        print(e)
        connection.rollback()

# Option 6 Module 
def link_employee(name, position, age, address,department_id,department_name):
    cursor.execute(f"INSERT INTO Employee(name, position, age, address,department_id) VALUES ('{name}','{position}','{age}','{address}','{department_id}');")
    try:
            connection.commit()
            print(f"Employee added successfully to {department_name}: Name: {name}, Position: {position}, age: {age}, address: {address}")
    except sqlite3.IntegrityError as e:
        print(e)
        connection.rollback()
# Option 7 Module 
# Instead of creating 3 find modules. Added 3 values: find_value,item_index,type_of_value
def find(find_value,item_index,type_of_value):
    dash = '-' * 100
    cursor.execute("SELECT e.id as Employee_ID, e.name as Name, e.position as Position, e.age as Age, e.address as Address, d.name as Department FROM Employee as e, Department as d WHERE e.department_id = d.id;")
    header = [description[0] for description in cursor.description]
    result = cursor.fetchall()
    
    # Employee Header
    ajustment = "{:^15} {: ^25} {:<15} {:<5} {:^15} {:<15}"
    print (ajustment.format(header[0],header[1],header[2],header[3],header[4],header[5]))
    print(dash)
    
    # Find value is int
    if type_of_value == "int":
        for item in result:
            if find_value == item[item_index]:
                Employee_ID, Name, Position, Age, Address, Department = item
                print (ajustment.format( Employee_ID, Name, Position, Age, Address, Department))
    # Find value is string
    else:
        for item in result:
            if find_value in item[item_index]:
                Employee_ID, Name, Position, Age, Address, Department = item
                print (ajustment.format( Employee_ID, Name, Position, Age, Address, Department))

# main module
def main():
    while True:
        menu()
        choice = input("Please make a choice:  ")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
            menu()
            choice = input("Wrong choice. Please choose from ( 1 to 8 ):   ")
    
        # Choice 1
        while choice == "1":
            # print("Do something 1")
            show_employees()
            if input("Back to main menu. Press (0) :  ") == "0":
                break

        # Choice 2        
        while choice == "2":
            # print("Do something 2")
            show_departments()
            if input('Back to main menu. Press (0) :  ') == "0":
                break
 
        # Choice 3
        while choice == "3":
            # print("Do Something 3")
            dept_total_members()
            if input('Back to main menu. Press (0) :  ') == "0":
                break
 
        # Choice 4
        while choice == "4":
            print("Please Type New Employee Information:")
            name = input("Name: ")
            position = input("Position:  ")
            age = input("Age: ")
            address = input("Address: ")
            add_employee(name,position,age,address)
            show_departments()
            
            # find this new employee id
            cursor.execute(f"SELECT id FROM Employee as e where e.name = '{name}' and e.position = '{position}' and e.age = '{age}' and e.address = '{address}';")
            this_employee = cursor.fetchall()
            employee_id = this_employee[0][0]
            department_id = input(f"Please choose department for {name}:   ")
            
            # add to department        
            add_to_department(employee_id,department_id)
            print(f"{name} added to department {department_id} SUCCESSFULLY")
            if input('Back to main menu. Press (0) or Type anything to add more employee :  ') == "0":
                break
 
        # Choice 5            
        while choice == "5":
            print("Please Type Department Information:")
            dept_name = input("Department Name: ")
            floor = input("Floor:  ")
            add_department(dept_name,floor)
            if input('Back to main menu. Press (0) or Type anything to add more deaprtment :  ') == "0":
                break
 
        # Choice 6            
        while choice == "6":
            print("Please Type Department Information:")
            dept_name = input("Department Name: ")
            floor = input("Floor:  ")
            add_department(dept_name,floor)
            
            # find this department id
            cursor.execute(f"SELECT id FROM Department as d where d.name = '{dept_name}' and d.floor = '{floor}';")
            this_department = cursor.fetchall()
            dept_id = this_department[0][0]
            
            # link new employee
            print(f"Please add employee to {dept_name}")
            name = input("Name: ")
            position = input("Position: ")
            age = input("Age: ")
            address = input("Address: ")
            link_employee(name,position,age,address,dept_id,dept_name)
            if input('Back to main menu. Press (0) :  ') == "0":
                break
  
        # Choice 7            
        while choice == "7":
            menu7()
            option7_choice = input("Please input choice: ")
            while option7_choice != "1" and option7_choice != "2" and option7_choice != "3":
                menu7()
                option7_choice = input("Wrong choice. Please choose from ( 1 to 3 ):   ")
            if option7_choice == "1":
                name = input("Please input employee name: ")
                index = 1
                find(name,index,"string")
            if option7_choice == "2":
                position = input("Please input employee position: ")
                index = 2
                find(position,index,"srting")
            if option7_choice == "3":
                id = int(input("Please input employee id: "))
                index = 0
                find(id,index,"int")
            if input('Press ( 0 ) to main menu or anykey to find again:  ') == "0":
                break
  
        # Choice 8
        if choice == "8":
            print("See you again !!! ")
            break

main()