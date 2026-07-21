from __future__ import annotations

import re
from engine_models import TaskProfile


def P(
    key: str,
    label: str,
    topic_key: str,
    grade_band: str,
    opening: tuple[str, ...],
    planning: tuple[str, ...],
    calculation: tuple[str, ...],
    checking: tuple[str, ...],
    hints: tuple[str, ...],
    misconceptions: tuple[str, ...],
) -> TaskProfile:
    return TaskProfile(
        key, label, topic_key, grade_band,
        opening, planning, calculation, checking, hints, misconceptions
    )


TASK_PROFILES: tuple[TaskProfile, ...] = (
    P(
        "linear_equation", "Lineare Gleichung", "algebra", "Klasse 7–10",
        (
            "Welche Rechenoperation steht direkt neben der Variablen und muss zuerst rückgängig gemacht werden?",
            "Welcher Term verhindert gerade, dass die Variable allein steht?",
        ),
        (
            "Welche Gegenoperation führst du auf beiden Seiten aus?",
            "In welcher Reihenfolge musst du die Rechenschritte rückgängig machen?",
        ),
        (
            "Was entsteht nach genau diesem Umformungsschritt auf beiden Seiten?",
            "Welchen einzelnen Rechenschritt kannst du jetzt sicher ausführen?",
        ),
        (
            "Was erhältst du beim Einsetzen deines Wertes in die Ausgangsgleichung?",
            "Sind linke und rechte Seite bei der Probe gleich?",
        ),
        (
            "Arbeite von außen nach innen.",
            "Mache zuerst Addition oder Subtraktion rückgängig.",
            "Teile danach durch den Faktor vor der Variablen.",
            "Setze das Ergebnis zur Probe ein.",
        ),
        (
            "Operation nur auf einer Seite",
            "Vorzeichenfehler",
            "falsche Reihenfolge der Gegenoperationen",
        ),
    ),
    P(
        "equation_with_parentheses", "Gleichung mit Klammern", "algebra", "Klasse 7–10",
        (
            "Welche Klammer musst du zuerst korrekt auflösen?",
            "Mit welchem Faktor wird jeder Term in der Klammer multipliziert?",
        ),
        (
            "Solltest du zuerst ausmultiplizieren oder zusammenfassen?",
            "Welche Terme kannst du nach dem Auflösen der Klammer zusammenfassen?",
        ),
        (
            "Welche Terme entstehen beim vollständigen Ausmultiplizieren?",
            "Welche gleichartigen Terme kannst du jetzt zusammenfassen?",
        ),
        (
            "Hast du wirklich jeden Term in der Klammer multipliziert?",
            "Stimmt deine Lösung beim Einsetzen in die Ausgangsgleichung?",
        ),
        (
            "Markiere den Faktor vor der Klammer.",
            "Multipliziere ihn mit jedem Term in der Klammer.",
            "Fasse erst danach zusammen.",
            "Löse anschließend die entstandene lineare Gleichung.",
        ),
        (
            "nur ersten Klammerterm multipliziert",
            "Minus vor der Klammer übersehen",
            "ungleichartige Terme zusammengefasst",
        ),
    ),
    P(
        "linear_system", "Lineares Gleichungssystem", "algebra", "Klasse 8–11",
        (
            "Welche Variable lässt sich mit den gegebenen Gleichungen am leichtesten beseitigen?",
            "Welches Verfahren passt hier besser: Einsetzen, Gleichsetzen oder Addieren?",
        ),
        (
            "Wie musst du eine Gleichung verändern, damit sich eine Variable aufhebt?",
            "Welche Variable kannst du zuerst ausdrücken und einsetzen?",
        ),
        (
            "Welche neue Gleichung mit nur einer Variablen entsteht?",
            "Welchen Wert erhältst du für die erste Variable?",
        ),
        (
            "Erfüllt dein Wertepaar beide Ausgangsgleichungen?",
            "Hast du das Ergebnis als geordnetes Paar angegeben?",
        ),
        (
            "Wähle zuerst ein geeignetes Lösungsverfahren.",
            "Beseitige eine Variable.",
            "Bestimme die zweite Variable durch Einsetzen.",
            "Prüfe beide Gleichungen.",
        ),
        (
            "nur eine Gleichung geprüft",
            "Vorzeichen beim Addieren falsch",
            "Lösung nicht als Wertepaar angegeben",
        ),
    ),
    P(
        "quadratic_equation", "Quadratische Gleichung", "algebra", "Klasse 9–12",
        (
            "Liegt die Gleichung bereits in der Form $ax^2+bx+c=0$ vor?",
            "Kannst du die Gleichung faktorisieren oder brauchst du eine Lösungsformel?",
        ),
        (
            "Welche Werte haben $a$, $b$ und $c$?",
            "Welches Verfahren ist hier am übersichtlichsten?",
        ),
        (
            "Wie groß ist die Diskriminante?",
            "Welche beiden möglichen Vorzeichen musst du beim Wurzelausdruck berücksichtigen?",
        ),
        (
            "Wie viele reelle Lösungen erwartest du aufgrund der Diskriminante?",
            "Erfüllen beide Lösungen die Ausgangsgleichung?",
        ),
        (
            "Bringe zuerst alles auf eine Seite.",
            "Bestimme $a$, $b$ und $c$ sorgfältig.",
            "Setze in die passende Lösungsformel ein.",
            "Prüfe jede gefundene Lösung.",
        ),
        (
            "Vorzeichen von b falsch übernommen",
            "± vergessen",
            "nicht auf Normalform gebracht",
        ),
    ),
    P(
        "pq_formula", "pq-Formel", "algebra", "Klasse 9–12",
        (
            "Ist der Koeffizient vor $x^2$ bereits 1?",
            "Welche Werte entsprechen in $x^2+px+q=0$ den Größen $p$ und $q$?",
        ),
        (
            "Musst du die Gleichung zuerst durch einen Faktor teilen?",
            "Wie setzt du $p$ und $q$ mit ihren Vorzeichen ein?",
        ),
        (
            "Was ergibt der Ausdruck unter der Wurzel?",
            "Welche beiden Lösungen entstehen durch das Plus-Minus-Zeichen?",
        ),
        (
            "Hast du beide Lösungen in die Ausgangsgleichung eingesetzt?",
            "Passt die Anzahl der Lösungen zum Wurzelausdruck?",
        ),
        (
            "Normiere zuerst den Koeffizienten von $x^2$ auf 1.",
            "Lies $p$ und $q$ einschließlich Vorzeichen ab.",
            "Berechne zuerst den Wurzelausdruck.",
            "Bilde beide Lösungen und prüfe sie.",
        ),
        (
            "p und q verwechselt",
            "Minus vor p/2 vergessen",
            "nur eine Lösung berechnet",
        ),
    ),
    P(
        "binomial_formula", "Binomische Formel", "algebra", "Klasse 8–11",
        (
            "Welche der drei binomischen Formeln passt zur gegebenen Struktur?",
            "Sind die beiden Terme durch Plus, Minus oder als Produkt zweier Klammern verbunden?",
        ),
        (
            "Welche Terme entsprechen $a$ und $b$?",
            "Welche drei Terme müssen nach dem Ausmultiplizieren entstehen?",
        ),
        (
            "Was ist das Quadrat des ersten Terms?",
            "Wie lautet der doppelte Mittelterm?",
        ),
        (
            "Enthält dein Ergebnis genau drei passende Terme?",
            "Stimmt das Vorzeichen des Mittelterms?",
        ),
        (
            "Ordne zuerst $a$ und $b$ zu.",
            "Nutze die Struktur $a^2 \\pm 2ab + b^2$.",
            "Berechne die drei Teile getrennt.",
            "Prüfe besonders das Vorzeichen des Mittelterms.",
        ),
        (
            "Mittelterm vergessen",
            "Vorzeichen des Mittelterms falsch",
            "Summe der Quadrate statt Quadrat der Summe",
        ),
    ),
    P(
        "power_laws", "Potenzgesetze", "algebra", "Klasse 7–11",
        (
            "Haben die Potenzen dieselbe Basis oder denselben Exponenten?",
            "Welches Potenzgesetz passt genau zu dieser Verknüpfung?",
        ),
        (
            "Musst du Exponenten addieren, subtrahieren oder multiplizieren?",
            "Welche Basis bleibt beim Umformen unverändert?",
        ),
        (
            "Welcher neue Exponent entsteht?",
            "Kannst du den Ausdruck anschließend noch weiter vereinfachen?",
        ),
        (
            "Hast du das Potenzgesetz nur bei gleicher Basis angewendet?",
            "Ist ein negativer Exponent korrekt als Kehrwert gedeutet?",
        ),
        (
            "Vergleiche zuerst die Basen.",
            "Bestimme die Rechenart zwischen den Potenzen.",
            "Wende genau ein Potenzgesetz an.",
            "Prüfe Sonderfälle wie Exponent 0 oder negative Exponenten.",
        ),
        (
            "Exponenten multipliziert statt addiert",
            "Potenzgesetz bei verschiedenen Basen angewendet",
            "negativen Exponenten falsch gedeutet",
        ),
    ),
    P(
        "root_simplification", "Wurzeln vereinfachen", "algebra", "Klasse 8–11",
        (
            "Welcher möglichst große Quadratzahl-Faktor steckt unter der Wurzel?",
            "Kannst du den Radikanden als Produkt aus Quadratzahl und Rest schreiben?",
        ),
        (
            "Welchen Faktor kannst du aus der Wurzel herausziehen?",
            "Bleibt unter der Wurzel noch ein nichtquadratischer Faktor?",
        ),
        (
            "Wie zerlegst du den Radikanden?",
            "Was ist die Wurzel aus dem Quadratzahl-Faktor?",
        ),
        (
            "Ist der Ausdruck vollständig vereinfacht?",
            "Ergeben ursprünglicher und vereinfachter Ausdruck denselben Näherungswert?",
        ),
        (
            "Suche zuerst Quadratzahl-Faktoren.",
            "Zerlege den Radikanden als Produkt.",
            "Ziehe die Quadratzahl aus der Wurzel.",
            "Prüfe, ob noch weiter vereinfacht werden kann.",
        ),
        (
            "Summen unter der Wurzel getrennt",
            "falschen Faktor herausgezogen",
            "nicht vollständig vereinfacht",
        ),
    ),
    P(
        "logarithm", "Logarithmen", "algebra", "Klasse 10–13",
        (
            "Welche Potenzgleichung steckt hinter diesem Logarithmus?",
            "Welche Basis, welcher Numerus und welcher Exponent gehören zusammen?",
        ),
        (
            "Kannst du den Logarithmus in eine Exponentialgleichung umschreiben?",
            "Welches Logarithmengesetz passt zur Verknüpfung?",
        ),
        (
            "Welche Potenz der Basis ergibt den Numerus?",
            "Wie verändert sich der Ausdruck nach Anwendung des Logarithmengesetzes?",
        ),
        (
            "Ist der Numerus positiv?",
            "Stimmt dein Ergebnis beim Rückübersetzen in die Potenzform?",
        ),
        (
            "Übersetze zuerst in die Potenzform.",
            "Ordne Basis, Exponent und Ergebnis zu.",
            "Nutze bei Produkten, Quotienten oder Potenzen das passende Gesetz.",
            "Prüfe den Definitionsbereich.",
        ),
        (
            "Numerus nicht positiv",
            "Basis und Exponent verwechselt",
            "Logarithmengesetz auf Summe angewendet",
        ),
    ),
    P(
        "fraction_add_subtract", "Brüche addieren oder subtrahieren", "fractions", "Klasse 5–8",
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
    P(
        "fraction_multiply_divide", "Brüche multiplizieren oder dividieren", "fractions", "Klasse 5–8",
        (
            "Wird hier multipliziert oder durch einen Bruch geteilt?",
            "Welchen Bruch musst du beim Dividieren umkehren?",
        ),
        (
            "Kannst du vor dem Multiplizieren kürzen?",
            "Welche Faktoren in Zähler und Nenner haben gemeinsame Teiler?",
        ),
        (
            "Welche Produkte entstehen in Zähler und Nenner?",
            "Wie weit kannst du das Ergebnis kürzen?",
        ),
        (
            "Hast du beim Dividieren mit dem Kehrwert multipliziert?",
            "Ist dein Ergebnis vollständig gekürzt?",
        ),
        (
            "Bei Division: bilde zuerst den Kehrwert des zweiten Bruchs.",
            "Kürze möglichst vor dem Multiplizieren.",
            "Multipliziere Zähler mit Zähler und Nenner mit Nenner.",
            "Kürze das Endergebnis vollständig.",
        ),
        (
            "falschen Bruch umgekehrt",
            "quer addiert statt multipliziert",
            "Kürzung über Summen",
        ),
    ),
    P(
        "percent", "Prozentrechnung", "percent", "Klasse 6–10",
        (
            "Welche Zahl ist hier der Grundwert?",
            "Welche Größe entspricht dem Prozentsatz?",
        ),
        (
            "Welche der Größen $G$, $p$ und $W$ ist gesucht?",
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
    P(
        "compound_interest", "Zinseszins", "percent", "Klasse 8–12",
        (
            "Wie groß sind Anfangskapital, Zinssatz und Anzahl der Zeiträume?",
            "Wird der Zins jedes Jahr wieder mitverzinst?",
        ),
        (
            "Welcher Wachstumsfaktor gehört zum Zinssatz?",
            "Wie oft muss der Wachstumsfaktor angewendet werden?",
        ),
        (
            "Wie lautet der Term $K_n=K_0\\cdot q^n$ mit deinen Werten?",
            "Welchen Wert erhältst du für den Wachstumsfaktor?",
        ),
        (
            "Ist das Endkapital größer als das Anfangskapital?",
            "Passt die Entwicklung zur Anzahl der Jahre?",
        ),
        (
            "Berechne zuerst $q=1+\frac{p}{100}$.",
            "Setze Anfangskapital und Laufzeit ein.",
            "Berechne die Potenz.",
            "Prüfe die Größenordnung.",
        ),
        (
            "p statt q potenziert",
            "einfache Zinsen statt Zinseszins",
            "Laufzeit falsch eingesetzt",
        ),
    ),
    P(
        "ratio_rule_of_three", "Dreisatz und proportionale Zuordnung", "word_problem", "Klasse 5–9",
        (
            "Welche beiden Größen gehören jeweils zusammen?",
            "Ist die Zuordnung proportional oder antiproportional?",
        ),
        (
            "Auf welchen Zwischenwert kannst du zuerst zurückrechnen?",
            "Wie verändert sich die zweite Größe, wenn sich die erste vergrößert?",
        ),
        (
            "Was ergibt der Schritt auf eine Einheit?",
            "Mit welchem Faktor gehst du vom Zwischenwert zum gesuchten Wert?",
        ),
        (
            "Wächst oder sinkt dein Ergebnis passend zur Zuordnung?",
            "Sind die Einheiten in allen Zeilen korrekt?",
        ),
        (
            "Ordne die zusammengehörigen Größen.",
            "Entscheide proportional oder antiproportional.",
            "Rechne auf eine Einheit oder nutze einen passenden Faktor.",
            "Prüfe die Richtung der Veränderung.",
        ),
        (
            "proportional und antiproportional verwechselt",
            "Faktor nur auf einer Seite angewendet",
            "Einheiten vertauscht",
        ),
    ),
    P(
        "rectangle_area", "Rechteck – Fläche", "geometry", "Klasse 5–8",
        (
            "Welche Länge und welche Breite sind gegeben?",
            "Sind beide Seitenlängen in derselben Einheit angegeben?",
        ),
        (
            "Welche Flächenformel passt zum Rechteck?",
            "Musst du vor dem Einsetzen noch eine Einheit umrechnen?",
        ),
        (
            "Was ergibt Länge mal Breite?",
            "Welche quadratische Einheit gehört dazu?",
        ),
        (
            "Ist dein Ergebnis größer als jede einzelne Seitenlänge?",
            "Hast du eine Flächeneinheit verwendet?",
        ),
        (
            "Bestimme Länge und Breite.",
            "Bringe beide in dieselbe Einheit.",
            "Multipliziere sie.",
            "Prüfe die quadratische Einheit.",
        ),
        (
            "Umfang statt Fläche",
            "Einheiten nicht angeglichen",
            "Quadrateinheit vergessen",
        ),
    ),
    P(
        "triangle_area", "Dreiecksfläche", "geometry", "Klasse 5–9",
        (
            "Welche Grundseite und welche dazugehörige Höhe sind gegeben?",
            "Welche Höhe steht senkrecht auf der gewählten Grundseite?",
        ),
        (
            "Wie lautet die Flächenformel für ein Dreieck?",
            "Warum wird das Produkt durch 2 geteilt?",
        ),
        (
            "Welche Werte setzt du für $g$ und $h$ ein?",
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
    P(
        "trapezoid_area", "Trapezfläche", "geometry", "Klasse 7–10",
        (
            "Welche beiden Seiten des Trapezes sind parallel?",
            "Welche Höhe steht senkrecht zwischen den parallelen Seiten?",
        ),
        (
            "Wie lautet die Flächenformel mit den parallelen Seiten $a$ und $c$?",
            "Warum wird zunächst der Mittelwert der parallelen Seiten gebildet?",
        ),
        (
            "Was ergibt die Summe der parallelen Seiten?",
            "Welchen Wert erhältst du nach Multiplikation mit der Höhe und Division durch 2?",
        ),
        (
            "Hast du wirklich die parallelen Seiten verwendet?",
            "Ist die Einheit quadratisch?",
        ),
        (
            "Bestimme die parallelen Seiten.",
            "Addiere sie.",
            "Multipliziere mit der Höhe und teile durch 2.",
            "Prüfe die Einheit.",
        ),
        (
            "nichtparallele Seiten eingesetzt",
            "Höhe mit Seitenlänge verwechselt",
            "Division durch 2 vergessen",
        ),
    ),
    P(
        "semicircle", "Halbkreis", "geometry", "Klasse 7–10",
        (
            "Wie hängt die Fläche des Halbkreises mit der Fläche eines ganzen Kreises zusammen?",
            "Welche Kreisgröße ist gegeben und welche Größe soll bestimmt werden?",
        ),
        (
            "Welche Formel verwendest du zunächst für die Fläche eines ganzen Kreises?",
            "An welcher Stelle musst du berücksichtigen, dass nur ein Halbkreis vorliegt?",
        ),
        (
            "Welche Gleichung entsteht aus $A_{Halbkreis}=\\frac{1}{2}\\pi r^2$ mit der gegebenen Fläche?",
            "Welche Operation musst du zuerst rückgängig machen, damit $r^2$ allein steht?",
        ),
        (
            "Ergibt die Hälfte der Kreisfläche mit deinem Radius wieder die vorgegebene Fläche?",
            "Ist dein Radius als Länge und nicht als Flächengröße angegeben?",
        ),
        (
            "Nutze zuerst $A_{Halbkreis}=\\frac{1}{2}\\pi r^2$.",
            "Multipliziere beide Seiten mit 2.",
            "Teile anschließend durch $\\pi$ und ziehe die Wurzel.",
            "Setze den Radius zur Probe in die Halbkreisformel ein.",
        ),
        (
            "Formel des ganzen Kreises ohne Halbierung verwendet",
            "Radius vor dem Wurzelziehen nicht isoliert",
            "Quadratzentimeter als Radiuseinheit übernommen",
        ),
    ),
    P(
        "circle_area_circumference", "Kreis – Fläche oder Umfang", "geometry", "Klasse 7–10",
        (
            "Ist die Fläche oder der Umfang des Kreises gesucht?",
            "Ist der Radius oder der Durchmesser gegeben?",
        ),
        (
            "Musst du den Durchmesser zuerst halbieren?",
            "Welche Formel passt zur gesuchten Größe?",
        ),
        (
            "Welche Werte setzt du für $r$ ein?",
            "Wird der Radius quadriert oder nur mit 2 multipliziert?",
        ),
        (
            "Hast du Längen- und Flächeneinheit unterschieden?",
            "Passt das Ergebnis ungefähr zur Größe des Kreises?",
        ),
        (
            "Kläre zuerst Fläche oder Umfang.",
            "Bestimme den Radius.",
            "Setze in $A=\\pi r^2$ oder $U=2\\pi r$ ein.",
            "Prüfe die Einheit.",
        ),
        (
            "Radius und Durchmesser verwechselt",
            "Flächen- und Umfangsformel verwechselt",
            "Radius bei Fläche nicht quadriert",
        ),
    ),
    P(
        "circle_sector", "Kreisausschnitt", "geometry", "Klasse 8–10",
        (
            "Welcher Mittelpunktswinkel und welcher Radius sind gegeben?",
            "Welchen Anteil eines vollständigen Kreises beschreibt der Winkel?",
        ),
        (
            "Brauchst du die Kreisfläche oder den Kreisumfang als Ausgangsgröße?",
            "Mit welchem Bruchteil von 360 Grad musst du weiterrechnen?",
        ),
        (
            "Welche Werte setzt du für $\alpha$ und $r$ ein?",
            "Welchen Teil der Rechnung kannst du zuerst vereinfachen?",
        ),
        (
            "Ist dein Ergebnis kleiner als die entsprechende Größe des ganzen Kreises?",
            "Hast du eine passende Längen- oder Flächeneinheit verwendet?",
        ),
        (
            "Bestimme zuerst, ob Fläche oder Bogenlänge gesucht ist.",
            "Nutze den Anteil $\\alpha/360^\\circ$.",
            "Multipliziere mit Kreisfläche oder Kreisumfang.",
            "Prüfe Einheit und Größenordnung.",
        ),
        (
            "Fläche und Bogenlänge verwechselt",
            "Winkelanteil vergessen",
            "Radius nicht quadriert",
        ),
    ),
    P(
        "pythagoras", "Satz des Pythagoras", "geometry", "Klasse 8–10",
        (
            "Wo liegt der rechte Winkel und welche Seite ist deshalb die Hypotenuse?",
            "Welche beiden Kathetenlängen sind gegeben?",
        ),
        (
            "Wie ordnest du die Seiten in $a^2+b^2=c^2$ ein?",
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
    P(
        "similarity", "Ähnlichkeit und Strahlensätze", "geometry", "Klasse 8–11",
        (
            "Welche Strecken gehören in den ähnlichen Figuren zueinander?",
            "Welche Seitenverhältnisse sind gleich?",
        ),
        (
            "Welches Verhältnis enthält die gesuchte Strecke?",
            "Wie kannst du eine Verhältnisgleichung aufstellen?",
        ),
        (
            "Welche Werte setzt du in die Verhältnisgleichung ein?",
            "Wie löst du die entstandene Gleichung nach der gesuchten Strecke auf?",
        ),
        (
            "Sind Zähler und Nenner in beiden Verhältnissen gleichartig angeordnet?",
            "Passt die Länge zur Zeichnung?",
        ),
        (
            "Ordne entsprechende Seiten zu.",
            "Schreibe zwei gleich angeordnete Verhältnisse.",
            "Löse die Verhältnisgleichung.",
            "Prüfe die Größenordnung.",
        ),
        (
            "nicht entsprechende Seiten verglichen",
            "Verhältnisse unterschiedlich herum geschrieben",
            "Maßstab falsch gedeutet",
        ),
    ),
    P(
        "prism_volume", "Prisma – Volumen", "solid_geometry", "Klasse 7–11",
        (
            "Welche Fläche ist die Grundfläche des Prismas?",
            "Wie groß ist die senkrechte Körperhöhe?",
        ),
        (
            "Wie berechnest du zuerst die Grundfläche?",
            "Welche Volumenformel gilt für jedes Prisma?",
        ),
        (
            "Welchen Wert erhältst du für $G$?",
            "Was ergibt $G\\cdot h$?",
        ),
        (
            "Hast du eine kubische Einheit verwendet?",
            "Passt die Körperhöhe zur gewählten Grundfläche?",
        ),
        (
            "Bestimme zuerst die Grundfläche.",
            "Berechne deren Flächeninhalt.",
            "Multipliziere mit der Körperhöhe.",
            "Prüfe die Volumeneinheit.",
        ),
        (
            "Mantelfläche als Grundfläche",
            "Körperhöhe mit Seitenkante verwechselt",
            "Quadrat- statt Kubikeinheit",
        ),
    ),
    P(
        "cylinder", "Zylinder", "solid_geometry", "Klasse 8–11",
        (
            "Ist Volumen, Mantelfläche oder Oberfläche gesucht?",
            "Welche Angaben zu Radius und Höhe sind gegeben?",
        ),
        (
            "Welche Kreisgröße brauchst du als Ausgangspunkt?",
            "Welche Teilflächen gehören zur Oberfläche?",
        ),
        (
            "Was ergibt die Grundfläche $\\pi r^2$?",
            "Welche Größe entsteht bei $2\\pi rh$?",
        ),
        (
            "Hast du bei der Oberfläche zwei Grundflächen berücksichtigt?",
            "Passt die Einheit zur gesuchten Größe?",
        ),
        (
            "Kläre zuerst Volumen, Mantel oder Oberfläche.",
            "Berechne die Kreisgrundfläche.",
            "Setze die Höhe passend ein.",
            "Prüfe Anzahl der Grundflächen und Einheit.",
        ),
        (
            "Mantel und Oberfläche verwechselt",
            "zweite Grundfläche vergessen",
            "Radius und Durchmesser verwechselt",
        ),
    ),
    P(
        "cone", "Kegel", "solid_geometry", "Klasse 9–12",
        (
            "Ist Volumen, Mantelfläche oder Oberfläche gesucht?",
            "Sind Radius, Höhe oder Mantellinie gegeben?",
        ),
        (
            "Brauchst du die senkrechte Höhe oder die Mantellinie?",
            "Welche Formel passt zur gesuchten Kegelgröße?",
        ),
        (
            "Was ergibt die Kreisgrundfläche?",
            "Hast du beim Volumen durch 3 geteilt?",
        ),
        (
            "Ist beim Mantel wirklich die Mantellinie verwendet worden?",
            "Hast du Fläche und Volumen korrekt unterschieden?",
        ),
        (
            "Ordne Radius, Höhe und Mantellinie.",
            "Wähle die passende Formel.",
            "Berechne die Kreisgröße.",
            "Prüfe Faktor 1/3 und Einheit.",
        ),
        (
            "Höhe und Mantellinie verwechselt",
            "durch 3 vergessen",
            "Mantel und Oberfläche verwechselt",
        ),
    ),
    P(
        "linear_function", "Lineare Funktion", "functions", "Klasse 8–11",
        (
            "Welche Größe hängt von welcher anderen Größe ab?",
            "Was bedeutet die Steigung in dieser Aufgabe?",
        ),
        (
            "Welche Form $y=m\\cdot x+b$ passt hier?",
            "Welche Angaben bestimmen $m$ und $b$?",
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
            "Ordne sie $m$ und $b$ zu.",
            "Setze ein bekanntes Wertepaar ein.",
            "Prüfe Gleichung und Graph gemeinsam.",
        ),
        (
            "Steigung und y-Achsenabschnitt vertauscht",
            "x- und y-Werte verwechselt",
            "Vorzeichen der Steigung falsch",
        ),
    ),
    P(
        "slope_from_points", "Steigung aus zwei Punkten", "functions", "Klasse 8–11",
        (
            "Welche beiden Punkte sind gegeben?",
            "Wie verändern sich y- und x-Wert zwischen den Punkten?",
        ),
        (
            "Wie lautet der Differenzenquotient für die Steigung?",
            "In welcher Reihenfolge setzt du die Punktkoordinaten ein?",
        ),
        (
            "Was ergibt $\\Delta y$?",
            "Was ergibt $\\Delta x$ und damit $m=\\Delta y/\\Delta x$?",
        ),
        (
            "Erhältst du dieselbe Steigung, wenn du beide Differenzen umgekehrt bildest?",
            "Passt das Vorzeichen zur Lage der Punkte?",
        ),
        (
            "Schreibe beide Punkte geordnet auf.",
            "Berechne y-Differenz und x-Differenz in derselben Reihenfolge.",
            "Bilde den Quotienten.",
            "Prüfe Vorzeichen und Graph.",
        ),
        (
            "Reihenfolge nur in einer Differenz vertauscht",
            "x- und y-Differenz vertauscht",
            "Division durch null übersehen",
        ),
    ),
    P(
        "quadratic_function", "Quadratische Funktion", "functions", "Klasse 9–12",
        (
            "Welche Form der Parabelgleichung liegt vor?",
            "Welche Informationen kannst du direkt über Öffnung, Streckung oder Verschiebung ablesen?",
        ),
        (
            "Brauchst du Scheitelpunktform, Normalform oder Produktform?",
            "Welche Parameter musst du bestimmen?",
        ),
        (
            "Welche Umformung bringt dich zur gewünschten Form?",
            "Welchen Wert erhältst du durch Einsetzen eines bekannten Punktes?",
        ),
        (
            "Passt die Öffnungsrichtung zum Vorzeichen von $a$?",
            "Stimmen Scheitelpunkt oder Nullstellen mit der Gleichung überein?",
        ),
        (
            "Bestimme zuerst die vorliegende Darstellungsform.",
            "Lies direkt erkennbare Parameter ab.",
            "Nutze bekannte Punkte für fehlende Parameter.",
            "Prüfe an Graph oder markanten Punkten.",
        ),
        (
            "Darstellungsformen verwechselt",
            "Vorzeichen der Verschiebung falsch",
            "a aus einem Punkt falsch bestimmt",
        ),
    ),
    P(
        "derivative", "Ableitung", "analysis", "Klasse 11–13",
        (
            "Welche Ableitungsregel passt zum Aufbau der Funktion?",
            "Welche Terme kannst du einzeln ableiten?",
        ),
        (
            "Brauchst du Potenz-, Produkt-, Quotienten- oder Kettenregel?",
            "Welche innere und äußere Funktion erkennst du?",
        ),
        (
            "Wie lautet die Ableitung des ersten Terms?",
            "Welcher zusätzliche Faktor entsteht durch die innere Ableitung?",
        ),
        (
            "Hast du jeden Summanden abgeleitet?",
            "Passt der Grad der abgeleiteten Funktion?",
        ),
        (
            "Zerlege die Funktion in ihre Struktur.",
            "Wähle die passende Ableitungsregel.",
            "Leite Schritt für Schritt ab.",
            "Vereinfache und prüfe den Grad.",
        ),
        (
            "innere Ableitung vergessen",
            "Produktregel unvollständig",
            "Konstante nicht zu null abgeleitet",
        ),
    ),
    P(
        "integral", "Integralrechnung", "analysis", "Klasse 11–13",
        (
            "Ist eine Stammfunktion oder ein bestimmtes Integral gesucht?",
            "Welche Potenzregel brauchst du beim Integrieren?",
        ),
        (
            "Wie verändert sich der Exponent beim Bilden einer Stammfunktion?",
            "Musst du Integrationsgrenzen einsetzen?",
        ),
        (
            "Welche Stammfunktion gehört zum ersten Term?",
            "Was ergibt obere Grenze minus untere Grenze?",
        ),
        (
            "Hast du bei einer unbestimmten Stammfunktion die Konstante $C$ ergänzt?",
            "Kann ein orientierter Flächeninhalt negativ sein?",
        ),
        (
            "Kläre bestimmt oder unbestimmt.",
            "Erhöhe den Exponenten um 1 und teile durch den neuen Exponenten.",
            "Setze bei bestimmten Integralen die Grenzen ein.",
            "Prüfe Vorzeichen und Einheit.",
        ),
        (
            "durch alten statt neuen Exponenten geteilt",
            "Integrationskonstante vergessen",
            "Grenzen in falscher Reihenfolge eingesetzt",
        ),
    ),
    P(
        "right_triangle_trig", "Trigonometrie im rechtwinkligen Dreieck", "trigonometry", "Klasse 9–12",
        (
            "Welche Seite ist bezüglich des gegebenen Winkels Gegenkathete, Ankathete und Hypotenuse?",
            "Welche Seiten sind gegeben und welche ist gesucht?",
        ),
        (
            "Welcher Quotient aus Sinus, Kosinus oder Tangens enthält genau diese Seiten?",
            "Musst du nach einer Seite oder nach einem Winkel auflösen?",
        ),
        (
            "Welche Werte setzt du in den trigonometrischen Quotienten ein?",
            "Welche Umkehrfunktion brauchst du für den Winkel?",
        ),
        (
            "Ist der Winkel zwischen 0 und 90 Grad?",
            "Passt die Seitenlänge zur Rolle als Kathete oder Hypotenuse?",
        ),
        (
            "Beschrifte die drei Seiten relativ zum Winkel.",
            "Wähle den Quotienten mit gegebener und gesuchter Seite.",
            "Stelle nach der gesuchten Größe um.",
            "Prüfe Winkelbereich und Größenordnung.",
        ),
        (
            "Gegen- und Ankathete vertauscht",
            "Sinus und Kosinus verwechselt",
            "Taschenrechner im falschen Winkelmaß",
        ),
    ),
    P(
        "mean_median", "Mittelwert und Median", "statistics", "Klasse 6–11",
        (
            "Ist der arithmetische Mittelwert oder der Median gesucht?",
            "Sind die Daten bereits der Größe nach geordnet?",
        ),
        (
            "Musst du alle Werte addieren oder zuerst sortieren?",
            "Wie viele Werte enthält die Datenreihe?",
        ),
        (
            "Wie groß ist die Summe aller Werte?",
            "Welche mittlere Position ist beim Median entscheidend?",
        ),
        (
            "Passt der Mittelwert ungefähr zur Datenverteilung?",
            "Hast du beim Median eine gerade Anzahl von Werten berücksichtigt?",
        ),
        (
            "Kläre Mittelwert oder Median.",
            "Sortiere für den Median die Werte.",
            "Addiere und teile für den Mittelwert durch die Anzahl.",
            "Prüfe die Lage des Ergebnisses.",
        ),
        (
            "Mittelwert und Median verwechselt",
            "durch falsche Anzahl geteilt",
            "Daten für Median nicht sortiert",
        ),
    ),
    P(
        "probability_tree", "Baumdiagramm und Pfadregeln", "probability", "Klasse 7–12",
        (
            "Wie viele Stufen hat das Zufallsexperiment?",
            "Welche Wahrscheinlichkeiten gehören zu den einzelnen Ästen?",
        ),
        (
            "Welcher Pfad beschreibt das gesuchte Ereignis?",
            "Musst du entlang eines Pfades multiplizieren oder mehrere Pfade addieren?",
        ),
        (
            "Wie groß ist die Wahrscheinlichkeit des ersten passenden Pfades?",
            "Welche weiteren disjunkten Pfade gehören zum Ereignis?",
        ),
        (
            "Ergeben die ausgehenden Wahrscheinlichkeiten an jedem Knoten zusammen 1?",
            "Liegt dein Ergebnis zwischen 0 und 1?",
        ),
        (
            "Zeichne die Stufen vollständig.",
            "Trage an jedem Ast eine Wahrscheinlichkeit ein.",
            "Multipliziere entlang eines Pfades.",
            "Addiere passende disjunkte Pfade.",
        ),
        (
            "Pfadregel und Summenregel verwechselt",
            "Gegenwahrscheinlichkeit falsch",
            "Äste an einem Knoten ergeben nicht 1",
        ),
    ),
    P(
        "combinatorics", "Kombinatorik", "probability", "Klasse 9–13",
        (
            "Spielt die Reihenfolge eine Rolle?",
            "Dürfen Elemente mehrfach verwendet werden?",
        ),
        (
            "Handelt es sich um Permutation, Variation oder Kombination?",
            "Welche Größen entsprechen $n$ und $k$?",
        ),
        (
            "Welche Formel passt zu den Bedingungen?",
            "Welche Fakultäten kannst du kürzen?",
        ),
        (
            "Ist dein Ergebnis eine ganze Zahl?",
            "Passt die Anzahl zur Größe des betrachteten Auswahlraums?",
        ),
        (
            "Kläre Reihenfolge und Wiederholung.",
            "Ordne den Fall einer Zählformel zu.",
            "Setze $n$ und $k$ ein.",
            "Prüfe Plausibilität und Ganzzahligkeit.",
        ),
        (
            "Reihenfolge falsch berücksichtigt",
            "Wiederholung übersehen",
            "n und k vertauscht",
        ),
    ),
    P(
        "word_problem", "Textaufgabe", "word_problem", "Klasse 5–13",
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


GENERAL_PROFILE = P(
    "general", "Mathematikaufgabe", "general", "offen",
    (
        "Welcher konkrete mathematische Zusammenhang ist in der Aufgabe als Erstes entscheidend?",
        "Welche Angabe aus der Aufgabe brauchst du unmittelbar für den ersten Schritt?",
    ),
    (
        "Welche Regel, Formel oder Darstellung passt am genauesten?",
        "Wie kannst du den Zusammenhang zunächst in Worten ausdrücken?",
    ),
    (
        "Welchen einzelnen Rechenschritt kannst du jetzt sicher ausführen?",
        "Was ergibt sich aus genau diesem Zwischenschritt?",
    ),
    (
        "Wie kannst du dein Ergebnis unabhängig überprüfen?",
        "Passt dein Ergebnis zur Größenordnung und Einheit?",
    ),
    (
        "Konzentriere dich auf einen einzigen ersten Schritt.",
        "Ordne Gegebenes und Gesuchtes.",
        "Wähle eine passende Regel.",
        "Prüfe Ergebnis, Einheit und Größenordnung.",
    ),
    (
        "zu viele Schritte gleichzeitig",
        "unpassende Regel gewählt",
        "Ergebnis nicht geprüft",
    ),
)


PATTERNS: dict[str, tuple[tuple[str, int], ...]] = {
    "linear_equation": ((r"\bx\b[^=\n]*=", 4), (r"=\s*[^\n]*\bx\b", 4), (r"\b(löse|bestimme)\b.*\bx\b", 4)),
    "equation_with_parentheses": ((r"\d+\s*\([^)]*x[^)]*\)", 4), (r"\([^)]*x[^)]*\)\s*=", 3)),
    "linear_system": ((r"\bgleichungssystem\b", 6), (r"\b(lgs|einsetzungsverfahren|additionsverfahren|gleichsetzungsverfahren)\b", 6), (r"\bx.*y.*=", 2)),
    "quadratic_equation": ((r"\bx\s*[²^]2\b", 4), (r"\bquadratische gleichung\b", 6), (r"\bx\^2\b", 4)),
    "pq_formula": ((r"\bpq[- ]formel\b", 8),),
    "binomial_formula": ((r"\bbinom", 7), (r"\([^)]+[+-][^)]+\)\s*[²^]2", 5)),
    "power_laws": ((r"\bpotenzgesetz", 7), (r"\w+\^\w+\s*[*:/]\s*\w+\^\w+", 4)),
    "root_simplification": ((r"\b(wurzel|radikand)\b", 4), (r"√", 4)),
    "logarithm": ((r"\b(logarithmus|log|ln)\b", 7),),
    "fraction_add_subtract": ((r"\d+\s*/\s*\d+\s*[+-]\s*\d+\s*/\s*\d+", 7), (r"\b(nenner|zähler|erweitern)\b", 3)),
    "fraction_multiply_divide": ((r"\d+\s*/\s*\d+\s*[*:÷]\s*\d+\s*/\s*\d+", 7), (r"\bkehrwert\b", 5)),
    "percent": ((r"%", 4), (r"\b(prozent|rabatt|mehrwertsteuer)\b", 5)),
    "compound_interest": ((r"\b(zinseszins|endkapital|anfangskapital)\b", 8), (r"\bzinsen\b.*\bjahre\b", 4)),
    "ratio_rule_of_three": ((r"\b(dreisatz|proportional|antiproportional)\b", 7),),
    "rectangle_area": ((r"\brechteck\b", 4), (r"\b(länge|breite)\b.*\bfläche", 4)),
    "triangle_area": ((r"\bdreieck\b.*\b(fläch|höhe|grundseite)", 6),),
    "trapezoid_area": ((r"\btrapez\b", 7),),
    "semicircle": ((r"\bhalbkreis(?:es|en|e|s)?\b", 10), (r"\bhalbkreis", 9)),
    "circle_area_circumference": ((r"\b(?:kreis|halbkreis|viertelkreis|kreisfläche|kreisumfang)\w*\b.*\b(fläch|umfang|radius|durchmesser)", 6),),
    "circle_sector": ((r"\b(kreisausschnitt|sektor|kreisbogen|mittelpunktswinkel)\b", 8),),
    "pythagoras": ((r"\b(pythagoras|hypotenuse|rechtwinklig)\b", 7),),
    "similarity": ((r"\b(strahlensatz|ähnlich|maßstab)\b", 6),),
    "prism_volume": ((r"\bprisma\b", 7),),
    "cylinder": ((r"\bzylinder\b", 8),),
    "cone": ((r"\bkegel\b", 8),),
    "linear_function": ((r"\blineare funktion\b", 7), (r"\by\s*=\s*[-+]?\d*\.?\d*\s*[·*]?\s*x", 5), (r"\by-achsenabschnitt\b", 5)),
    "slope_from_points": ((r"\bsteigung\b.*\bpunkt", 7), (r"\bpunkt(e)?\b.*\bsteigung\b", 7)),
    "quadratic_function": ((r"\b(parabel|quadratische funktion|scheitelpunkt)\b", 7),),
    "derivative": ((r"\b(ableitung|ableiten|differenzieren)\b", 8), (r"f\s*'", 5)),
    "integral": ((r"\b(integral|stammfunktion|integrieren)\b", 8), (r"∫", 8)),
    "right_triangle_trig": ((r"\b(sinus|kosinus|cosinus|tangens)\b", 7), (r"\bgegenkathete|ankathete\b", 8)),
    "mean_median": ((r"\b(mittelwert|median|zentralwert)\b", 7),),
    "probability_tree": ((r"\b(baumdiagramm|pfadregel|wahrscheinlichkeit)\b", 6),),
    "combinatorics": ((r"\b(kombination|variation|permutation|fakultät)\b", 7),),
    "word_problem": ((r".{180,}", 2), (r"\b(insgesamt|kostet|fährt|jeweils|mehr als|weniger als)\b", 2)),
}


def _score(profile: TaskProfile, text: str) -> int:
    return sum(weight for pattern, weight in PATTERNS.get(profile.key, ()) if re.search(pattern, text, re.I | re.S))


def classify_task(task_text: str, messages: list[dict]) -> TaskProfile:
    # The original task determines the mathematical topic. Later student
    # answers must not accidentally reclassify the whole problem.
    conversation = " ".join(
        str(m.get("content", ""))
        for m in messages
        if m.get("role") == "user"
    )
    text = (task_text or conversation).lower().strip()

    ranked = sorted(
        ((profile, _score(profile, text)) for profile in TASK_PROFILES),
        key=lambda item: item[1],
        reverse=True,
    )
    best, score = ranked[0]
    return best if score > 0 else GENERAL_PROFILE


def classifier_debug(task_text: str, messages: list[dict]) -> list[tuple[str, int]]:
    conversation = " ".join(
        str(m.get("content", ""))
        for m in messages
        if m.get("role") == "user"
    )
    text = (task_text or conversation).lower().strip()
    ranked = sorted(
        ((profile.label, _score(profile, text)) for profile in TASK_PROFILES),
        key=lambda item: item[1],
        reverse=True,
    )
    return [item for item in ranked[:5] if item[1] > 0]
