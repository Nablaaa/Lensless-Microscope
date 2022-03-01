"""
Wilkommen zum zweiten Programm auf dem Weg zu einem funktionsfaehigem 
linsenlosen Mikroskop fuer unter 10 Euro.

Falls Sie Probleme mit diesem Programm haben sollten, schauen Sie sich bitte
das erste Programm "01_Videos_mit_Kamera.py" an

Kommentare, die im vorherigen Programm gemacht wurden, werden hier der
Uebersicht halber verkuerzt oder weg gelassen.

In diesem Programm soll getestet werden, ob:
- die Module imageio (videos speichern) und os (Ordner erstellen) genutzt werden
  koennen
- Ordner erstellt werden koennen
- Videos in den Ordnern gespeichert werden koennen
- Sie die Ordner finden und die Videos ansehen koennen



Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Viel Spass beim ausprobieren!
"""

import cv2
import time
import imageio # videos speichern
import os # Verzeichnisse (Ordner) erstellen



# Erstelle Speicherordner und gebe der Datei einen Namen
# beide Infos ergeben den Speicherpfad
Speicherort = "Speicher-ordner"
gif_name = "Videodatei.gif"
gif_pfad = Speicherort + '/' + gif_name

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
Kamera = cv2.VideoCapture(2)

# gebe an wie viele aufnahmen gemacht werden sollen
anzahl_Bilder = 20	

# die startzeit ist wichtig, um zu sehen wie viel zeit insgesamt vergangen ist
# die "vorherige zeit" und die "aktuelle zeit" im der for schleife sind dazu 
# gedacht, herauszufinden, welche zeit zwischen zwei fotos vergeht
startzeit = time.time()
vorherige_Zeit = startzeit

# kommando zum speicher der fotos
with imageio.get_writer(gif_pfad, mode='I') as writer:
	
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
		
		# Konvertiere Format von BGR (blau gruen rot) zu RGB (rot gruen blau)
		# und speichere es mit 'writer'
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		writer.append_data(imgRGB)
		
		cv2.waitKey(1)



