"""
Wilkommen zu einem kleinen Tutorial ueber einige hilfreiche Funktionen
in Python. Dieses Skript dient als kleine Hilfestellung, um die anderen
Programme besser zu verstehen. Es ist nicht notwendig, dass Sie dieses
Skript durcharbeiten, aber es kann sehr hilfreich sein.


In diesem Programm soll gezeigt werden:
- welche funktionen man in einer for-Schleife nutzen kann und warum
  man das machen sollte

- diese Funktionen sind:
    - range()
    - np.arange()
    - np.linspace()
    - enumerate()
    - np.unique()
    - zip()
    - sorted()
    - reversed()
    - break
    - continue

aber es gibt auch noch mehr

Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Viel Spass beim ausprobieren!
"""


# einfachste Schleife
for i in range(5):
    print(i)

# Numpy array
import numpy as np
for i in np.arange(1,12,0.25):
    print(i)

for i in np.linspace(1,13,5):
    print(i)


# Jetzt wollen wir durch definierte Listen durch iterieren
# das kann zum Beispiel hilfreich sein, wenn wir spaeter 
# unsere Bilder durchgehen wollen

ordner_mit_bildern = "Desktop/LinsenlosesMikroskop/PythonSkripte/Tips_Und_Tricks/"
wort_liste = ["bild7.png","bild12.png","bild5.png","bild8.png","bild19.png"]

for bildname in wort_liste:
    print("Bild %s wird nun aufgerufen" %(ordner_mit_bildern+bildname))

    # hier kann nun z.B. das bild geladen werden
    # import cv2
    # bild = cv2.imread(ordner_mit_bildern+bildname)


# jetzt haben wir z.B. ein Bild und wollen sehen welche werte in dem Bild alles auftauchen
# dazu nutzen wir die UNIQUE funktion von numpy
# ein beispiel bild soll ein format von 5x5 pixeln haben und
# ganze-zahlen Werte zwischen 0 und 10 beinhalten
bild_beispiel = np.random.randint(0,10,(5,5)) 
print(bild_beispiel)

# nun wollen wir alle einzigartigen Werte aus dem Bild auslesen
print(np.unique(bild_beispiel))

for wert in np.unique(bild_beispiel):

    # schaue, wie oft der wert im Bild vorkommt
    anzahl = np.sum(bild_beispiel==wert)

    print("Der Wert %i kommt im Bild %i mal vor" %(wert,anzahl))


# Jetzt wollen wir durch namen durchiterieren und gleichzeitig die
# Position des namens in der Liste ausgeben
# Dazu nutzen wir die enumerate funktion


# intensitaet = np.zeros(len(wort_liste))
for i, bildname in enumerate(wort_liste):
    print("Bild %s wird nun aufgerufen" %(ordner_mit_bildern+bildname))
    print("Es ist das Bild Nummer %i von insgesamt %i Bildern" %(i+1,len(wort_liste)))

    # jetzt kann das bild wieder mit cv2.imread gelesen werden
    # und dann koennte man z.B. einen Wert von dem Bild extrahieren
    # und in einer Liste speichern

    # initialisiere eine Liste, bevor die Schleife startet
    # jetzt nutze den Wert "i" der Schleife um eintraege hinzuzufuegen
    # fuege z.B. die maximale intensitaet des Bildes hinzu

    # import cv2
    # bild = cv2.imread(ordner_mit_bildern+bildname)
    # intensitaet[i] = np.max(bild)


# sortiere Liste vor der Iteration (kann wichtig werden)
for i, bildname in enumerate(sorted(wort_liste)):
    print("Bild %s wird nun aufgerufen" %(ordner_mit_bildern+bildname))
    print("Es ist das Bild Nummer %i von insgesamt %i Bildern" %(i+1,len(wort_liste)))







# mehrere Listen gleichzeitig durchiterieren und sortieren
# dazu nutzen wir die zip funktion
# das kann sehr hilfreich sein, wenn wir spater informationen
# aus zwei bildern bekommen wollen (e.g. wir haben ein bild auf
# dem wir kleine Mikroben sehen und ein Bild auf dem wir markiert
# haben wo sich die Mikroben befinden. Dann koennen wir die 
# Information von der Position nutzen, um Messungen an den Mikroben
# zu machen)

liste_mit_mikroben = ["Mikrobe5.png","Mikrobe2.png","Mikrobe12.png","Mikrobe4.png"]
liste_mit_segmentierung = ["Mikrobe2_segmentiert.png","Mikrobe12_segmentiert.png","Mikrobe5_segmentiert.png","Mikrobe4_segmentiert.png"]

for mikrobe, segmentierung in zip(liste_mit_mikroben,liste_mit_segmentierung):
    print("Mikrobe %s und Segmentierung %s wird nun aufgerufen" %(mikrobe, segmentierung))


# jetzt wollen wir die Listen sortieren und noch den Index ausgeben
# dazu nutzen wir die enumerate, sorted und zip funktion
for i, (mikrobe, segmentierung) in enumerate(zip(sorted(liste_mit_mikroben),sorted(liste_mit_segmentierung))):
    print("Mikrobe %s und Segmentierung %s wird nun aufgerufen" %(mikrobe, segmentierung))
    print("Es ist die Mikrobe Nummer %i von insgesamt %i Mikroben" %(i+1,len(liste_mit_mikroben)))


# manchmal will man eine Schleife vorzeitig abbrechen oder eine Funktion in der Schleife ueberspringen
# dazu gibt es die break und continue funktion
# break beendet die Schleife komplett
# continue ueberspringt die aktuelle iteration und geht zur naechsten
for i in range(10):
    if i==5:
        break
    print(i)

for i in range(10):
    if i==5:
        continue
    print(i)


# continue kann sehr nuetzlich werden wenn man funktionen in der Schleife hat, die nicht immer
# ausgefuehrt werden sollen
for bild in wort_liste:
    print("Bild %s wird nun aufgerufen" %(ordner_mit_bildern+bild))

    """
    # hier kann nun z.B. das bild geladen werden
    import cv2
    bild = cv2.imread(ordner_mit_bildern+bild)

    maximale_intensitaet = np.max(bild)


    # jetzt wollen wir nur die Bilder laden, die hohe maximale intensitaeten haben
    if maximale_intensitaet < 10:
        continue

    
    # jetzt geht die schleife fur alle HELLEN bilder weiter
    # und wir koennen z.B. die maximale intensitaet ausgeben
    # oder andere operationen durchfuehren
    print(maximale_intensitaet)

    """




# zur Vollstaendigkeit gibt es noch die "reversed" als umgekehrte funktion zu
# sorted
for i in reversed(range(5)):
    print(i)




