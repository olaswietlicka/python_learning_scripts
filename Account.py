class Account():

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return 'Account owner: {o}\nAccount balace: ${b}'.format(o=self.owner,b = self.balance)

	def deposit(self,depo):
		self.balance = self.balance + depo
		print('Deposit accepted')

	def withdraw(self,withdr):
		if self.balance<withdr:
			print('Funds Unavailable!')
		else:
			self.balance = self.balance - withdr
			print('Withdrawal Accepted')

acc = Account('Jose',100)
print(acc)
print(acc.owner)
print(acc.balance)
acc.deposit(50)
print(acc.balance)
acc.withdraw(75)
acc.withdraw(500)
