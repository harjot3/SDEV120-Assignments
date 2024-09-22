def readFile(file):
    try:
        f = open(file, "r")
        employee_data = {
            "name": 1,#name in file
            "id" : 1,#id in file"
            "dependents" : 1, #number of dependents
            "hours": 1, #hours worked
        }
    except FileNotFoundError:
        print(f"The file {file} does not exist")

def main():
    print("""For this assignment, we'll be reading a file including 10 employee's
first and last name, ID, number of dependents, hours worked, and creating their payroll.\n""")
    file = input("Please enter your file's name: ")
    readFile(file)

main()

