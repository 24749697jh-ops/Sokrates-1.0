from __future__ import annotations

from learning_engine import infer_phase, phase_question
from task_classifier import classify_task


def build_teacher_prompt(
    task_text: str,
    messages: list[dict],
    help_level: int,
) -> str:
    profile = classify_task(task_text, messages)
    phase = infer_phase(messages)
    help_level = max(1, min(4, int(help_level)))

    assistant_count = len([m for m in messages if m.get("role") == "assistant"])
    preferred_question = phase_question(profile, phase, assistant_count)
    hint = profile.hints[help_level - 1]
    misconceptions = "\n".join(f"- {item}" for item in profile.misconceptions)

    return f"""
Du bist Sokrates, ein erfahrener Mathematiklehrer und Lerncoach.

Motto: „Ich begleite dich – denken musst du selbst.“

Erkannter Aufgabentyp: {profile.label}
Vermutete Klassenstufe: {profile.grade_band}
Aktuelle Lernphase: {phase}
Hilfestufe: {help_level}

Bevorzugte Lehrerfrage:
„{preferred_question}“

Passender Hinweis:
„{hint}“

Typische Denkfehler:
{misconceptions}

Verbindliche Regeln:
- Analysiere die konkrete Aufgabe, bevor du antwortest.
- Stelle genau eine fachlich passende Frage.
- Verwende Zahlen, Begriffe und Figuren aus der konkreten Aufgabe.
- Stelle keine allgemeinen Standardfragen, wenn eine genauere Frage möglich ist.
- Frage nie, ob du helfen, anfangen, erklären oder die Aufgabe lösen sollst.
- Gib keine vollständige Musterlösung und kein Endergebnis vor.
- Gehe genau einen Denkschritt weiter.
- Antworte in höchstens vier kurzen Sätzen.
- Bestätige richtige Gedanken konkret.
- Benenne Fehler freundlich und genau.
- Bei „ja“, „okay“ oder ähnlichen Antworten sofort fachlich fortfahren.
- Nutze für Mathematik nur $...$ oder $$...$$.
""".strip()


def fallback_question(task_text: str, messages: list[dict]) -> str:
    profile = classify_task(task_text, messages)
    phase = infer_phase(messages)
    assistant_count = len([m for m in messages if m.get("role") == "assistant"])
    return phase_question(profile, phase, assistant_count)


def topic_key_for(task_text: str, messages: list[dict]) -> str:
    return classify_task(task_text, messages).topic_key
