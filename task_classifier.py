from __future__ import annotations

import re
from engine_models import TaskProfile


TASK_PROFILES: tuple[TaskProfile, ...] = (
    TaskProfile(
        "linear_equation",
        "Lineare Gleichung lösen",
        "linear_equation",
        "Klasse 7–10",
        (
            "Welche Rechenoperation steht direkt neben der Variablen und muss zuerst rückgängig gemacht werden?",
            "Welcher Term verhindert, dass die Variable allein steht?",
        ),
        (
            "Welche Gegenoperation führst du auf beiden Seiten aus?",
            "In welcher Reihenfolge solltest du die Rechenschritte rückgängig machen?",
        ),
        (
            "Was ergibt sich nach diesem Umformungsschritt auf beiden Seiten?",
            "Welchen einzelnen Rechenschritt kannst du jetzt sicher ausführen?",
        ),
        (
            "Was erhältst du, wenn du deinen Wert in die Ausgangsgleichung einsetzt?",
            "Sind linke und rechte Seite bei der Probe gleich?",
        ),
        (
            "Arbeite von außen nach innen.",
            "Nutze zuerst die Gegenoperation zur Addition oder Subtraktion.",
            "Teile danach durch den Faktor vor der Variablen.",
            "Setze das Ergebnis zur Probe ein.",
        ),
        (
            "Operation nur auf einer Seite",
            "Vorzeichenfehler",
            "falsche Reihenfolge der Gegenoperationen",
        ),
    ),
    TaskProfile(
        "fraction_add_subtract",
        "Brüche addieren oder subtrahieren",
        "fraction",
        "Klasse 5–8",
        (
            "Sind die Nenner bereits gleich oder musst du zuerst erweitern?",
            "Welcher gemeinsame Nenner passt zu beiden Brüchen?",
        ),
        (
            "Mit welchen Faktoren musst du die Brüche erweitern?",
            "Welche neuen Zähler entstehen dabei?",
        ),
        (
            "Welche Zähler kannst du jetzt zusammenfassen?",
            "Kannst du den entstandenen Bruch noch kürzen?",
        ),
        (
            "Ist das Ergebnis vollständig gekürzt?",
            "Passt die Größe des Ergebnisses zu den Ausgangsbrüchen?",
        ),
        (
            "Betrachte zuerst nur die Nenner.",
            "Finde einen gemeinsamen Nenner.",
            "Erweitere korrekt.",
            "Rechne die Zähler und kürze am Ende.",
        ),
        (
            "Zähler und Nenner getrennt addiert",
            "falsch erweitert",
            "nicht vollständig gekürzt",
        ),
    ),
    TaskProfile(
        "percent",
        "Prozentrechnung",
        "percent",
        "Klasse 6–10",
        (
            "Welche Zahl ist hier der Grundwert?",
            "Welche Größe entspricht dem Prozentsatz?",
        ),
        (
            "Welche der Größen G, p und W ist gesucht?",
            "Welche passende Prozentformel brauchst du?",
        ),
        (
            "Welche Werte setzt du in die Formel ein?",
            "Welchen Rechenschritt kannst du zuerst vereinfachen?",
        ),
        (
            "Ist dein Ergebnis im Verhältnis zum Grundwert plausibel?",
            "Welche Einheit gehört zum Ergebnis?",
        ),
        (
            "Ordne Grundwert, Prozentsatz und Prozentwert zu.",
            "Schreibe die passende Formel auf.",
            "Setze die Werte ein.",
            "Prüfe die Größenordnung.",
        ),
        (
            "Grundwert und Prozentwert vertauscht",
            "Prozentsatz nicht durch 100 geteilt",
            "Einheit vergessen",
        ),
    ),
    TaskProfile(
        "circle_sector",
        "Kreisausschnitt",
        "geometry",
        "Klasse 8–10",
        (
            "Welcher Mittelpunktswinkel und welcher Radius sind gegeben?",
            "Welchen Anteil eines vollständigen Kreises beschreibt der Winkel?",
        ),
        (
            "Brauchst du die Kreisfläche oder den Kreisumfang als Ausgangsgröße?",
            "Mit welchem Bruchteil von 360 Grad musst du weiterrechnen?",
        ),
        (
            "Welche Werte setzt du für α und r ein?",
            "Welchen Teil der Rechnung kannst du zuerst vereinfachen?",
        ),
        (
            "Ist dein Ergebnis kleiner als die entsprechende Größe des ganzen Kreises?",
            "Hast du eine passende Längen- oder Flächeneinheit verwendet?",
        ),
        (
            "Bestimme zuerst, ob Fläche oder Bogenlänge gesucht ist.",
            "Nutze den Anteil α zu 360 Grad.",
            "Multipliziere mit Kreisfläche oder Kreisumfang.",
            "Prüfe Einheit und Größenordnung.",
        ),
        (
            "Fläche und Bogenlänge verwechselt",
            "Winkelanteil vergessen",
            "Radius nicht quadriert",
        ),
    ),
    TaskProfile(
        "triangle_area",
        "Dreiecksfläche",
        "geometry",
        "Klasse 5–9",
        (
            "Welche Grundseite und welche dazugehörige Höhe sind gegeben?",
            "Welche Höhe steht senkrecht auf der gewählten Grundseite?",
        ),
        (
            "Wie lautet die Flächenformel für ein Dreieck?",
            "Warum wird das Produkt durch 2 geteilt?",
        ),
        (
            "Welche Werte setzt du für g und h ein?",
            "Was ergibt zuerst Grundseite mal Höhe?",
        ),
        (
            "Hast du durch 2 geteilt?",
            "Hast du eine quadratische Einheit verwendet?",
        ),
        (
            "Wähle Grundseite und zugehörige Höhe.",
            "Multipliziere beide Werte.",
            "Teile das Produkt durch 2.",
            "Prüfe die Einheit.",
        ),
        (
            "falsche Höhe gewählt",
            "durch 2 nicht geteilt",
            "Umfang statt Fläche berechnet",
        ),
    ),
    TaskProfile(
        "pythagoras",
        "Satz des Pythagoras",
        "pythagoras",
        "Klasse 8–10",
        (
            "Wo liegt der rechte Winkel und welche Seite ist deshalb die Hypotenuse?",
            "Welche beiden Kathetenlängen sind gegeben?",
        ),
        (
            "Wie ordnest du die Seiten in a² + b² = c² ein?",
            "Welche Seite steht allein auf der rechten Seite?",
        ),
        (
            "Welche Quadrate musst du addieren oder voneinander abziehen?",
            "Wann musst du die Wurzel ziehen?",
        ),
        (
            "Ist die Hypotenuse länger als jede Kathete?",
            "Passt dein Ergebnis zur Skizze?",
        ),
        (
            "Bestimme zuerst die Hypotenuse.",
            "Setze die Seiten richtig ein.",
            "Rechne die Quadrate.",
            "Ziehe erst am Ende die Wurzel.",
        ),
        (
            "falsche Seite als Hypotenuse",
            "Wurzel vergessen",
            "Quadrate falsch berechnet",
        ),
    ),
    TaskProfile(
        "linear_function",
        "Lineare Funktion",
        "function",
        "Klasse 8–11",
        (
            "Welche Größe hängt von welcher anderen Größe ab?",
            "Was bedeutet die Steigung in dieser Aufgabe?",
        ),
        (
            "Welche Form y = m · x + b passt hier?",
            "Welche Angaben bestimmen m und b?",
        ),
        (
            "Welche Werte kannst du direkt einsetzen?",
            "Welchen Parameter kannst du zuerst bestimmen?",
        ),
        (
            "Passt das Vorzeichen der Steigung zum Graphen?",
            "Stimmt der y-Achsenabschnitt mit der Darstellung überein?",
        ),
        (
            "Suche zuerst Steigung und Anfangswert.",
            "Ordne sie m und b zu.",
            "Setze ein bekanntes Wertepaar ein.",
            "Prüfe Gleichung und Graph gemeinsam.",
        ),
        (
            "Steigung und y-Achsenabschnitt vertauscht",
            "x- und y-Werte verwechselt",
            "Vorzeichen der Steigung falsch",
        ),
    ),
    TaskProfile(
        "word_problem",
        "Textaufgabe",
        "word_problem",
        "Klasse 5–12",
        (
            "Welche konkrete Größe soll am Ende bestimmt werden?",
            "Welche Angaben gehören unmittelbar zur gesuchten Größe?",
        ),
        (
            "Welchen Zusammenhang kannst du zuerst in Worten beschreiben?",
            "Welche Rechnung oder Gleichung bildet diesen Zusammenhang ab?",
        ),
        (
            "Welchen ersten Rechenschritt kannst du mit den gegebenen Zahlen ausführen?",
            "Welche Zwischengröße brauchst du als Nächstes?",
        ),
        (
            "Beantwortet dein Ergebnis wirklich die Frage des Textes?",
            "Ist das Ergebnis in der beschriebenen Situation plausibel?",
        ),
        (
            "Markiere Gegebenes und Gesuchtes.",
            "Formuliere den Zusammenhang ohne Zahlen.",
            "Übersetze ihn in eine Rechnung.",
            "Prüfe das Ergebnis an der Situation.",
        ),
        (
            "zu früh gerechnet",
            "Frage des Textes nicht beantwortet",
            "Einheit vergessen",
        ),
    ),
)

GENERAL_PROFILE = TaskProfile(
    "general",
    "Mathematikaufgabe",
    "general",
    "offen",
    (
        "Welcher konkrete Teil der Aufgabe ist für den ersten Schritt entscheidend?",
        "Welche Information brauchst du zuerst, um sinnvoll beginnen zu können?",
    ),
    (
        "Welche Regel, Formel oder Darstellung könnte hier passen?",
        "Welchen Zusammenhang erkennst du in der Aufgabe?",
    ),
    (
        "Welchen einzelnen Rechenschritt kannst du jetzt sicher ausführen?",
        "Was ergibt sich aus diesem Zwischenschritt?",
    ),
    (
        "Wie kannst du dein Ergebnis überprüfen?",
        "Passt dein Ergebnis zur Größenordnung und Einheit?",
    ),
    (
        "Konzentriere dich auf einen ersten Schritt.",
        "Ordne Gegebenes und Gesuchtes.",
        "Wähle eine passende Regel.",
        "Prüfe das Ergebnis.",
    ),
    (
        "zu viele Schritte gleichzeitig",
        "unpassende Regel gewählt",
        "Ergebnis nicht geprüft",
    ),
)


def _score(profile: TaskProfile, text: str) -> int:
    key = profile.key
    patterns: dict[str, tuple[str, ...]] = {
        "linear_equation": (r"\bx\b.*=", r"=\s*[-+]?\d", r"\b(löse|bestimme)\b.*\bx\b"),
        "fraction_add_subtract": (r"\d+\s*/\s*\d+\s*[+-]\s*\d+\s*/\s*\d+", r"\bnenner\b", r"\bzähler\b"),
        "percent": (r"%", r"\bprozent\b", r"\brabatt\b", r"\bzins"),
        "circle_sector": (r"\bkreisausschnitt\b", r"\bsektor\b", r"\bkreisbogen\b", r"\bmittelpunktswinkel\b"),
        "triangle_area": (r"\bdreieck\b.*\bfläche", r"\bgrundseite\b", r"\bflächeninhalt\b.*\bdreieck"),
        "pythagoras": (r"\bpythagoras\b", r"\bhypotenuse\b", r"\brechtwinklig"),
        "linear_function": (r"\bsteigung\b", r"\by\s*=", r"\bfunktionsgleichung\b", r"\by-achse"),
        "word_problem": (r".{100,}", r"\b(insgesamt|kostet|fährt|jeweils|mehr als|weniger als)\b"),
    }
    return sum(1 for pattern in patterns.get(key, ()) if re.search(pattern, text, re.I | re.S))


def classify_task(task_text: str, messages: list[dict]) -> TaskProfile:
    conversation = " ".join(
        str(m.get("content", ""))
        for m in messages
        if m.get("role") == "user"
    )
    text = f"{task_text}\n{conversation}".lower().strip()

    best = GENERAL_PROFILE
    best_score = 0
    for profile in TASK_PROFILES:
        score = _score(profile, text)
        if score > best_score:
            best = profile
            best_score = score
    return best
