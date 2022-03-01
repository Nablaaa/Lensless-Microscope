# kleines testprogramm
x = 5

# importiere das modul
import guterRechner
import numpy as np
x = 17
meinRechner = guterRechner.Rechner(x)
print('x = ' + str(x))
print('Quadrat = ' + str(meinRechner.Quadrat()))
print('2x = ' + str(meinRechner.Verdoppeln()))
print('Nachfolger = ' + str(meinRechner.Nachfolger()))

# oder auch

x = np.linspace(0,9,10)	
andererRechner = guterRechner.Rechner(x)
print('x = ' + str(x))
print('Quadrat = ' + str(andererRechner.Quadrat()))
print('2x = ' + str(andererRechner.Verdoppeln()))
print('Nachfolger = ' + str(andererRechner.Nachfolger()))

andererRechner.Darstellen()

