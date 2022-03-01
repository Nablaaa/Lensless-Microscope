"""
Wilkommen zum vierten Programm was zugleich das erste Modul auf dem Weg zu einem 
funktionsfaehigem linsenlosen Mikroskop fuer unter 10 Euro.

Falls Sie Probleme mit diesem Programm haben sollten, schauen Sie sich bitte
die vorherigen Programme an oder besuchen Sie die Tutorials auf YouTube.

Kommentare, die im vorherigen Programm gemacht wurden, werden hier der
Uebersicht halber verkuerzt oder weg gelassen.

Dieses Programm oder besser gesagt dieses "Modul" wird so funktionieren, wie
wir es bisher von cv2, time, imageio und os kennen. Man kann es in ein anderes
Progamm importieren und dann direkt auf die hier definierten Funktionen
zugreifen. Damit spart man sich viel Arbeit, da man nicht alles wieder und
wieder schreiben muss.


Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert. Gerade im "main()" Teil koennen die Einstellungen aus den vorherigen
Programmen wiederholt werden.

Viel Spass beim ausprobieren!
"""

import cv2
import time
import imageio
import os


# Beginne eine "Klasse" (Stichwort: Objektorientiertes Programmieren).

class Kameramodul():
	""" Dieses "Objekt" wird mit Werten initialisiert. Sie kennen das schon von
	cv2 als wir das Objekt mit dem Namen "Kamera" erstellt haben in dem Befehl
	Kamera = cv2.VideoCapture(0)  
	in dieser Zeile ist die "Klasse"  "cv2" und es wird in die Funktion
	"VideoCapture" gesprungen und mit dem Parameter 0 (Null) initialisiert.
	
	Hier heisst unsere Klasse "Kameramodul" und wird mit den Parametern
		Kamera (z.B. 0 falls die Laptopkamera angesprochen werden soll) 
		wCam (weite des Bildes)
		hCam (hoehe des Bildes)
		belichtungszeit
	initialisiert. 
	
	Falls die Parameter nicht weiter spezifiziert werden, dann werden sie mit 
	0, 640, 480, 0.001 initialisiert.
	"""

	# Achtung! Der __init__ Bereich sieht aus wie Zeitverschwendung, aber wenn
	# man sieht wie viel Zeit man spaeter damit spart ist es in Ordnung
	# Sie werden es im naechsten Tutorial sehen!
	def __init__(self, kamera=0, wCam=640, hCam=480):
		"""
		__init__ sind die mindestens notwendigen Parameter, um eine Klasse
		zu initialisieren. Diese Parameter werden als "self" gespeichert und
		gehoeren dann zu der Klasse 'selbst'. Das soll heissen, dass alle
		anderen Funktionen (z.B. "videoansicht") auf alle Parameter zugreifen 
		koennen. Es muss einfach ein "self." davor gesetzt werden.
		
		Hinweis am Rande: Es ist nicht notwendig die Namen der Parameter gleich 
		zu waehlen, aber es macht Sinn, um einen Ueberblick zu behalten.
		Also z.B. self.wCam = wCam koennte auch self.weite = wCam heissen
		und man kann dann innerhalb der Klasse mit self.weite immer darauf
		zurueck greifen. Das aber nur am Rande!
		"""
		
		self.Kamera = cv2.VideoCapture(kamera)
		
		self.wCam = wCam
		self.hCam = hCam
		
		self.Kamera.set(3, self.wCam)
		self.Kamera.set(4, self.hCam)
		
				
	def kameraeinstellungen(self, Helligkeit=20, Kontrast=20, 
								Saettigung=50, Hue=0, Gain=0,
								Belichtung=0,Weissabgl = 0 ):
		"""
		Diese Funktion dient zum Aendern der Kameraeinstellungen.
		Die hier festgelegten Einstellungen werden dann ueberall in der 
		Klasse aufzurufen sein und z.B. in "videoansicht" nutzbar sein
		"""
			
			
		self.Helligkeit = Helligkeit
		self.Kontrast = Kontrast
		self.Saettigung = Saettigung 
		self.Hue = Hue
		self.Gain = Gain
		self.Belichtung = Belichtung
		self.Weissabgl = Weissabgl
			
		self.modi = [10, 11, 12, 13, 14, 15, 17]
		self.initialisierungswerte = [self.Helligkeit, self.Kontrast, 
										self.Saettigung, self.Hue, self.Gain,
										self.Belichtung, self.Weissabgl]
	
		# uebergebe alle werte an die kamera
		for modus, wert in zip(self.modi, self.initialisierungswerte):
			self.Kamera.set(modus, wert)
	
					
	def videoansicht(self, laufzeit=5):
		"""
		Diese Funktion dient der Ansicht von Videos fuer eine bestimmte Zeit.
		Es werden keine Videos gespeichert. Falls beim Aufruf der Funktion
		kein Parameter uebergeben wird, ist der "default" Wert = 5 Sekunden
		"""
	
		startzeit = time.time()
		vorherige_Zeit = startzeit
		
		schleife = True
		while schleife:
			success, img = self.Kamera.read()	
			
			aktuelle_Zeit = time.time()
			zeit_differenz = aktuelle_Zeit - vorherige_Zeit
			fps = 1/zeit_differenz  # (frames per second)
			vorherige_Zeit = aktuelle_Zeit 

			# schreibe die Zeit und "Framerate" in das Display
			text = str(int(fps)) + " FPS, Laufzeit: " + str(int(
							time.time() - startzeit)) + " s"
													
			cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN,
						3, (255, 100, 0), 3)
			
			# Zeige das Foto an
			cv2.imshow("Image",img)
			cv2.waitKey(1)
		
			# Gehe aus schleife raus, wenn laufzeit ueberschritten ist
			if time.time() - startzeit >= laufzeit:
				schleife = False
		
			
			
	def videoaufnahme(self, Speicherort, gif_name, anzahl_Bilder):
		"""
		Zeige Video und speichere es gleich ab. In der Wissenschaft ist es
		angebracht, seine Daten ordentlich zu bennenen. So ist es eigentlich
		immer standard, die Parameter direkt in den Dateinamen zu speichern.
		Das wird hier auch gemacht. Und schon lohnt es sich, dass die Parameter
		ueberall mit "self.Parametername" aufgerufen werden koennen.
		
		Der Rest ist bereits bekannt.
		"""
		
		
		speichername = gif_name + "-dim-" + str(self.hCam) + "_px_" + str(
						self.wCam) + "_px-Helligkeit-" + str(
						self.Helligkeit) + "-Kontrast-" + str(
						self.Kontrast)  + "-Saettigung-" + str(
						self.Saettigung)  + "-Hue-" + str(
						self.Hue)   + "-Gain-" + str(
						self.Gain)   + "-Belichtung-" + str( 
						1000 * self.Belichtung)   + "_ms-Weissabgl-" + str(
						self.Weissabgl) + ".gif"
						
						
		# ist Ihnen aufgefallen, dass die belichtungszeit mit dem Faktor 
		# 1000 versehen ist? Dafuer ist die einheit von sekunden in ms 
		# gewechselt. Diese Aenderung beeinflusst NUR den speichernamen und 
		# NICHT den weiteren Programmverlauf
		
		
		
		# Probiere den Ordner zu erstellen
		try:
			os.mkdir(Speicherort)
		# Falls ein Fehler auftritt gib eine Fehlermeldung aus
		except OSError:
			print ("Der Ordner %s wurde nicht erstellt (z.B. weil er schon existiert)"
					 % Speicherort)
		#ansonsten gib eine Erfoglsmeldung aus
		else:
			print ("Der Ordner %s wurde erfolgreich erstellt" % Speicherort)
	
	
		gif_pfad = Speicherort + "/" + speichername
		
		startzeit = time.time()
		vorherige_Zeit = startzeit
		
		# kommando zum speicher der fotos
		with imageio.get_writer(gif_pfad, mode='I') as writer:
			
			# wiederhole vorgang "anzahl_Bilder" mal 
			for i in range(anzahl_Bilder):
				success, img = self.Kamera.read()	
				
				#############################################################
				# Zeit messung und ausgabe
				
				aktuelle_Zeit = time.time()	
				aufnahmedauer = aktuelle_Zeit - vorherige_Zeit
				
				text = str(int(i)) + ":  " + str(round(
						aktuelle_Zeit - startzeit,3)) + " s "  + str(round(
						aufnahmedauer,3)) + " s " 

				vorherige_Zeit = aktuelle_Zeit

				cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN,
						3, (0, 100, 2550), 3)
				#############################################################	
					
				# Zeige die Bilder im Display an
				cv2.imshow("Image",img)
				
				# Konvertiere Format von BGR zu RGB
				# und speichere es mit 'writer'
				imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				writer.append_data(imgRGB)
				cv2.waitKey(1)



def main():
	"""
	Ein Modul wird eigentlich nur von anderen Programmen aufgerufen. Z.B.
	von "05_Benutze_Kamera_Modul.py"
	Zum Testen des Programmes ist es aber sinnvoll es auch direkt hier aufrufen
	zu koennen. Dazu ist der "main()" Teil gedacht. Hier werden alle 
	Parameter initialisiert, und die Klasse aufgerufen und ausgefuehrt.
	
	Es ist sehr praktisch zum Testen und um zu sehen was das Programm kann.
	
	"""

	kamera = 0 # USB Kamera
	wCam, hCam = 1080, 720 # weite und hoehe des Bildes

	USB_Kamera = Kameramodul(kamera, wCam, hCam)
	
	# theoretisch geht auch:
	#
	# kamera = Kameramodul()
	#
	# weil ja in der "Klasse" die Parameter einen default Wert haben.
	
	
	# Kameraeinstellungen (setze Helligheit und Hue, lasse den Rest als default)
	Helligkeit = 10
	Hue = 0 # spiegelt sozusagen die Hauptfarbe wieder (auch negative Werte)
	
	# stelle nun die einstellungen der kamera ein
	USB_Kamera.kameraeinstellungen( Helligkeit=Helligkeit, Hue=Hue)
	
	
	# starte ein video, z.B. um zu sehen ob die einstellungen gut sind
	USB_Kamera.videoansicht(laufzeit = 1)	
	
	
	Speicherort = "Experiment-01"
	gif_name = "04_Kameramodul"
	anzahl_Bilder = 300	
	
	# nehme ein video auf
	USB_Kamera.videoaufnahme(Speicherort, gif_name, anzahl_Bilder)

	
	
# zum testen des Moduls muss jedes mal beim starten dieses Programmes
# der 'main' Teil laufen. Das erreicht man mit dem folgenden Ausdruck:
if __name__ == "__main__":
	main()
	




