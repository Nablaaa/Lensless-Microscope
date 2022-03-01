"""
Wilkommen zum dritten Programm auf dem Weg zu einem funktionsfaehigem 
linsenlosen Mikroskop fuer unter 10 Euro.

Falls Sie Probleme mit diesem Programm haben sollten, schauen Sie sich bitte
die vorherigen Programme an oder besuchen Sie die Tutorials auf YouTube.

Kommentare, die im vorherigen Programm gemacht wurden, werden hier der
Uebersicht halber verkuerzt oder weg gelassen.

In diesem Programm sollen weitere Kameraeinstellungen ausprobiert werden. Diese
Einstellungen sind fuer das Protokoll wichtig, damit eine andere Forschungs-
gruppe oder Ihre Klassenkamerad:innen den Versuch reproduzieren koennen.

Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Eine Liste fuer die Einstellungen ist hier:
https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

Viel Spass beim ausprobieren!
"""



# HINWEIS: Dieser Teil ist der unuebersichtlichste den wir schreiben werden
# der Rest wird wieder uebersichtlicher und smarter werden




import cv2
import time
import imageio
import os

# Erstelle Speicherordner und gebe der Datei einen Namen
# beide Infos ergeben den Speicherpfad
Speicherort = "Videoordner"
gif_name = "Weitere_Einstellungen.gif"

gif_pfad = Speicherort + '/' + gif_name

# Probiere den Ordner zu erstellen
try:
    os.mkdir(Speicherort)
# Falls ein Fehler auftritt gib eine Fehlermeldung aus
except OSError:
    print ("Der Ordner %s wurde nicht erstellt (z.B. weil er schon existiert)" % Speicherort)
#ansonsten gib eine Erfoglsmeldung aus
else:
    print ("Der Ordner %s wurde erfolgreich erstellt" % Speicherort)
    




# initialisiere Kamera 
Kamera = cv2.VideoCapture(2)
anzahl_Bilder = 100	


"""
die folgenden Einstellungen koennen gemacht werden, manche werden aber nicht
von der Kamera unterstuetzt. 
Die im Set enthaltene Kamera kann:
Weite (3), Hoehe (4), Helligkeit (10), Kontrast (11)
Saettigung (12) und hue (13)
einstellen. Weiterhin interessant waeren noch die Belichtungszeit (15)
und der Weissabgleich (17) aber diese werden zurzeit nicht unterstuetzt
"""

# Diese Einstellung hier machen wir sofort, den Rest stellen wir in einer 
# Schleife ein
wCam, hCam = 640, 480 # weite und hoehe des Bildes
Kamera.set(3, wCam)
Kamera.set(4, hCam)



# Name der Modi und Nummer der Modi, die in der Schleife durchlaufen werden
namen = ['Helligkeit', 'Kontrast', 'Saettigung', 'Hue',
			'Gain', 'Belichtung', 'Weissabgl.']
modi = [10, 11, 12, 13, 14, 15, 17]


# initialisierungswerte bevor modus gewechselt wird
initialisierungswerte = [20,20,50,10,0,0,0]


# Bildrate
startzeit = time.time()
vorherige_Zeit = startzeit


# Speichere videos mit writer
with imageio.get_writer(gif_pfad, mode='I') as writer:

	
	# gehe durch alle Modi und Namen
	for modus, name in zip(modi, namen):
		
		print(modus, name)	
		print("Initialisierung")
	
		# initialisiere die Kamera indem ALLE werte auf standard gesetzt werden
		for m, wert in zip(modi, initialisierungswerte):
			Kamera.set(m, wert) 
			
		time.sleep(1)
	
	
	
		# mache nun pro Modus eine gewissen Anzahl an Bildern uns speicher sie
		for i in range(anzahl_Bilder):
		
			# Teste nun verschiedene Werte durch
					
			# erhoehe wert im ersten Drittel des Videos
			if i < anzahl_Bilder/3:
				einstellungswert = 3 * i
				
			
			# fuer den Rest des Videos gehe bis in den anderen 
			# Bereich des Einstellungsbereiches
			else: 
				einstellungswert = anzahl_Bilder - 3 * (
								i- int(anzahl_Bilder/3))
				
				
			# gebe den Wert an
			Kamera.set(modus, einstellungswert) 
			
			# mache das Foto nun wie gewohnt
			success, img = Kamera.read()	
			
			aktuelle_Zeit = time.time()	
			aufnahmedauer = aktuelle_Zeit - vorherige_Zeit
			
			text = str(int(i)) + ":  " + str(round(
					aktuelle_Zeit - startzeit,3)) + " s "  + str(round(
					aufnahmedauer,3)) + " s " 

			vorherige_Zeit = aktuelle_Zeit


			cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN,
					3, (0, 100, 2550), 3)
		
			
			# zeige Einstellungen an	
			text_einstellung = name + ': ' + str(einstellungswert)
			cv2.putText(img, text_einstellung, (10, 200),
						cv2.FONT_HERSHEY_PLAIN,	3, (0, 100, 2550), 3)
		
				
				
			# Zeige die Bilder im Display an
			cv2.imshow("Image",img)
			
			# Konvertiere Format von BGR (blau gruen rot) zu RGB (rot gruen blau)
			# und speichere es mit 'writer'
			imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			writer.append_data(imgRGB)
			
			cv2.waitKey(1)



