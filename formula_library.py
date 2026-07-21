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
    Formula("Algebra", ("algebra",), "Lineare Gleichung", "a · x + b = c", r"a\cdot x+b=c", "Allgemeine Form einer linearen Gleichung."),
    Formula("Algebra", ("algebra",), "1. binomische Formel", "(a + b)² = a² + 2ab + b²", r"(a+b)^2=a^2+2ab+b^2", "Quadrat einer Summe."),
    Formula("Algebra", ("algebra",), "2. binomische Formel", "(a − b)² = a² − 2ab + b²", r"(a-b)^2=a^2-2ab+b^2", "Quadrat einer Differenz."),
    Formula("Algebra", ("algebra",), "3. binomische Formel", "(a + b)(a − b) = a² − b²", r"(a+b)(a-b)=a^2-b^2", "Summe mal Differenz."),
    Formula("Algebra", ("algebra",), "pq-Formel", "x = −p/2 ± √((p/2)² − q)", r"x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}", "Für x² + px + q = 0."),
    Formula("Brüche", ("fractions",), "Brüche addieren", "a/b + c/d = (ad + bc)/bd", r"\frac ab+\frac cd=\frac{ad+bc}{bd}", "Gemeinsamer Nenner."),
    Formula("Prozentrechnung", ("percent",), "Prozentwert", "W = G · p : 100", r"W=G\cdot\frac p{100}", "Berechnet den Prozentwert."),
    Formula("Prozentrechnung", ("percent",), "Prozentsatz", "p = W : G · 100", r"p=\frac WG\cdot100", "Berechnet den Prozentsatz."),
    Formula("Prozentrechnung", ("percent",), "Grundwert", "G = W · 100 : p", r"G=\frac{W\cdot100}{p}", "Berechnet den Grundwert."),
    Formula("Prozentrechnung", ("percent",), "Zinseszins", "Kₙ = K₀ · qⁿ", r"K_n=K_0\cdot q^n", "Kapitalentwicklung mit Wachstumsfaktor q."),
    Formula("Geometrie", ("geometry",), "Rechteck – Fläche", "A = Länge · Breite", r"A=\mathrm{Länge}\cdot\mathrm{Breite}", "Fläche eines Rechtecks."),
    Formula("Geometrie", ("geometry",), "Dreieck – Fläche", "A = g · h : 2", r"A=\frac{g\cdot h}{2}", "Grundseite mal Höhe, geteilt durch 2."),
    Formula("Geometrie", ("geometry",), "Trapez – Fläche", "A = (a + c) · h : 2", r"A=\frac{(a+c)\cdot h}{2}", "a und c sind parallel."),
    Formula("Geometrie", ("geometry",), "Kreis – Fläche", "A = π · r²", r"A=\pi r^2", "Fläche eines Kreises."),
    Formula("Geometrie", ("geometry",), "Kreis – Umfang", "U = 2 · π · r", r"U=2\pi r", "Umfang eines Kreises."),
    Formula("Geometrie", ("geometry",), "Kreisausschnitt – Fläche", "Aₛ = α : 360° · π · r²", r"A_s=\frac{\alpha}{360^\circ}\cdot\pi r^2", "Fläche eines Kreisausschnitts."),
    Formula("Geometrie", ("geometry",), "Kreisbogen – Länge", "b = α : 360° · 2 · π · r", r"b=\frac{\alpha}{360^\circ}\cdot2\pi r", "Länge eines Kreisbogens."),
    Formula("Geometrie", ("geometry",), "Satz des Pythagoras", "a² + b² = c²", r"a^2+b^2=c^2", "c ist die Hypotenuse."),
    Formula("Körper", ("solid_geometry",), "Prisma – Volumen", "V = G · h", r"V=G\cdot h", "Grundfläche mal Körperhöhe."),
    Formula("Körper", ("solid_geometry",), "Zylinder – Volumen", "V = π · r² · h", r"V=\pi r^2h", "Kreisgrundfläche mal Höhe."),
    Formula("Körper", ("solid_geometry",), "Kegel – Volumen", "V = 1/3 · π · r² · h", r"V=\frac13\pi r^2h", "Ein Drittel des entsprechenden Zylinders."),
    Formula("Funktionen", ("functions",), "Lineare Funktion", "y = m · x + b", r"y=m\cdot x+b", "m ist Steigung, b y-Achsenabschnitt."),
    Formula("Funktionen", ("functions",), "Steigung", "m = (y₂ − y₁) : (x₂ − x₁)", r"m=\frac{y_2-y_1}{x_2-x_1}", "Steigung durch zwei Punkte."),
    Formula("Funktionen", ("functions",), "Scheitelpunktform", "f(x) = a(x − d)² + e", r"f(x)=a(x-d)^2+e", "Scheitelpunkt S(d|e)."),
    Formula("Trigonometrie", ("trigonometry",), "Sinus", "sin(α) = Gegenkathete : Hypotenuse", r"\sin(\alpha)=\frac{\mathrm{Gegenkathete}}{\mathrm{Hypotenuse}}", "Im rechtwinkligen Dreieck."),
    Formula("Trigonometrie", ("trigonometry",), "Kosinus", "cos(α) = Ankathete : Hypotenuse", r"\cos(\alpha)=\frac{\mathrm{Ankathete}}{\mathrm{Hypotenuse}}", "Im rechtwinkligen Dreieck."),
    Formula("Trigonometrie", ("trigonometry",), "Tangens", "tan(α) = Gegenkathete : Ankathete", r"\tan(\alpha)=\frac{\mathrm{Gegenkathete}}{\mathrm{Ankathete}}", "Im rechtwinkligen Dreieck."),
    Formula("Analysis", ("analysis",), "Potenzregel – Ableitung", "f(x) = xⁿ ⇒ f′(x) = n · xⁿ⁻¹", r"f(x)=x^n\Rightarrow f'(x)=n\cdot x^{n-1}", "Ableitung einer Potenz."),
    Formula("Analysis", ("analysis",), "Potenzregel – Stammfunktion", "∫xⁿ dx = xⁿ⁺¹ : (n + 1) + C", r"\int x^n\,dx=\frac{x^{n+1}}{n+1}+C", "Für n ≠ −1."),
    Formula("Statistik", ("statistics",), "Arithmetisches Mittel", "x̄ = Summe der Werte : Anzahl", r"\bar{x}=\frac{\sum x_i}{n}", "Durchschnitt einer Datenreihe."),
    Formula("Wahrscheinlichkeit", ("probability",), "Pfadregel", "P(Pfad) = Produkt der Astwahrscheinlichkeiten", r"P(\mathrm{Pfad})=\prod P(\mathrm{Ast})", "Entlang eines Pfades multiplizieren."),
)

CATEGORIES = (
    "Passend zur Aufgabe",
    "Algebra",
    "Brüche",
    "Prozentrechnung",
    "Geometrie",
    "Körper",
    "Funktionen",
    "Trigonometrie",
    "Analysis",
    "Statistik",
    "Wahrscheinlichkeit",
)


def formulas_for(category: str, topic_key: str) -> tuple[Formula, ...]:
    if category == "Passend zur Aufgabe":
        result = tuple(f for f in FORMULAS if topic_key in f.topics)
        return result or FORMULAS[:8]
    return tuple(f for f in FORMULAS if f.category == category)
