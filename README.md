# Sokrates 1.1.4 – Teacher Engine 2.0 (iPad Edition)

Sokrates 1.1 erweitert vor allem den fachlich-didaktischen Unterbau.
Die Oberfläche bleibt bewusst weitgehend unverändert.

## Neu in 1.1

- deutlich erweiterte Erkennung mathematischer Aufgabentypen
- rund 30 konkret ausgearbeitete Aufgabentypen
- gewichtete Mustererkennung statt einfacher Stichwortsuche
- Schülerzustände:
  - kurze Bestätigung
  - Unsicherheit
  - begründete Erklärung
  - Rechenschritt
  - allgemeine Erklärung
- automatische Erkennung erster typischer Denkfehler
- präzisere Einstiegs-, Planungs-, Rechen- und Prüfungsfragen
- erweiterte Formelsammlung
- Hilfestufen bleiben erhalten

## Neue Themenbereiche

- lineare und quadratische Gleichungen
- Klammergleichungen und Gleichungssysteme
- pq-Formel und binomische Formeln
- Potenzen, Wurzeln und Logarithmen
- Bruchrechnung
- Prozent- und Zinsrechnung
- Dreisatz
- Flächen, Kreis, Pythagoras und Ähnlichkeit
- Prisma, Zylinder und Kegel
- lineare und quadratische Funktionen
- Ableitungen und Integrale
- Trigonometrie
- Statistik
- Baumdiagramme und Kombinatorik

## Installation auf dem iPad

Alle Dateien liegen im Hauptverzeichnis.

1. ZIP-Datei entpacken.
2. Auf GitHub im Repository **Add file → Upload files** öffnen.
3. Alle Dateien auswählen.
4. Gleichnamige Dateien ersetzen.
5. **Commit changes** bestätigen.
6. Streamlit startet nach dem GitHub-Commit normalerweise automatisch neu.

## Neue Datei

Zusätzlich zu den bisherigen Dateien wird benötigt:

- `misconception_engine.py`

Diese Datei muss ebenfalls in das Hauptverzeichnis hochgeladen werden.


## Fehlerbehebung in 1.1.1

- Behebt den Streamlit-Fehler beim Start einer Aufgabe:
  `st.session_state.task_input cannot be modified after the widget is instantiated`
- Behebt denselben möglichen Fehler beim Leeren der Antwort-Eingabe.
- Eingabefelder werden jetzt erst im nächsten Streamlit-Durchlauf sicher geleert.


## Fehlerbehebung in 1.1.2

- Ganze Aufgabenstellungen werden nicht mehr als zusammengezogene LaTeX-Formel angezeigt.
- Normaler Text bleibt normal lesbarer Text.
- Nur kurze mathematische Eingaben erhalten eine Formelvorschau.
- Halbkreisaufgaben werden jetzt ausdrücklich erkannt.
- Eine Gleichung wie `A = 30 cm²` wird nicht mehr fälschlich als lineare Gleichung eingeordnet.
- Die erste Frage bei einer Halbkreisfläche bezieht sich nun auf den Zusammenhang
  zwischen Halbkreis und ganzem Kreis.


## Fehlerbehebung in 1.1.3

- Behebt das Löschen der gesamten Eingabe beim Antippen von `²`, `³`,
  Wurzeln, griechischen Buchstaben oder Operatoren auf dem iPad.
- Die Tastatur verwendet jetzt den aktuell sichtbaren Text aus demselben
  Streamlit-Durchlauf.
- Änderungen werden sicher vor dem erneuten Erzeugen des Eingabefeldes
  übernommen.
- Rücktaste, Löschen und Formel-Builder verwenden dieselbe robuste Methode.


## Korrekturen in 1.1.4

- Die normale Texteingabe wird von der Mathematik-Tastatur nicht mehr verändert.
- Handgeschriebener beziehungsweise normal getippter Text bleibt auf dem iPad erhalten.
- Mathematische Tastatureingaben erscheinen in einer eigenen Ergänzungszeile.
- Beim Absenden werden Text und mathematische Ergänzung zusammengeführt.
- Der Aufgabentyp bleibt an die ursprüngliche Aufgabe gebunden und kann nicht
  durch spätere Schülerantworten versehentlich wechseln.
- Die allererste Lehrerfrage wird direkt von der Teacher Engine erzeugt und
  nicht mehr frei vom Sprachmodell formuliert.
