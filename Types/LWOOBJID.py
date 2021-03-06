import random


# Generates Object IDs for characters and object

class LWOOBJID:
	def generate(self, persistent: bool = False, client: bool = False, spawned: bool = False, character: bool = False):
		number = random.randrange(0, (2 ** 32) - 1)
		number = number | (int(persistent) << 32)
		number = number | (int(client) << 46)
		number = number | (int(spawned) << 58)
		number = number | (int(character) << 60)
		return number

	def generateobject(self):
		return random.randrange(1000000000000000000, 1999999999999999999)

	def generatespawner(self):
		return random.randrange(70000000000000, 79999999999999)
