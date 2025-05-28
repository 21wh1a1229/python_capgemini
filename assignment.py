"""#assignment
inventory = [
    #name,    category,     unit_price,  unit_sold,  unit_left
    ["Strawberry", "Fruit",    3.50,        40,       10],
    ["Broccoli",    "Vegetable", 2.20,      25,        81],
    ["Cheddar",     "Dairy", 5.00,          18,         4],
    ["Baguette",   "Bakery", 2.80,         35,          2],
    ["Blueberry",   "Fruit", 4.00,          22,         8],
    ["Spinach",    "Vegetable", 1.80,      30,         12],
    ["Yogurt",     "Dairy",   1.20,        50,         10],
    ["Croissant", "Bakery",   3.00,        28,         3],]

#total revenue
def total_revenue():
    total_rev=0
    for item in inventory:
       total_rev +=item[2] * item[3]
       return total_rev
print(f'total revenue:{total_revenue()}')

#low stock
print('low stock items (stock<5):')
for item in inventory:
    name=item[0]
    stock_left=item[4]
    if stock_left<5:
        print("_", name)

#category wise revenue
category_rev={}
for item in inventory:
    category =item[1]
    revenue=item[2]*item[3]
    if category in category_rev:
        category_rev[category] += revenue
    else:
        category_rev[category] = revenue

print("category-wise revenue:")

for category,revenue in category_rev.items():
    print(f'{category}: ${revenue :.2f}')



#assignment 1

university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#print al students name and majors

print('students names and majors')
for students in university_data.values():
    print(f'{students['name']}-{students['major']}')
print()


#Average score per course per student
print(" Average Score Per Course Per Student")
for student in university_data.values():
    print(f"{student['name']}:")
    for course, scores in student["courses"].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: {avg:.2f}")
        print()

#fint the students who have scored >90 in final python101

print(" Students who scored >90 in final of Python101")
for student in university_data.values():
    if "Python101" in student["courses"]:
         if student["courses"]["Python101"]["final"] > 90:
            print(f"{student['name']}")
            print()

#Add new course AI101 for student S101
print("Adding AI101 course to S101")
university_data["S101"]["courses"]["AI101"] = {"midterm": 87, "final": 90, "project": 93}
print("AI101 added to S101.\n")

# Print average for each course
print(" Average per course (combined across all students)")
for std_id,std_info in university_data.items():
    print("name of the student is ",std_info["name"])
    for course,course_data in std_info["courses"].items():
        average = sum(course_data.values()) / len(course_data)
        print("Average:",course, average)
        print()



#assignment 2
import datetime
from functools import wraps

# Global list to store student records
students = []

# Decorator to log function activity
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Executing '{func.__name__}' at {datetime.datetime.now()}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}'\n")
        return result
    return wrapper

# Function to add student with multiple course grades
@log_activity
def add_student(name, roll_no, *courses, **grades):
    student_record = {
        "name": name,
        "roll_no": roll_no,
        "courses": courses,  
        "grades": grades      
    }
    students.append(student_record)
    print(f"Added {name} (Roll No: {roll_no}) with courses: {', '.join(courses)}")

# Function to display results
@log_activity
def display_all_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("=" * 40)
        print(f"Name    : {student['name']}")
        print(f"Roll No : {student['roll_no']}")
        total = 0
        count = 0

        for course in student['courses']:
            mark = student['grades'].get(course, None)
            if mark is not None:
                print(f"{course}: {mark}")
                total += mark
                count += 1
            else:
                print(f"{course}: No mark provided")

        if count > 0:
            avg = total / count
            print(f"Total   : {total}")
            print(f"Average : {avg:.2f}")
            if avg >= 90:
                grade = "A+"
            elif avg >= 75:
                grade = "A"
            elif avg >= 60:
                grade = "B"
            elif avg >= 40:
                grade = "C"
            else:
                grade = "F"
            print(f"Grade   : {grade}")
        else:
            print("No valid marks to calculate grade.")
        print("=" * 40)
add_student("irshi", 201, "AI", "ML", AI=95, ML=90)
add_student("bhagi", 202, "DBMS", "ML", DBMS=67, ML=70)
add_student("Shaik", 203, "AI", "DBMS", AI=55, DBMS=60)

display_all_students()



#assignment 3

class Department:
    total_depts = 0  # Class variable to keep track of department count

    def __init__(self, deptid, name, location, hod):
        self.deptid = deptid
        self.name = name
        self.location = location
        self.hod = hod
        Department.total_depts += 1  # Capital 'D' to refer to the class name correctly

    def display_info(self):
        print(f"\nDepartment ID: {self.deptid}")
        print(f"Name         : {self.name}")
        print(f"Location     : {self.location}")
        print(f"HOD          : {self.hod}")

    @classmethod
    def display_total_departments(cls):
        print(f"\nTotal Departments in Organization: {cls.total_depts}")


# Main Program
departments = []

n = int(input("Enter the number of departments: "))

for i in range(n):
    print(f"\nEnter details for Department {i + 1}:")
    deptid = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    hod = input("Enter HOD Name: ")

    dept = Department(deptid, name, location, hod)  # Use 'Department', not 'department'
    departments.append(dept)

for dept in departments:
    dept.display_info()


search_id = input("\nEnter Department ID to search: ")
found = False
for dept in departments:
    if dept.deptid == search_id:
        print("\nDepartment found:")
        dept.display_info()
        found = True
        break
if not found:
    print("Department ID not found.")

search_name = input("\nEnter Department Name to search (partial or full): ").lower()
matched = False

print("\n--- Departments Matching the Name ---")
for dept in departments:
    dept_name_lower = dept.name.lower()
    if (
        dept_name_lower.startswith(search_name)
        or dept_name_lower.endswith(search_name)
        or search_name in dept_name_lower
    ):
        dept.display_info()
        matched = True

if not matched:
    print("No department names matched your search.")


Department.display_total_departments() 


"""
#assignement 4

# Step 1: Write new initial content
with open('example_file.txt', 'w') as file:
    file.write("Welcome to the initial file.\n")
print("New initial content written.")

# Step 2: Append new content
with open('example_file.txt', 'a') as file:
    file.write(" Added as a continuation.\n")
print("New content appended.")

# Step 3: Read and print file content
with open('example_file.txt', 'r') as file:
    content = file.read()
print("File content:\n" + content)



    




       
