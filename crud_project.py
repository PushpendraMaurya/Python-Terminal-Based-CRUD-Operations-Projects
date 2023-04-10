import mysql.connector as db
import time
from prettytable import PrettyTable
class CRUD:
    def __init__(self):
        #step - 2
        # 1 create database 
        mydb = db.connect(host = 'loca  lhost',user = 'dbuser',passwd = 'Squ@d123')
        query = ''' create database if not exists BasicDB;'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()
        
        # create table
        mydb = db.connect(host = 'localhost',user ='dbuser',passwd ='Squ@d123',database ='BasicDB')
        query = '''create table if not exists EmployeeInfo(eid int primary key auto_increment,
                    e_name varchar(20) not null,
                    e_date_of_join date,
                    e_salary bigint,
                    e_designation varchar (50),
                    e_contact varchar(20) unique);'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()
    
    def connection(self):
        self.mydb = db.connect(host = 'localhost',user ='dbuser', passwd = 'Squ@d123', database ='BasicDB')
        self.cur = self.mydb.cursor()


    def InsertDetails(self,name,doj,esalary,edesignation,econtact):
        self.connection()
        try :
            query =''' insert into EmployeeInfo(e_name ,e_date_of_join,e_salary, e_designation,e_contact ) values 
            (%s, %s, %s, %s, %s);'''

            data = (name, doj,esalary,edesignation,econtact)

            self.cur.execute(query ,data)
            self.cur.execute('commit ;')
            self.mydb.close()
            return True
        except:
            return False

    

    #Fetch all the records..

    def ReadAllData(self):
        self.connection()
        query='''select * from EmployeeInfo;'''
        self.cur.execute(query)
        records = self.cur.fetchall()
        # print(records)
        return records

    # delete the datas..
    def DeleteRecord(self,contact):
        self.connection()
        query= '''delete from EmployeeInfo where e_contact = %s;'''
        data = (contact,)
        self.cur.execute(query,data)
        self.cur.execute("commit ;")
        self.mydb.close()
        return "Data SuccessFUlly Deleted"

    def checkUser(self,contact):
        self.connection()
        data = (contact,)
        query = '''select * from EmployeeInfo where e_contact = %s'''
        self.cur.execute(query,data)
        record = self.cur.fetchone
        self.mydb.close()
        return record
    
    def UpdateInfo(self,query,data):
        self.connection()
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully data Updated"





# instamce 

app = CRUD()
while True:
    print("***********This is my crud appplication***************")
    print("1 - Insert \n2 Read \n3 Delete \n4 Update \n5 Exit")

    ch = input("Enter Your Choice :")
    if ch == "1":
        print("\n*********  Insert Information  ***********\n")
        name = input("Enter Your Name :")
        doj = time.strftime("%Y-%m-%d")
        esalary = int(input("Enter Your Salary :"))
        edesignation = input("Enter Your Designation :")
        econtact = input("Enter Your Contact :")

        x = app.InsertDetails(name,doj ,esalary, edesignation, econtact)
        if x == True:
            print("\n*********** SuccessFully Inserted ****************\n")

        else:
            print("\n******** This Contact Is Already Exists *********\n")

    elif ch == "2":
        print("\n*************** All Data From EMployee Table ***********\n")
        records =app.ReadAllData()
        x = PrettyTable()
        x.field_names =["id","EmployeeName","DateJoin","Salary","Designation","Contact"]
        x.add_rows(records)
        print(x)
    elif ch  == "3":
        print("\n************* Delete  Data ************\n")
        contact = int(input("Enter Your Unique "))
        dch = input("Are Your Sure Want to deleet the record :(y/n) :")
        if dch =="y" or dch =="yes" or dch =="Y" :
            a = app.DeleteRecord(contact)
            print(f"\n **************{a}*************\n")

        else:
            print("\n*********** Process has been Cancel **************\n")
    elif ch == "4":
        print("\n**********Update Section's ********\n")
        print("1 - update Employee Name \n2- Update Employee Salary \n3 - Update Designation \n")

        uch = input("Enter Your Choice to Updates ? :")
        contact = input("Enter Your Unique to Confirm your Identity :")


        #checkUser..............
        chk = app.checkUser(contact)
        if chk ==None:
            print("/n *********** Employee Not Exists ********/n")

        else:
            if uch =="1":
                print("Old Name is {chk[1]}")
                new_name = input("ENter Your New Name :")
                query = '''update EmployeeInfo set e_name = %s where e_contact = %s'''
                data = (new_name, contact)
                x = app.UpdateInfo(query,data)
                print(f"\n**************{x}************\n")

            elif uch =="2":
                print("Old Salary is {chk[3]}")
                new_salary = input("Enter Your New salary :")
                query = '''update EmployeeInfo set e_salary = %s where e_contact = %s'''
                data = (new_salary,contact)
                x = app.UpdateInfo(query,data)
                print(f"/n*****{x}*******/n")

            elif uch =="3":
                print("Old Designation is {chk[4]}")
                new_designation = input("Enter Your New Designation :")
                query = '''update EmployeeInfo set e_designation = %s where e_contact = %s'''
                data = (new_designation,contact)
                x = app.UpdateInfo(query, data)
                print(f"/n***************{x}*************/n")

            else:
                print("/n************** Invalid Updates choice !!!!/n")




    elif ch == "5":
        print("**************  Thank You **************")
        break
    else :
        print("********  Invalid Input  !!!!!!!!!!!1***********")
        

