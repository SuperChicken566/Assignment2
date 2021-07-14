#code based off of marc's code for assignment 3. Kloe did most of the function editing and Marc did most of the database manipulation. changes will be marked individually below. 

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
        
def main():
    #marc - addded collums to the student table. not needed after running once
    #cursor.execute("""ALTER TABLE STUDENT ADD CRN1 INTEGER NULL;""")
    #cursor.execute("""ALTER TABLE STUDENT ADD CRN2 INTEGER NULL;""")
    #cursor.execute("""ALTER TABLE STUDENT ADD CRN3 INTEGER NULL;""")
    #cursor.execute("""ALTER TABLE STUDENT ADD CRN4 INTEGER NULL;""")
    #cursor.execute("""ALTER TABLE STUDENT ADD CRN5 INTEGER NULL;""")
    
    courses = {}
    students = {}
    instructors = {}
    admins = {}
    #collective contributions from marc and kloe
    inputUser = input("Are you logging in as a student, instuctor, or admin?\n")
    while True:
        inputEmail = input("Please enter an email: ")
        cursor.execute("""SELECT * FROM '%s' WHERE EMAIL = '%s';""" % (inputUser, inputEmail))
        result = cursor.fetchall()
        if len(result) == 0:
            print("Email doesn't exist")
            continue
        cursor.execute("""SELECT ID FROM '%s' WHERE EMAIL = '%s';""" % (inputUser, inputEmail))
        result = [int(record[0]) for record in cursor.fetchall()]
        inputPass = int(input("Please enter your ID number: "))
        if result[0] == inputPass:
            print("login valid")
            break
        elif result[0] != inputPass:
            print("login invalid")
            continue
    
    choice = 1
    while choice != 0:
    #kloe - edited/updated menu
        choice = int(input("\nSelect your choice:\n1: Add Course to System\n2: Remove Course from System\n3: Update Courses\n4: Search Courses\n5: Print Roster\n0: Exit Program\n"))
        selection = 1
        if choice == 1: #marc added from previous code, kloe updated 
            CRN = int(input("Enter CRN number: "))
            title = input("Enter Title Name: ")
            department = input("Enter Department Name: ")
            time = int(input("Enter Start Time: "))
            days = input("Enter Days (MTWRF): ")
            semester = input("Enter Semester: ")
            year = int(input("Enter Year: "))
            credits = int(input("Enter Credits: "))

            courses[CRN] = course_s(CRN, title, department, time, days, semester, year, credits)

        elif choice == 2: #marc added from previous code, kloe updated 
            CRN = int(input("Enter CRN of course you want to delete: "))
            cursor.execute("""DELETE FROM COURSES WHERE CRN = '%i';""" % (CRN))
            break
        elif choice == 3:#marc created in addition to courses in course table 
            inID = int(input("Enter Student ID: "))
            CRN1 = int(input("Enter CRN1: "))
            CRN2 = int(input("Enter CRN2: "))
            CRN3 = int(input("Enter CRN3: "))
            CRN4 = int(input("Enter CRN4: "))
            CRN5 = int(input("Enter CRN5: "))
            cursor.execute("""UPDATE STUDENT SET CRN1 = '%i', CRN2 = '%i', CRN3 = '%i', CRN4 = '%i', CRN5 = '%i' WHERE ID = '%i';""" % (CRN1,CRN2,CRN3,CRN4,CRN5,inID))

        elif choice == 4: #kloe added search by parameters
            selection = int(input("\nHow would you like to search?\n1: By CRN\n2: By CRN and Department\n"))
            if selection == 1:
                CRN = int(input("Enter CRN of course you want to Search: "))
                cursor.execute("""SELECT * FROM COURSES WHERE CRN = '%i';""" % (CRN))
                result = cursor.fetchall()
                for i in result:
                    print(i)
                continue 
            if selection == 2:
                CRN = int(input("Enter CRN course you want to Search: "))
                department = input("Enter Department for course you want to search: ")
                cursor.execute("""SELECT * FROM COURSES WHERE CRN = '%i' AND DEPARTMENT = '%s';""" % (CRN, department))
                result = cursor.fetchall()
                for i in result:
                    print(i)
                continue 
            elif selection == 0:
                break
            break
        elif choice == 5: #kloe & marc added print roster function 
            CRNin = int(input("Enter CRN of course roster you would like to print: "))
            cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE CRN1 = '%i' ; """ % (CRNin))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
            cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE CRN2 = '%i' ; """ % (CRNin))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
            cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE CRN3 = '%i' ; """ % (CRNin))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
            cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE CRN4 = '%i' ; """ % (CRNin))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
            cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE CRN5 = '%i' ; """ % (CRNin))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)

        elif choice == 0:
            print("Exit Program")
            break

if __name__=="__main__":
    main()


database.commit() 

# close the connection 
database.close()