import time
from random import randint

def log(func):
	def wrapper(*args, **kwargs):
		#a+ : read or file add mode. if no file, make it
		file = open("machine.log", "a+")
		#computer current time, return float
		exec = time.time()
		s = str(func).split()[1].split('.')[1].replace('_', ' ').title()
		file.write("(cclaude) Running: {:30}".format(s))
		result = func(*args, **kwargs)
		exec = time.time() - exec
		if exec > 0.001:
			file.write("[ exec-time = %.3f s ]\n" % exec)
		else:
			file.write("[ exec-time = %.3f ms ]\n" % (exec * 1000))
		file.close()
		return result
	return wrapper

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
	@log
	def boil_water(self):
			return "boiling..."
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)
