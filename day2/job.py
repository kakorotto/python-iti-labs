class Person:
	def __init__(self, full_name, money, sleepmood, healthRate):
		self.full_name=full_name
		self.money=money
		self.sleepmood=sleepmood
		self.healthRate=healthRate

	def sleep( hours ):
	 	if hours == 7:
	 		return "happy"
	 	elif hours > 7:
	 		return "tiered"
	 	elif hours < 7: 
	 		return "lazy"
	 	else:
	 		return "wrong answer"

	def eat(self, meals ):
	 	if meals == 3:
	 		self.healthRate = 100
	 	elif meals == 2:
	 		self.healthRate = 75
	 	elif meals == 1: 
	 		self.healthRate = 50
	 	else:
	 		return "wrong answer"


	def buy( items ):
		if items == 1:
			self.money -= 10
		else:
			return "wrong answer"

	def sendEmail(to, suject, body, receiver_name ): 
		pass
		# try:
		#     f = open("plan.txt", 'r')
		# except:
		#     print("file is not reachable")
		# else:
		#     content = f.read()
		#     print(content)
		# finally:
		#     print("Transaction completed") 

	def p(self):
		print(self.full_name)

pp = Person("pola",10,1,400)

pp.p()

class Employee( Person ):
	def __init__(self, full_name, money, sleepmood, healthRate, id, email, workmood, salary, is_manager):
		super().__init__(full_name, money, sleepmood, healthRate)
		self.id=id
		self.email=email
		self.workmood=workmood
		self.salary=salary
		self.is_manager=is_manager




def work ( hours ):
	pass
 # Method in Employee class( 8  happy, 8  tired, > 8  lazy)
def Salary(): 
	pass
# Property must be 1000 or more
def Healthrate():
	pass
# Property must b e between 0 and 100
def Email(): 
	pass
# Property must be verified with regex expression

def function(sendEmail):
 	pass


class Office:
	def __init__(employees):
			pass
	def get_all_employees(self):
		pass
	def get_employee(self):
		pass
	def fire(self):
		pass
	def hire(self):
		pass