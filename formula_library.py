from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Formula:
    category: str
    topics: tuple[str, ...]
    title: str
    display: str
    latex: str
    explanation: str


FORMULAS: tuple[Formula, ...] = (
    Formula("Geometrie", ("geometry",), "Rechteck – Fläche", "A = Länge · Breite", r"A=\mathrm{Länge}\cdot\mathrm{Breite}", "Fläche eines Rechtecks."),
    Formula("Geometrie", ("geometry",), "Dreieck – Fläche", "A = g · h : 2", r"A=\frac{g\cdot h}{2}", "Grundseite mal Höhe, geteilt durch 2."),
    Formula("Kreis", ("geometry",), "Kreis – Fläche", "A = π · r²", r"A=\pi r^2", "Fläche eines Kreises."),
    Formula("Kreis", ("geometry",), "Kreis – Umfang", "U = 2 · π · r", r"U=2\pi r", "Umfang eines Kreises."),
    Formula("Kreis", ("geometry",), "Kreisausschnitt – Fläche", "Aₛ = α : 360° · π · r²", r"A_s=\frac{\alpha}{360^\circ}\cdot\pi r^2", "Fläche eines Kreisausschnitts."),
    Formula("Kreis", ("geometry",), "Kreisbogen – Länge", "b = α : 360° · 2 · π · r", r"b=\frac{\alpha}{360^\circ}\cdot2\pi r", "Länge eines Kreisbogens."),
    Formula("Pythagoras", ("pythagoras",), "Satz des Pythagoras", "a² + b² = c²", r"a^2+b^2=c^2", "c ist die Hypotenuse."),
    Formula("Prozentrechnung", ("percent",), "Prozentwert", "W = G · p : 100", r"W=G\cdot\frac{p}{100}", "Berechnet den Prozentwert."),
    Formula("Prozentrechnung", ("percent",), "Prozentsatz", "p = W : G · 100", r"p=\frac{W}{G}\cdot100", "Berechnet den Prozentsatz."),
    Formula("Prozentrechnung", ("percent",), "Grundwert", "G = W · 100 : p", r"G=\frac{W\cdot100}{p}", "Berechnet den Grundwert."),
    Formula("Funktionen", ("function",), "Lineare Funktion", "y = m · x + b", r"y=m\cdot x+b", "m ist die Steigung, b der y-Achsenabschnitt."),
    Formula("Gleichungen", ("linear_equation",), "Lineare Gleichung", "a · x + b = c", r"a\cdot x+b=c", "Allgemeine Form einer linearen Gleichung."),
)

CATEGORIES = (
    "Passend zur Aufgabe",
    "Geometrie",
    "Kreis",
    "Pythagoras",
    "Prozentrechnung",
    "Funktionen",
    "Gleichungen",
)


def formulas_for(category: str, topic_key: str) -> tuple[Formula, ...]:
    if category == "Passend zur Aufgabe":
        result = tuple(f for f in FORMULAS if topic_key in f.topics)
        return result or FORMULAS[:6]
    return tuple(f for f in FORMULAS if f.category == category)
