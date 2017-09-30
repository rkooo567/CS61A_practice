class Account(object):
	""" 
	A bank account that has a non-negatvie balance.
	"""
	interest = 0.02 # class varaible 
	def __init__(self, account_holder):
		""" constructor """
		self.balance = 0
		self.holder = account_holder

	def deposit(self, amount):
		""" deposit money to the account """
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return "Insufficient funcs"
		self.balance = self.balance - amount
		return self.balance

class CheckingAccount(Account):
	""" A bank account that charges for withdraw """
	withdraw_charge = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_charge)