**Nom del Projecte:**

PolyBot: El bot de Telegram que respon gràficament i textualment a operacions amb polígons convexos.

**Autor:**

Raul Lumbreras Navarro

**Descripció:**

Pràctica d'LP que consisteix a fer una classe de Python per crear i manipular polígons, un llenguatge de programació amb antlr4 per treballar amb aquests polígons i un bot de Telegram per interaccionar amb els polígons.


**Instalació:**

Perquè funcioni la pràctica cal tenir python3 i instal·lar els mòduls de Python trobats al fitxer requeriments.txt:

Windows:


	pip install antlr4-python3-runtime==4.9
	pip install Pillow==5.4.1
	pip install python-telegram-bot==13.1
	
	
Linux:


	pip3 install antlr4-python3-runtime==4.9
	pip3 install Pillow==5.4.1
	pip3 install python-telegram-bot==13.1


**Ús:**

Un cop feta la instal·lació podem executar el bot de Telegram:

- Des del directori bot de la pràctica podem obrir una terminal i fer:

		python3 bot.py
	
- O fer un run del programa bot.py des d'una IDE.

Un cop executat el bot hem d'obrir una conversació de Telegram amb el bot a <https://t.me/TheoriginalPolyBot>

**Jocs de prova:**

Per facilitar el testeig de la pràctica, aquí deixo dues seccions de codi per provar la pràctica, la primera és la vista a l'enunciat de la pràctica, la segona és una feta per mi mateix, en tots dos casos deixo el resultat esperat.

- Prova 1 (es pot copiar i enganxar al xat de Telegram):
		
		// sample script
		p1 := [0 0  0 1  1 1  0.2 0.8]
		color p1, {1 0 0}
		print p1
		area p1
		perimeter p1
		vertices p1
		centroid p1

		print "---"

		p2 := [0 0  1 0  1 1]
		color p2, {0 1 0}
		print p2
		equal p1, p2
		inside p1, p2
		inside [0.8 0.2], p2

		draw "image.png", p1, p2

		print "---"

		print p1 + p2                           // convex union
		print p1 * p2                           // intersection
		print #p2                               // bounding box
		equal p1 + p2, #p2                      // complex operations
		p3 := #((p1 + p2) * [0 0  1 0  1 1])    // complex operations

		r := !100                               // convex polygon made with 100 random points
		
	Resultat esperat a la imatge prova1.png

		
- Prova 2:

		// sample script to show 0,1 and 2-vertex polygons
		p1 := [] //We can make 0-vertex Polygons
		draw "image1.png", p1
		p2 := [3 8] //We can make 1-vertex Polygons
		draw "image2.png", p2
		p3 := [5 4  7 7] //We can make 2-vertex Polygons
		color p1, {1 0 0}
		draw "image3.png", p3
		area p3
		perimeter p3
		vertices p3
		centroid p3
		draw "image4.png", p2, p3 //We can draw the 1 and 2 vertex polygons together

	Resultat esperat a la imatge prova2.png i a les 4 imatges (imatge1.png, imatge2.png, imatge3.png, imatge4.png)

**Documentació:**

El projecta consisteix en tres parts:

- Polygon.py consisteix en un arxiu que implementa la classe de Python ConvexPolygon, aquesta classe té els implementats els mètodes especificats a l'enunciat de la pràctica (El cost del convexHull és quasi lineal i el de la intersecció quadràtic).

- El directori cl conté tota la part del llenguatge de domini específic creat amb antlr4 per a manipular polígons, aquest directori conte la gramàtica, el visitor i altres arxius utilitzats en la creació.

- El directori bot conté l'arxiu bot.py, el programa que executa el bot i per tant tota la resta del projecte, al fer-lo servir (enviant missatges per Telegram), es guardaran imatges en aquest directori.

