import re
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='python'
)

cur = mydb.cursor()

# cur.execute('''create table employee(
#             id int primary key not null,
#             full_name varchar(50) not null,
#             salary int not null,
#             is_manager int
#             );''')
# mydb.commit()


class Person:
   def __init__(self, full_name, money,sleepmood,health_rate):
      self.full_name = full_name
      self.money = money
      self.sleepmood = sleepmood
      self.health_rate = health_rate

  
   def sethealth_rate(self, health_rate):
       if health_rate>=0 and health_rate<=100:
          self.health_rate=health_rate
       else:
          print('out of range')

   def sleep(self,hours):
      if hours==7:
          self.sleepmood = 'happy'
          print('your sleepmood changed to happy')
      elif hours > 7:
          self.sleepmood = 'lazy'
          print('your sleepmood changed to lazy')
      elif hours < 7:
          self.sleepmood = 'tired'
          print('your sleepmood changed to tired')
      return self.sleepmood

   def eat(self,meals):
       if meals<=3 and meals>=1:
            if meals==3:
                self.health_rate = '100'
                print('your health rate changed to 100')
            elif meals==2:
                self.health_rate = '75'
                print('your health rate changed to 75')
            elif meals==1:
                self.health_rate = '50'
                print('your health rate changed to 50')
            return self.health_rate
       else:
           print('out of range')

   def buy(self,items):
      if items==1:
          self.money -= 10
          print('Your money decreased by 10')

class Employee(Person):

   def __init__(self,full_name, money,sleepmood,health_rate, id, email, workmood,salary,is_manager):
      Person. __init__(self, full_name, money,sleepmood,health_rate)

      self.id = id
      self.email = email
      self.workmood = workmood
      self.salary = salary
      self.is_manager = is_manager

      sql="INSERT INTO employee (id, full_name, salary, is_manager) Values " \
            "(%s,%s,%s,%s)"
      val = (self.id,self.full_name, self.salary, self.is_manager)
      cur.execute(sql, val)
      print("employee added")  
      mydb.commit()   

    
   def setsalary(self, salary):
       if(salary>=10000):
          self.salary = salary
       else:
          print('out of range')
    
   def getsalary(self):
       return self.salary

   def setemail(self, email):
      if(re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email)):
         self.email = email
      else:
         print("Invalid Email")



   def work(self,hours):
      if hours==8:
          self.workmood = 'happy'
          print('your workmood changed to happy')
      elif hours < 8:
          self.workmood = 'lazy'
          print('your workmood changed to lazy')
      elif hours > 8:
          self.workmood = 'tired'
          print('your workmood changed to tired')
      return self.workmood

   def sendemail(self,to,subject,sender):
      f=open('email.txt','w')
      f.write(f'This email is sent to : {to} \n')
      f.write(f'This email subject is :{subject} \n')
      f.write(f'This email sender is : {sender} \n')
      f.close()


class Office:

   def __init__(self):
       pass
  
   def get_all_employees(self):
       cur.execute('select * from employee')
       rows = cur.fetchall()
       for row in rows:
            print(row)
       mydb.commit()
   
   def get_employee(self,num):
            cur.execute(f'select * from employee where id={num}')
            rows = cur.fetchall()
            for row in rows:
                print(row)
            mydb.commit()


   def hire(self,id,full_name,salary,is_manager):
      sql="INSERT INTO employee (id, full_name, salary,is_manager) Values " \
      "(%s,%s,%s,%s)"
      val = (id,full_name,salary,is_manager)
      cur.execute(sql, val)
      print("employee hired")  
      mydb.commit()  

   def fire(self,num):
      cur.execute(f'delete from employee where id={num}')
      print("employee fired")  
      mydb.commit()

ans=True
while ans:
    print ("""
    1.Add a Employees
    2.Get All Employees
    3.Exit/Quit
    """)
    ans=input("Make a choice: ") 
    if ans=="1": 
       o=Office()
       id = input("Enter your id: ")
       name = input("Enter your name: ")
       salary = input("Enter your salary: ")
       is_manager = input("Enter your manager: ")
       o.hire(id,name,salary,is_manager)
    elif ans=="2": 
       o=Office()
       o.get_all_employees()
    elif ans=="3":
      print("\n Goodbye") 
      ans=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 
      
      
      
mydb.close()