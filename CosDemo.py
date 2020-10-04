
# **** IMPORTANT I do not go over Encapsulation Polymorphism and Inheritance in this demo ****
class Salesteam:
	def __init__(self,name, teammate_type):
		self.name = name
		self.teammate_type = teammate_type
class Customer:
	def __init__(self,name, membership_type):
		self.name = name
		self.membership_type = membership_type
	def update_membership(self,new_membership):
		# Theoretically would invoke an API
		self.membership_type = new_membership
	def calc_customer():
		print("Finding customer from data base")
	def __str__(self):
		print('converting to string')
		return self.name +" " +self.membership_type
	def print_all_customers(customers):
		for customer in customers:
			print(customer)
	def __eq__(self,other):
		if self.membership_type == other.membership_type:
			return True
		return False


print('\t\t\t---------------------\n')
print('\t\t---------------------\n')
print('\t\tCreating Costco Membership\n')
print('\t\t---------------------\n')
print('\t\t\t---------------------\n')
print('\tNames and Membership type.\n')
# Arguments follow method parameters 

customers = [Customer("james","gold"),
			Customer("mike","silver"),
			Customer("sean","gold"),
			Customer("laura","silver")]
print(customers[0].name.title())

print(customers[0].membership_type.title())

print(customers[1].name.title())

print(customers[1].membership_type.title())

print('\n===========================\n')
# New type of membership for customer Mike
customers[1].update_membership("gold")
print(customers[1].membership_type.title() + ' is the members new tier!')

print('\n===========================\n')
# Mike is now a Gold member
Customer.calc_customer()
# All Customer class invoked calculating position, because self isn't present

print('\n===========================\n')
print(customers[0])
# When you don't want the location but the actual data
print('\n===========================\n')
# Say you want a quick access to customer list 
# Create a method for and in (loop) using Class Customer
Customer.print_all_customers(customers)
print('\n===========================\n')
# Using the equals method to compare customers
print(customers[0] == customers[1])
print(customers[0] == customers[3])
print('\n===========================\n')
