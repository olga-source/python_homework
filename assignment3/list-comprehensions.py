import csv

def load_employees_from_csv():
    list_lists = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            list_lists = [row for row in reader] #written as comprehension instead of for loop
            # for row in reader:
            #     list_lists.append(row)  
    except Exception as e:
        return (f"Error: ", e)
    return list_lists

list_of_employees = load_employees_from_csv()

def load_names_from_csv():
    names_list = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) #first row
            names_list = [row[1] + " " + row[2] for row in reader] #row[1]=first_name; row[2]=last_name
    except Exception as e:
        return (f"Error: ", e)
    return names_list

names_of_employees = load_names_from_csv()

def names_with_e():
    list_names_e = []

    list_names_e = [row for row in names_of_employees if "e" in row] #added condition
    return list_names_e
