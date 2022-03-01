# kleines testprogramm
x = 5

# importiere das modul
import Rechner

# greife auf die Quadratrechner funktion zu
quadrat = Rechner.Quadratrechner(x)

# gib das Ergebnis aus
print(str(x) + ' zum Quadrat = ' + str(quadrat) )

###################################################
# Jetzt mit Listen

# selbiges funktioniert auch mit dem modul numpy
import numpy
x = numpy.linspace(0,9,10)

# wieder unseren Quadratrechner nutzen
y = Rechner.Quadratrechner(x)

# und dartstellen mit Hilfe von matplotlib
import matplotlib.pyplot
matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()
