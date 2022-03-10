"""
Wilkommen zum zweiten Programm auf dem Weg zu einem funktionsfaehigem 
linsenlosen Mikroskop fuer unter 10 Euro.

Falls Sie Probleme mit diesem Programm haben sollten, schauen Sie sich bitte
das erste Programm "01_Videos_mit_Kamera.py" an

Kommentare, die im vorherigen Programm gemacht wurden, werden hier der
Uebersicht halber verkuerzt oder weg gelassen.

In diesem Programm soll getestet werden, ob:
- das Modul os (Ordner erstellen) genutzt werden kann
- Ordner erstellt werden koennen
- Videos in den Ordnern gespeichert werden koennen
- Sie die Ordner finden und die Videos ansehen koennen



Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Viel Spass beim ausprobieren!
"""

import cv2
import time
import os # Verzeichnisse (Ordner) erstellen



# Erstelle Speicherordner und gebe der Datei einen Namen
# beide Infos ergeben den Speicherpfad
Speicherort = "Speicher-ordner"
video_name = "Videodatei.avi"
speicher_pfad = Speicherort + '/' + video_name

# Probiere den Ordner zu erstellen (mit 'os' modul)
try:
    os.mkdir(Speicherort)
    
# Falls ein Fehler auftritt gib eine Fehlermeldung aus
except OSError:
    print ("Der Ordner %s wurde nicht erstellt (z.B. weil er schon existiert)"
    		 % Speicherort)
    		 
# ansonsten gib eine Erfoglsmeldung aus
else:
    print ("Der Ordner %s wurde erfolgreich erstellt" % Speicherort)
    


# initialisiere Kamera
Kamera = cv2.VideoCapture(0)

# stelle die hoehe und weite des bildes ein 
w, h = 1280,720
Kamera.set(3,w)
Kamera.set(4,h)

# tatsaechliche weite und hoehe kann abweichen, deshalb werden wir die Variablen
# hier doppelchecken
w = int(Kamera.get(3)) # weite als integer
h = int(Kamera.get(4)) # hoehe als integer



# gebe an wie viele aufnahmen gemacht werden sollen
anzahl_Bilder = 200

# die startzeit ist wichtig, um zu sehen wie viel zeit insgesamt vergangen ist
# die "vorherige zeit" und die "aktuelle zeit" im der for schleife sind dazu 
# gedacht, herauszufinden, welche zeit zwischen zwei fotos vergeht
startzeit = time.time()
vorherige_Zeit = startzeit


# initialisiere den video writer.
# Dieser nimmt den speicherpfad entgegen
# danach das Format fuer .avi dateien (in variable fourcc gespeichert)
# und die frames per second, mit der spater das video gespeichert werden soll
# (Sie koennen den Wert veraendern und dann das gespeicherte Video anschauen,
# sehen Sie einen Unterschied?)
# und am ende noch die hoehe und weite des videos

fps = 60
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
video_writer = cv2.VideoWriter(speicher_pfad,fourcc, fps, (w,h))



# wiederhole vorgang "anzahl_Bilder" mal 
for i in range(anzahl_Bilder):
	success, img = Kamera.read()	
	
	#############################################################
	# Zeit messung und ausgabe
	
	aktuelle_Zeit = time.time()	
	aufnahmedauer = aktuelle_Zeit - vorherige_Zeit
	
	text = str(int(i)) + ":  " + str(round(
			aktuelle_Zeit - startzeit,3)) + " s "  + str(round(
			aufnahmedauer,3)) + " s " 

	vorherige_Zeit = aktuelle_Zeit

	cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN,
		    3, (0, 100, 255), 3)
	#############################################################	
				
	# Zeige die Bilder im Display an
	cv2.imshow("Image",img)
	
	# bringe img in richtiges format, falls es nicht bereits richtig ist
	img = cv2.resize(img,(w,h)) 
	
	# fuege das bild zum video hinzu
	video_writer.write(img)
	
	# Sobald Sie den Buchstaben e (ende) druecken, schliesst das Programm
	if (cv2.waitKey(1) & 0xFF == ord('e')):
		break


# gib die Kamera wieder frei nachdem das Programm geschlossen ist
Kamera.release()
# schliesse alle Fenster
cv2.destroyAllWindows()

