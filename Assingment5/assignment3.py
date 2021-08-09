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
	#marc - addded collums to the student table. 
	cursor.execute("""ALTER TABLE STUDENT 
  ADD CRN1 INTEGER NOT NULL, 
  ADD CRN2 INTEGER NOT NULL, 
  ADD CRN3 INTEGER NOT NULL, 
  ADD CRN4 INTEGER NOT NULL, 
  ADD CRN5 INTEGER NOT NULL;""")
  
  
      courses = {}
      students = {}
      instructors = {}
      admins = {}

	
      choice = 1
      while choice != 0:
      #kloe - edited/updated menu
    choice = int(input("\nSelect your choice:\n1: Add Course to System\n2: Remove Course from System\n3: Update Courses\n4: Search Courses\n5: Print Roster\n6: Remove Course from Semester Schedule\n0: Exit Program\n"))
    selection = 1
    if choice == 1: #marc added from previous code, kloe updated 
          selection = int(input("\nEnter the information for the course you want to add:\n"))
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
    elif choice == 2: #marc added from previous code, kloe updated 
        selection = int(input("\nEnter information for the course you want to delete:\n"))
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
      elif choice == 3:#marc created in addition to courses in course table 
      		inID = int(input("Enter Student ID"))
      		CRN1 = int(input("Enter CRN1"))
            CRN2 = int(input("Enter CRN2"))
            CRN3 = int(input("Enter CRN3"))
            CRN4 = int(input("Enter CRN4"))
            CRN5 = int(input("Enter CRN5"))
            cursor.execute("""UPDATE STUDENT WHERE ID = '%i' SET CRN1 = '%i', CRN2 = '%i', CRN3 = '%i', CRN4 = '%i', CRN5 = '%i';""" % (inID,CRN1,CRN2,CRN3,CRN4,CRN5)

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
              CRN = int(input("Enter CRN and Department of course you want to Search: "))
              cursor.execute("""SELECT * FROM COURSES WHERE CRN = '%i' AND DEPARTMENT = '%s';""" % (CRN, DEPARTMENT))
              result = cursor.fetchall()
              for i in result:
                  print(i)
              continue 
              
          elif selection == 0:
              break
          break
      elif choice == 5: #kloe added print roster function 
          selection = int(input("\nWhich roster would you like to print?\n"))
          if selection == 1:
          	  CRNin = int(input("Enter CRN of course roster you would like to print: "))
              cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE CRN1 = '%i' OR CRN2 = '%i' OR CRN3 = 'i' OR CRN4 = '%i' OR CRN5 = '%i'; """ % (CRNin,CRNin,CRNin,CRNin,CRNin))
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
          
          #kloe and marc created new choice
      elif choice == 6:
          selection = int(input("\nWhich course would you like to remove?\n"))
          if selection == 1:
              CRNin = int(input("Enter CRN number: "))
              cursor.execute("""UPDATE COURSES SET SEMESTER = "Null" WHERE CRN = '%i'; """ % (CRNin))
            	

          
if __name__=="__main__":
main()

database.commit() 
  
# close the connection 
database.close()