"kleines Beispiel modul"

# Funktion
def Quadratrechner(x):
    return x * x
    
# Main Teil
def main():
    zahl = 5
    quadratzahl = Quadratrechner(zahl)
    print(str(zahl) + ' zum Quadrat = ' + str(quadratzahl) )

# Bedingung
if __name__ == "__main__":
	main()
