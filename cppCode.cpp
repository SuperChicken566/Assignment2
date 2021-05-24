#include <iostream>
#include <string>
using namespace std; 

struct course_s
{
    int crn, time;
    string instructor, days, name;
};

class user_c
{
    private:
        string fName, lName;
        int idNum; 
    public:
        string getfName(){return fName;}
        string getlName() {return lName;}
        int getID(){return idNum;}
        void setfName(string f){fName = f;}
        void setlName(string l){lName = l;}
        void setID(int id){idNum = id;}
        void printAll()
        {
            cout << "Name: " << fName << " " << lName << endl;
            cout << "ID: W" << idNum << endl;
        }
        user_c(string f, string l, int ID) : fName{f}, lName{l}, idNum{ID}{}
        user_c() : fName{"Empty"}, lName{"Empty"}, idNum{0}{}
        ~user_c(){cout << "Person Deconstructed\n";} 
};

class student_c : public user_c
{
    public:

    void search()
    {
        cout << "searched " << endl;
    }

    void add()
    {
        cout << "registered successfully" << endl;
    }

    void drop()
    {
        cout << "dropped successfully" << endl;
    }
    void printSchedule()
    {
        cout << "printed schedule" << endl;
    }
    //empty constructor just for testing
    student_c() : user_c()
    {
        cout<<"Student created"<<endl;
    }

};

class instructor_c : public user_c
{
    public:

    void printList()
    {
        cout << "printed courses" << endl;
    }

    void printSchedule()
    {
        cout << "schedule printed" << endl;
    }

    void search()
    {
        cout << "search completed" << endl;
    }
    instructor_c() : user_c()
    {
        cout<<"Instructor created"<<endl;
    }
};

class admin_c : public user_c
{
    public:

    void addCourse()
    {
        cout << "course created" << endl;
    }

    void removeCourse()
    {
        cout << "course deleted" << endl;
    }

    void addUser()
    {
        cout << "user created" << endl;
    }

    void removeUser()
    {
        cout << "user deleted" << endl;
    }

    void forceRegister()
    {
        cout << "registered" << endl;
    }

    void forceDrop()
    {
        cout << "dropped a class" << endl;
    }

    void printSchedule()
    {
        cout << "print called" << endl;
    }

    void search()
    {
        cout << "search called" << endl;
    }
    admin_c() : user_c()
    {
        cout<<"Student created"<<endl;
    }      
};

int main ()
{
int choice = 0, selection = 0;
student_c testStudent;
instructor_c testInstructor;
admin_c testAdmin;

do
{
    cout << "\nSelect your role:\nStudent: 1\nInstructor: 2\nAdmin: 3\nLeave: 0\n" << endl;
    cin >> choice;

    switch (choice)
    {
    case 1:
        do
        {
        cin.ignore();
        cout << "\nStudent Selected \nChoose your action:\n1: Search courses\n2: Register\n3: Drop\n4: print schedule\n0: Leave\n\nMake your selection:\n";
        cin >> selection;
            switch (selection)
            {
            case 1:
                testStudent.search();
                break;

            case 2:
                testStudent.add();
                break;
            
            case 3:
                testStudent.drop();
                break;

            case 4:
                testStudent.printSchedule();
                break;

            case 0:
                break;

            default:
                cout << "code brokey try again" << endl;
                break;
            }
        } while (selection != 0);

        break;

    case 2:
        do
        {
        cin.ignore();
        cout << "\nInstructor Selected \nChoose your action:\n1: Search courses\n2: Print Classlist\n3: Print Schedule\n0: Leave\n\nMake your selection:\n";
        cin >> selection;
            switch (selection)
            {
            case 1:
                testInstructor.search();
                continue;

            case 2:
                testInstructor.printList();
                continue;
            
            case 3:
                testInstructor.printSchedule();
                continue;
                
            case 0:
                break;

            default:
                cout << "code brokey try again" << endl;
                break;
            }

        } while (selection !=0);
        break;
    
    case 3:
        do
        {
        cin.ignore();
        cout << "\nAdmin Selected \nChoose your action:\n1: Create Course\n2: Delete Course\n3: Creat User\n4: Remove User\n5: Force Register\n6:Forcedrop\n7: Print\n0: Leave\n\nMake your selection:\n";
        cin >> selection;
            switch (selection)
            {
            case 1:
                testAdmin.addCourse();
                break;

            case 2:
                testAdmin.removeCourse();
                break;
            
            case 3:
                testAdmin.addUser();
                break;
                
            case 4:
                testAdmin.removeUser();
                break;

            case 5:
                testAdmin.forceRegister();
                break;
            
            case 6:
                testAdmin.forceDrop();
                break;

            case 7:
                testAdmin.printSchedule();
                break;

            case 0:
                break;

            default:
                cout << "code brokey try again" << endl;
                break;
            }
        } while (selection !=0);
        break;

    default:
        break;
    }
} while (choice != 0);

}

