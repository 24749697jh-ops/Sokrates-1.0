from __future__ import annotations

import re


SHORT_ACKS = {"ja", "okay", "ok", "mhm", "verstanden", "gut", "weiter"}
UNCERTAINTY = (
    "weiß nicht", "keine ahnung", "unsicher", "verstehe nicht",
    "kann ich nicht", "hilfe", "hinweis", "keine idee"
)
JUSTIFICATION = ("weil", "denn", "daher", "deshalb", "also", "folglich")
CALCULATION = ("ergibt", "gerechnet", "multipliziert", "geteilt", "addiert", "subtrahiert", "=")
CHECKING = ("probe", "prüfen", "kontrollieren", "stimmt", "einsetzen")


def last_user_text(messages: list[dict]) -> str:
    for message in reversed(messages):
        if message.get("role") == "user":
            return str(message.get("content", "")).lower().strip()
    return ""


def infer_phase(messages: list[dict]) -> str:
    recent = " ".join(
        str(m.get("content", "")).lower()
        for m in messages[-8:]
        if m.get("role") == "user"
    )

    if any(word in recent for word in CHECKING):
        return "PRÜFEN"
    if any(word in recent for word in CALCULATION):
        return "RECHNEN"
    if any(word in recent for word in ("formel", "plan", "strategie", "ansatz", "ich würde")):
        return "PLANEN"
    return "VERSTEHEN"


def infer_student_state(messages: list[dict]) -> str:
    text = last_user_text(messages)
    cleaned = re.sub(r"[^a-zäöüß0-9 ]", "", text)

    if cleaned in SHORT_ACKS or len(cleaned.split()) <= 2:
        return "KURZE_BESTAETIGUNG"
    if any(marker in text for marker in UNCERTAINTY):
        return "UNSICHER"
    if any(marker in text for marker in JUSTIFICATION):
        return "BEGRUENDET"
    if any(marker in text for marker in CALCULATION):
        return "RECHNET"
    return "ERKLAERT"


def phase_question(profile, phase: str, index: int = 0) -> str:
    pools = {
        "VERSTEHEN": profile.opening_questions,
        "PLANEN": profile.planning_questions,
        "RECHNEN": profile.calculation_questions,
        "PRÜFEN": profile.checking_questions,
    }
    questions = pools.get(phase, profile.opening_questions)
    return questions[index % len(questions)]
