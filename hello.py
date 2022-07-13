# example class
# A Sample class with init method

class Hello:
	
	# init method or constructor
	def __init__(self, yourname):
		# Instance Variable
		self.name = yourname
	
	# Sample Method
	def say(self):
		print(f"Hello, my name is {self.name}")

# Driver Code
a = Hello("Alex")
a.say()