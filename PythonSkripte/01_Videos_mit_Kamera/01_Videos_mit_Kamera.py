"""
Wilkommen zum ersten Programm auf dem Weg zu einem funktionsfaehigem 
linsenlosen Mikroskop fuer unter 10 Euro.

In diesem Programm soll getestet werden, ob:
- die "Module" (cv2 fuer die Kamera, time fuer Zeit) genutzt werden koennen
- die Kamera funktioniert
- das Bild am Computer angezeigt wird
- Kommentare in das Bild eingefuget werden koennen


Weiterhin soll es dazu dienen ein Gefuehl fuer das Programmieren zu bekommen.
Fuehlen Sie sich daher frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Viel Spass beim ausprobieren!
"""



# importiere "Bibliotheken" die einen Grossteil der Arbeit machen
import cv2 # Zugriff auf Kamera
import time # Zeitmessungen

# suche eine Kamera aus 
# (0 is die eingebaute kamera im laptop, 1,2,3,... sind weitere Anschluesse)
Kamera = cv2.VideoCapture(2) # der name Kamera ist nun bereit und kann verandert
							 # werden. Zum Beispiel kann die Aufloesung 
							 # eingestellt werden

# stelle die Aufloesung in pixel ein
wCam, hCam = 640, 480 # weite und hoehe des Bildes
Kamera.set(3, wCam)
Kamera.set(4, hCam)




# optional wollen wir hier die Anzahl der Bilder pro Sekunde (fps) berechnen.
# Dazu muss die Zeit gemessen werden, die fuer ein Bild gebraucht werden
# Hier wird die Zeit initialisiert.
vorherige_Zeit = 0 



# stelle ein, wie lange die Kamera laufen soll
startzeit = time.time()
laufzeit = 50000000 # s
schleife = True

# Fuehre den folgenden Abschnitt in einer Schleife aus, bis der Wert False
# uebergeben wird
while schleife:
	# Mache ein Foto und speichere es als "img"
	success, img = Kamera.read()	
		
		
	# Messe die Zeit, die pro bild gebraucht wird. 
	aktuelle_Zeit = time.time()
	zeit_differenz = aktuelle_Zeit - vorherige_Zeit
	
	# Reziproker Wert ist die Anzahl der Bilder pro zeit
	fps = 1/zeit_differenz  # (frames per second)
	
	vorherige_Zeit = aktuelle_Zeit 

	# schreibe die Zeit in das Display
	text = str(int(fps)) # string = textformat
						 # int = integer (Ganze Zahl... ohne Komma)
	
	# Befehl, um Text in das Bild (img) einzubauen
	# Position, Schriftart, Schriftgroesse, (BGR) Farbcode, Strichdicke
	cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN,
			    3, (255, 100, 0), 3)
	
	
	# Zeige das Foto an
	cv2.imshow("Image",img)
	cv2.waitKey(1)
		
	# wenn die laufzeit ueberschritten wird, wird die schleife auf False gesetzt
	# und endet somit
	if time.time() - startzeit >= laufzeit:
		schleife = False


