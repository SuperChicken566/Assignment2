import sqlite3
from sqlite3.dbapi2 import Cursor

database = sqlite3.connect("final.db") 

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
        cursor.execute("""INSERT INTO STUDENT VALUES('%i','%s', '%s', '%i', '%s', '%s', 0, 0, 0, 0, 0);""" % (id, f, l, year, major, email))
    
        print("Student Created")

class instructor_c(user_c):
    def __init__(self, f, l, id, title, year, department, email):
        super().__init__(f, l, id, email)
        self.title = title
        self.hireYear = year
        self.dept = department
        cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%i','%s', '%s', '%i', '%s', '%s', 0, 0, 0);""" % (id, f, l, title, year, department, email))

        print("Instructor Created")

class admin_c(user_c):
    def __init__(self, f, l, id, title, office, email):
        super().__init__(f, l, id, email)
        self.title = title
        self.office = office
        cursor.execute("""INSERT INTO ADMIN VALUES('%i','%s', '%s', '%s', '%s', '%s');""" % (id, f, l, title, office, email))

        print("Admin Created")

#functions for the student
def studentselection(inputID):
    while True:
        choice = int(input("\nSelect your choice:\n1: Register for Course\n2: Drop Course\n3: Print Schedule\n4: Search Course Catalogue\n0: Save and Exit Program\n"))
        if choice == 1:
            inputCRN = input("Enter CRN of course you want to register for: ")
            SQLstring = "SELECT * FROM COURSES WHERE CRN = " + inputCRN
            cursor.execute(SQLstring)
            result1 = cursor.fetchall()
            if len(result1) == 0:
                print("Course does not exist.")
                break
            else:
                for i in result1:
                    print(*i, sep=' ')
                selection = input("\nIs this the course you want to register? (y/n): ")
                if selection in ['y', 'Y', 'yes', 'YES']:
                    for x in range(1,6): #used to iterate through the 5 crn values
                        SQLstring =  "SELECT CRN" + str(x) + " FROM STUDENT WHERE ID = " + str(inputID)
                        cursor.execute(SQLstring)
                        result = [int(record[0]) for record in cursor.fetchall()]
                        if result[0] != 0:
                            #print("Cell Already Filled")
                            continue
                        else: 
                            print("Empty course slot found; Schedule Updated")
                            SQLstring =  "UPDATE STUDENT SET CRN" + str(x) + " = " + str(inputCRN) + " WHERE ID =" + str(inputID)
                            cursor.execute(SQLstring)
                            break
                else:
                    break 

        elif choice == 2:
            inputCRN = int(input("Enter CRN of course you want to drop: "))
            for x in range(1,6):
                SQLstring =  "SELECT CRN" + str(x) + " FROM STUDENT WHERE ID = " + str(inputID)
                cursor.execute(SQLstring)
                result = [int(record[0]) for record in cursor.fetchall()]
                print(result[0])
                if result[0] == inputCRN:
                    SQLstring =  "UPDATE STUDENT SET CRN" + str(x) + " = 0 " "WHERE ID = " + str(inputID) 
                    cursor.execute(SQLstring)
                    print("Emptied cell")
                    break
                else: 
                    print("Cell value missmatched")

        elif choice == 3:
            for x in range (1,6):
                SQLstring =  "SELECT CRN" + str(x) + " FROM STUDENT WHERE ID = " + str(inputID)
                cursor.execute(SQLstring)
                result = [int(record[0]) for record in cursor.fetchall()]
                SQLstring = "SELECT * FROM COURSES WHERE CRN = " + str(result[0])
                cursor.execute(SQLstring)
                result1 = cursor.fetchall()
                for i in result1:
                    print(*i, sep=' ')

        elif choice == 4:
            searchCourses()
    
        elif choice == 0:
            break

def intructorSelection(inputID):
    while True:
        choice = int(input("\nSelect your choice:\n1: Print Course Detail Schedule\n2: Print Course Roster\n3: Search Roster \n4: Search Course Catalogue\n0: Save and Exit Program\n"))
        if choice == 1:
             for x in range (1,4):
                SQLstring =  "SELECT CRN" + str(x) + " FROM INSTRUCTOR WHERE ID = " + str(inputID)
                cursor.execute(SQLstring)
                result = [int(record[0]) for record in cursor.fetchall()]
                SQLstring = "SELECT * FROM COURSES WHERE CRN = " + str(result[0])
                cursor.execute(SQLstring)
                result1 = cursor.fetchall()
                for i in result1:
                    print(*i, sep=' ')
        elif choice == 2:
            CRNin = int(input("Enter CRN of course roster you would like to print: "))
            for x in range(1, 5):
                SQLstring = "SELECT NAME, SURNAME FROM STUDENT WHERE CRN" + str(x) + " =  " + str(CRNin)
                cursor.execute(SQLstring)
                query_result = cursor.fetchall()
                for i in query_result:
                    print(*i, sep=' ')
        elif choice == 3:
            CRNin = int(input("Enter CRN of course roster you would like to print: "))
            IDin = input("Enter the ID of the Student: ")
            for x in range(1, 5):
                SQLstring = "SELECT NAME, SURNAME FROM STUDENT WHERE (CRN" + str(x) + " =  " + str(CRNin) + " AND ID = " + str(IDin) + ")"
                cursor.execute(SQLstring)
                query_result = cursor.fetchall()
                for i in query_result:
                    print(*i, sep=' ')
        elif choice == 4:
            searchCourses()
        elif choice == 0:
            break

def searchCourses():
    selection = int(input("\n1: By CRN\n2: By CRN and Department\nHow would you like to search?: "))
    if selection == 1:
        CRN = int(input("Enter CRN of course you want to Search: "))
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = '%i';""" % (CRN))
        result = cursor.fetchall()
        for i in result:
            print(i)

    if selection == 2:
        CRN = int(input("Enter CRN course you want to Search: "))
        department = input("Enter Department for course you want to search: ")
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = '%i' AND DEPARTMENT = '%s';""" % (CRN, department))
        result = cursor.fetchall()
        for i in result:
            print(i)

def main():

    courses = {}
    students = {}
    instructors = {}
    admins = {}
    while True:
        inputUser = input("Are you logging in as a STUDENT, INSTRUCTOR, or ADMIN?\n")
        if inputUser in ["STUDENT", "INSTRUCTOR", "ADMIN"]:
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
        else:
            print("Invalid user. Please retry with a valid user type.")

    while True:
        if inputUser == "STUDENT":
            studentselection(inputPass)
        elif inputUser == "INSTRUCTOR":
            intructorSelection(inputPass)
        elif inputUser == "ADMIN":
            while True:
                choice = int(input("\n1: Add Course to Catalogue\n2: Remove Course from Catalogue\n3: Add User to Database\n4: Link Course to Instructor/Student \n0: Save and Exit Program\nSelect your choice: "))
                if choice == 1:
                    inputCRN = int(input("Enter CRN: "))
                    inputTitle = input("Enter Title of the Course: ")
                    inputDEPT = input("Enter 4 character Department: ")
                    inputTime = int(input("Enter time course runs: "))
                    inputDays = input("Enter days of the Week(MTWRF): ")
                    inputSemester = input("Enter Semester(Fall,Spring,Summer): ")
                    inputYear = int(input("Enter year: "))
                    inputCredits = int(input("Enter # of Credits: "))
                    courses[inputCRN] = (inputCRN, inputTitle, inputDEPT, inputTime, inputDays, inputSemester, inputYear, inputCredits)

                elif choice == 2:
                    CRN = int(input("Enter CRN of course you want to delete: "))
                    cursor.execute("""DELETE FROM COURSES WHERE CRN = '%i';""" % (CRN))
                
                elif choice == 3:
                    selection = int(input("1: Add Student\n2: Add Instructor\n0: Exit\n "))
                    inputID = input("Enter ID: ")
                    inputName = input("Enter Name: ")
                    inputSurname = input("Enter Surname: ")
                    inputEmail = input("Enter Email: ")
                    inputMaj = input("Enter Department: ")
                    if selection == 1:
                        inputGrad = int(input("Enter Graduation Year: "))
                        students[inputID] = (inputID, inputName, inputSurname, inputGrad, inputMaj, inputEmail)
                    elif selection == 2:
                        inputTitle = input("Enter Title: ")
                        inputYear = input("Enter Hire Year: ")
                        instructors[inputID] = (inputID, inputName, inputSurname, inputTitle, inputYear, inputDEPT, inputEmail)

                elif choice == 4:
                    selection = int(input("1: Link Course To Student\n2: Link Course to Instructor\nEnter Selection: "))
                    inputCRN = int(input("Enter CRN of Course you want to link to User: "))
                    inputID = int(input("Enter User ID: "))
                    if selection == 1:
                        for x in range(1,6): #used to iterate through the 5 crn values
                            SQLstring =  "SELECT CRN" + str(x) + " FROM STUDENT WHERE ID = " + str(inputID)
                            cursor.execute(SQLstring)
                            result = [int(record[0]) for record in cursor.fetchall()]
                            if result[0] != 0:
                                #print("Cell Already Filled")
                                continue
                            else: 
                                print("Empty course slot found; Schedule Updated")
                                SQLstring =  "UPDATE STUDENT SET CRN" + str(x) + " = " + str(inputCRN) + " WHERE ID =" + str(inputID)
                                cursor.execute(SQLstring)
                                break
                    
                    elif selection == 2: 
                        for x in range(1,4): #used to iterate through the 5 crn values
                            SQLstring =  "SELECT CRN" + str(x) + " FROM INSTRUCTOR WHERE ID = " + str(inputID)
                            cursor.execute(SQLstring)
                            result = [int(record[0]) for record in cursor.fetchall()]
                            if result[0] != 0:
                                #print("Cell Already Filled")
                                continue
                            else: 
                                print("Empty course slot found; Schedule Updated")
                                SQLstring =  "UPDATE STUDENT SET CRN" + str(x) + " = " + str(inputCRN) + " WHERE ID =" + str(inputID)
                                cursor.execute(SQLstring)
                                break
                elif choice == 5:
                    searchCourses()

                elif choice == 0:
                    break
        break

if __name__=="__main__":
    main()


database.commit() 

# close the connection 
database.close()