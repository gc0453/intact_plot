# Programminfo:

Das Programm ist die zweite Aufgabe für die Lehrveranstaltung Programmierübung durchgeführt von Auer Lukas und Gleinser Christoph.

# Vorgabe:

Aufgabe ist es die Datei activity.csv einzulesen und die Leistungswerte bzw. Herzfrequenzwerte über streamlit grafisch sowie als Zahlenwerte auszugeben. Um die Aufgabe umzusetzen, war wichtigen die gegeben Daten zu "reinigen" (leere Werte bzw. Werte mit 0 entfernen). Gefragt waren außerdem die Durchschnittswerte.

# Installationsanleitung:

Bevor das Programm verwendet werden kann, muss das Repository auf Ihr Gerät geklont ( Befehl: git clone https://github.com/gc0453/intact_plot.git) und mit PDM installiert werden ( Befehl: pdm install ). Das Programm kann anschließend mit dem folgenden Befehl ausgeführt werden: pdm run streamlit run main.py 

# Programmbeschreibung:

## Slide 1: Herzfrequenzzonen

Die maximale Herzfrequenz wird über einen Slider eingestellt und die Leistungen pro Zone bzw. die Zeiten pro Zone werden einerseits grafisch (Liniendiagramm mit farblich markierten Zonen, Balkendiagramm) und andereseits in Textform ausgegeben. 

![Bild_1](screenshot/src_1.png)
![Bild_2](screenshot/src_2.png)
![Bild_3](screenshot/src_3.png)

## Slide 2: Power-Data

Die Durschnittsleistung, diemaximale Leistung und der Zeitpunkt werden in Textform ausgegeben. Zusätzlich ist die Leistung noch grafisch ersichtlich

![Bild_4](screenshot/src_4.png)

## Slide 3: Combined Data

Als Zusatz wurde noch ein Diagramm erstellt welches die Leistung sowie die Herzfrequenz dargestellt wird.

![Bild_5](screenshot/src_5.png)