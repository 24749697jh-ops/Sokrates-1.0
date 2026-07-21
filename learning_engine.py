from __future__ import annotations


def infer_phase(messages: list[dict]) -> str:
    recent = " ".join(
        str(m.get("content", "")).lower()
        for m in messages[-8:]
        if m.get("role") == "user"
    )

    if any(word in recent for word in ("probe", "prüfen", "kontrollieren", "stimmt", "einsetzen")):
        return "PRÜFEN"
    if any(word in recent for word in ("ergibt", "gerechnet", "umformen", "multipliziert", "geteilt")):
        return "RECHNEN"
    if any(word in recent for word in ("formel", "plan", "strategie", "ansatz", "ich würde")):
        return "PLANEN"
    return "VERSTEHEN"


def phase_question(profile, phase: str, index: int = 0) -> str:
    pools = {
        "VERSTEHEN": profile.opening_questions,
        "PLANEN": profile.planning_questions,
        "RECHNEN": profile.calculation_questions,
        "PRÜFEN": profile.checking_questions,
    }
    questions = pools.get(phase, profile.opening_questions)
    return questions[index % len(questions)]
