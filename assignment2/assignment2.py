#Task#2: Read a CSV File
import csv

def read_employees():
    employees_dict = {}
    rows_list = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) #first row
            employees_dict['fields']=header
            for row in reader:
                rows_list.append(row)    
            employees_dict['rows']=rows_list
    except Exception as e:
        return ("Error: ", e)
    return employees_dict
    
employees = read_employees()
print(employees)

#Task#3: Find the Column Index
def column_index(column_header):
    return employees["fields"].index(column_header)

employee_id_column = column_index("employee_id")

#Task#4: Find the Employee First Name
def first_name(row_number):
    try:
        first_name_index  = column_index("first_name") #index =1
        row = employees["rows"][row_number-1] #list
        return row[first_name_index]
    except Exception as e:
        return "Error: ", e
print(first_name(2))

#Task#5: Find the Employee: a Function in a Function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))

    return matches

#Task#6: Find the Employee with a Lambda
def employee_find_2(employee_id): 
    return list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"])) 

#Task#7: Sort the Rows by last_name Using a Lambda 
def sort_by_last_name():
    employees["rows"].sort(key=lambda e: e[column_index("last_name")])
    return employees["rows"]

#Task#8: Create a dict for an Employee
def employee_dict(row):
    result_dict = {}

    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":  
            result_dict[field] = row[i]
    return result_dict

print(employee_dict(employees["rows"][10]))

#Task#9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[employees["fields"].index("employee_id")]
        result[employee_id] = employee_dict(row)
    return result

print(all_employees_dict())

#Task#10: Use the os Module
import os

def get_this_value():
    return os.environ.get('THISVALUE')

print(get_this_value())

#Task#11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Test_123")
print(custom_module.secret)  

#Task#12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = {}
    minutes2 = {}

    #helper function: DRY principal used
    def read_file(file):
        minutes_dict = {}
        rows_list = []
        file_path = f"../csv/{file}.csv"
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                minutes_dict['fields']=header
                for row in reader:
                    rows_list.append(row)    
                minutes_dict["rows"]=rows_list
                minutes_dict["rows"] = [tuple(row) for row in minutes_dict["rows"]]
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        return minutes_dict
    
    try:
        minutes1 = read_file('minutes1')
        minutes2 = read_file('minutes2')
    except Exception as e:
        return ("Error: ", e)
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

#Task#13: Create minutes_set
def create_minutes_set():
    resulting_set = {}

    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    resulting_set = set1.union(set2)
    return resulting_set

minutes_set = create_minutes_set()

#Task#14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)

    #converted in tuples then in list; 2nd element converted in datetime objects
    resulting_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return resulting_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task#15: Write Out Sorted List
def write_sorted_list():
    #Sort minutes_list in ascending order of datetime 
    sorted_datetime = sorted(minutes_list, key=lambda x: x[1])
    #2nd element converted in string from datetime objects
    converted_sorted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_datetime))

    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(minutes_list)

    return converted_sorted_list

write_sorted_list()

