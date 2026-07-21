# Sokrates 1.1.1 – Teacher Engine 2.0 (iPad Edition)

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
