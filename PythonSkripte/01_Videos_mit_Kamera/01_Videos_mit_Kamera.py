"""
Wilkommen zum ersten Programm auf dem Weg zu einem funktionsfaehigem 
linsenlosen Mikroskop fuer unter 10 Euro.

In diesem Programm soll getestet werden, ob:
- die "Module" (cv2 fuer die Kamera, time fuer Zeit) genutzt werden koennen
- die Kamera funktioniert
- das Bild am Computer angezeigt wird
- Kommentare in das Bild eingefuget werden koennen
- das Programm schliesst wenn man den Buchstaben 'e' drueckt

Weiterhin soll es dazu dienen ein Gefuehl fuer das Programmieren zu bekommen.
Fuehlen Sie sich daher frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Viel Spass beim ausprobieren!
"""



# importiere "Bibliotheken" die einen Grossteil der Arbeit machen
import cv2 # Zugriff auf die Kamera
import time # Zeitmessungen

# suche eine Kamera aus 
# (0 is die eingebaute kamera im laptop, 1,2,3,... sind weitere Anschluesse)
Kamera = cv2.VideoCapture(0) # der name Kamera ist nun bereit und kann verandert
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


# Die folgende schleife wird solange durchlaufen, bis sie den buchstaben e
# auf der Tastatur druecken (da sie immer wahr = 'True' ist)
while True:
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
	
	# Sobald Sie den Buchstaben e (ende) druecken, schliesst das Programm
	if cv2.waitKey(1) & 0xFF == ord('e'):
          break

# gib die Kamera wieder frei nachdem das Programm geschlossen ist
Kamera.release()
# schliesse alle Fenster
cv2.destroyAllWindows()