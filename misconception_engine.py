from __future__ import annotations

import re


RULES: tuple[tuple[str, str, str], ...] = (
    (
        r"\b\d+\s*\([^)]*\+[^)]*\)\s*=\s*\d+\w+\s*\+\s*\d+\b",
        "distributive_incomplete",
        "Möglicherweise wurde beim Ausmultiplizieren nicht jeder Term in der Klammer berücksichtigt.",
    ),
    (
        r"\b\d+\s*/\s*\d+\s*\+\s*\d+\s*/\s*\d+\s*=\s*\d+\s*/\s*\d+\b",
        "fraction_addition",
        "Prüfe, ob du beim Addieren der Brüche zuerst einen gemeinsamen Nenner gebildet hast.",
    ),
    (
        r"\ba\s*[²^]2\s*\+\s*b\s*[²^]2\s*=\s*\(a\+b\)",
        "binomial_middle_term",
        "Beim Quadrat einer Summe fehlt häufig der doppelte Mittelterm $2ab$.",
    ),
    (
        r"\b(?:sin|cos|tan)\b.*(?:hypotenuse|gegenkathete|ankathete)",
        "trig_ratio",
        "Prüfe die Zuordnung von Gegenkathete, Ankathete und Hypotenuse bezogen auf den markierten Winkel.",
    ),
)


def detect_misconception(messages: list[dict]) -> tuple[str, str] | None:
    user_text = " ".join(
        str(m.get("content", ""))
        for m in messages[-4:]
        if m.get("role") == "user"
    ).lower()

    for pattern, key, feedback in RULES:
        if re.search(pattern, user_text, re.I):
            return key, feedback
    return None
