import sqlite3

database = sqlite3.connect("assignment3.db") 

cursor = database.cursor() 

sql_command = """CREATE TABLE IF NOT EXISTS COURSES (
CRN INTEGER PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL,
TIME INTEGER NOT NULL,
DAYS TEXT NOT NULL,
SEMESTER TEXT NOT NULL,
YEAR INTEGER NOT NULL,
CREDITS INTEGER NOT NULL);"""

cursor.execute(sql_command)

class course_s():
    def __init__(self, crn, title, department, time, days, semester, year, credits):
        self.title = title
        self.CRN = crn
        self.time = time
        self.days = days
        self.department = department
        self.semester = semester
        self.year = year
        self.credits = credits
        cursor.execute("""INSERT INTO COURSES VALUES('%i','%s', '%s', '%i', '%s', '%s', '%i','%i');""" % (crn, title, department, time, days, semester, year, credits))
        
class user_c():
    def __init__(self, f, l, id, email):
        self.fName = f
        self.lName = l
        self.idNum = id
        self.email = email

class student_c(user_c):
    def __init__(self,f ,l ,id, year, major, email):
        super().__init__(f,l,id, email)
        self.gradYear = year
        self.major = major
        cursor.execute("""INSERT INTO STUDENT VALUES('%i','%s', '%s', '%i', '%s', '%s');""" % (id, f, l, year, major, email))
  
        print("Student Created")

class instructor_c(user_c):
    def __init__(self, f, l, id, title, year, department, email):
        super().__init__(f, l, id, email)
        self.title = title
        self.hireYear = year
        self.dept = department
        cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%i','%s', '%s', '%i', '%s', '%s');""" % (id, f, l, title, year, department, email))

        print("Instructor Created")

class admin_c(user_c):
    def __init__(self, f, l, id, title, office, email):
        super().__init__(f, l, id, email)
        self.title = title
        self.office = office
        cursor.execute("""INSERT INTO ADMIN VALUES('%i','%s', '%s', '%s', '%s', '%s');""" % (id, f, l, title, office, email))

        print("Admin Created")

courses = {}
students = {}
instructors = {}
admins = {}

choice = 1
while choice != 0:
    choice = int(input("\nSelect your choice:\n1: Add Entry\n2: Remove Entry\n3: Update Entry\n4: Search Table\n5: Print Table\n0: Exit Program\n"))
    selection = 1
    if choice == 1:
        selection = int(input("\nWhat table are you adding to?\n1: Course\n2: Student\n3: Instructor\n4: Admin\n0: Back\n"))
        if selection == 1:
            CRN = int(input("Enter CRN number: "))
            title = input("Enter Title Name: ")
            department = input("Enter Department Name: ")
            time = int(input("Enter Start Time: "))
            days = input("Enter Days (MTWRF): ")
            semester = input("Enter Semester: ")
            year = int(input("Enter Year: "))
            credits = int(input("Enter Credits: "))

            courses[CRN] = course_s(CRN, title, department, time, days, semester, year, credits)
            
            continue
        elif selection == 2:
            ID = int(input("Enter ID number: "))
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            gradYear = int(input("Enter Graduation Year: "))
            major = input("Enter Major: ")
            email = input("Enter Email: ")

            students[ID] = student_c(firstName, lastName ,ID, gradYear, major, email)
            continue
        elif selection == 3:
            ID = int(input("Enter ID number: "))
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            title = input("Enter Title: ")
            hireYear = int(input("Enter Hire Year: "))
            department = input("Enter Department: ")
            email = input("Enter Email: ")

            instructors[ID] = instructor_c(firstName, lastName , ID, title, hireYear, department, email)
            continue
        elif selection == 4:
            ID = int(input("Enter ID number: "))
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            title = input("Enter Title: ")
            office = input("Enter Office: ")
            email = input("Enter Email: ")

            instructors[ID] = instructor_c(firstName, lastName, id, title, office, email)
            continue
        elif selection == 0:
            break        
    elif choice == 2:
        selection = int(input("\nWhat table are you deleting from?\n1: Course\n2: Student\n3: Instructor\n4: Admin\n0: Back\n"))
        if selection == 1:
            CRN = int(input("Enter CRN of course you want to delete: "))
            cursor.execute("""DELETE FROM COURSES WHERE CRN = '%i';""" % (CRN))
            continue 
        elif selection == 2:
            ID = int(input("Enter ID of Student you want to delete: "))
            cursor.execute("""DELETE FROM STUDENT WHERE ID = '%i';""" % (ID))
            continue
        elif selection == 3:
            ID = int(input("Enter ID of Instructor you want to delete: "))
            cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID = '%i';""" % (ID))
            continue
        elif selection == 4:
            ID = int(input("Enter ID of Admin you want to delete: "))
            cursor.execute("""DELETE FROM ADMIN WHERE ID = '%i';""" % (ID))
            continue
        elif selection == 0:
            break
    elif choice == 3:
        cursor.execute("""UPDATE ADMIN SET TITLE = 'Vice-President' WHERE ID = 30002;""")

        cursor.execute("""SELECT COURSES.TITLE, INSTRUCTOR.SURNAME FROM COURSES, INSTRUCTOR WHERE COURSES.DEPARTMENT = INSTRUCTOR.DEPT""")
        result = cursor.fetchall()
        for i in result:
            print(i)
         
        continue
    elif choice == 4:
        selection = int(input("\nWhat table are you searching from?\n1: Course\n2: Student\n3: Instructor\n4: Admin\n0: Back\n"))
        if selection == 1:
            CRN = int(input("Enter CRN of course you want to Search: "))
            cursor.execute("""SELECT * FROM COURSES WHERE CRN = '%i';""" % (CRN))
            result = cursor.fetchall()
            for i in result:
                print(i)
            continue 
        elif selection == 2:
            ID = int(input("Enter ID of Student you want to Search: "))
            cursor.execute("""SELECT * FROM STUDENT WHERE ID = '%i';""" % (ID))
            result = cursor.fetchall()
            for i in result:
                print(i)
            continue
        elif selection == 3:
            ID = int(input("Enter ID of Instructor you want to Search: "))
            cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = '%i';""" % (ID))
            result = cursor.fetchall()
            for i in result:
                print(i)
            continue
        elif selection == 4:
            ID = int(input("Enter ID of Admin you want to Search: "))
            cursor.execute("""SELECT * FROM ADMIN WHERE ID = '%i';""" % (ID))
            result = cursor.fetchall()
            for i in result:
                print(i)
            continue
        elif selection == 0:
            break
        break
    elif choice == 5:
        selection = int(input("\nWhat table do you want printed?\n1: Course\n2: Student\n3: Instructor\n4: Admin\n0: Back\n"))
        if selection == 1:
            cursor.execute("""SELECT * FROM COURSES""")
            query_result = cursor.fetchall()
            
            for i in query_result:
                print(i)
            continue 
        elif selection == 2:
            cursor.execute("""SELECT * FROM STUDENT""")
            query_result = cursor.fetchall()
            
            for i in query_result:
                print(i)
            continue
        elif selection == 3:
            cursor.execute("""SELECT * FROM INSTRUCTOR""")
            query_result = cursor.fetchall()
            
            for i in query_result:
                print(i)
            continue
        elif selection == 4:
            cursor.execute("""SELECT * FROM ADMIN""")
            query_result = cursor.fetchall()
            
            for i in query_result:
                print(i)
            continue
        elif selection == 0:
            break
        break
    elif choice == 0:
        print("Exit Program")
        break

database.commit() 
  
# close the connection 
database.close()