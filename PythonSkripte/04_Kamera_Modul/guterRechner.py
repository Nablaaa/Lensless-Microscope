class Rechner():
	def __init__(self, x):
		self.x = x
		
	def Quadrat(self):
		self.quadrat = self.x * self.x
		return self.quadrat
		
	def Verdoppeln(self):
		self.doppelt = 2 * self.x
		return self.doppelt
		
	def Nachfolger(self):
		self.nachfolger = self.x + 1
		return self.nachfolger
		
	def Darstellen(self):
		import matplotlib.pyplot as plt
		plt.plot(self.x, self.quadrat, label='x * x')
		plt.plot(self.x, self.doppelt, label='2 * x')
		plt.plot(self.x, self.nachfolger, label='x + 1')
		plt.legend()
		plt.show()
		
		
def main():
	import numpy as np
	x = 17
	meinRechner = Rechner(x)
	print('x = ' + str(x))
	print('Quadrat = ' + str(meinRechner.Quadrat()))
	print('2x = ' + str(meinRechner.Verdoppeln()))
	print('Nachfolger = ' + str(meinRechner.Nachfolger()))
	
	# oder auch
	
	x = np.linspace(0,9,10)	
	andererRechner = Rechner(x)
	print('x = ' + str(x))
	print('Quadrat = ' + str(andererRechner.Quadrat()))
	print('2x = ' + str(andererRechner.Verdoppeln()))
	print('Nachfolger = ' + str(andererRechner.Nachfolger()))
	
	andererRechner.Darstellen()
	
if __name__ == "__main__":
	main()
	
