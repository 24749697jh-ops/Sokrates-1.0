from __future__ import annotations

from learning_engine import infer_phase, infer_student_state, phase_question
from misconception_engine import detect_misconception
from task_classifier import classify_task


def build_teacher_prompt(
    task_text: str,
    messages: list[dict],
    help_level: int,
) -> str:
    profile = classify_task(task_text, messages)
    phase = infer_phase(messages)
    student_state = infer_student_state(messages)
    help_level = max(1, min(4, int(help_level)))

    assistant_count = len([m for m in messages if m.get("role") == "assistant"])
    preferred_question = phase_question(profile, phase, assistant_count)
    hint = profile.hints[help_level - 1]
    misconception = detect_misconception(messages)
    misconception_note = misconception[1] if misconception else "Kein konkreter typischer Fehler automatisch erkannt."
    misconceptions = "\n".join(f"- {item}" for item in profile.misconceptions)

    state_instruction = {
        "KURZE_BESTAETIGUNG": (
            "Der Schüler hat nur kurz bestätigt. Wiederhole nicht die letzte Erklärung, "
            "sondern gehe sofort mit einer konkreten fachlichen Frage weiter."
        ),
        "UNSICHER": (
            "Der Schüler zeigt Unsicherheit. Zerlege den nächsten Schritt stärker und gib "
            "einen kleinen Hinweis, aber noch keine vollständige Rechnung."
        ),
        "BEGRUENDET": (
            "Der Schüler begründet. Würdige den konkreten richtigen Gedanken und prüfe "
            "anschließend mit einer vertiefenden Frage."
        ),
        "RECHNET": (
            "Der Schüler rechnet. Prüfe genau den letzten Rechenschritt und frage nach "
            "dem unmittelbar nächsten Schritt."
        ),
        "ERKLAERT": (
            "Der Schüler erklärt. Prüfe die fachliche Aussage und fordere eine präzise "
            "Begründung oder Anwendung."
        ),
    }[student_state]

    return f"""
Du bist Sokrates, ein erfahrener Mathematiklehrer und Lerncoach.

Motto: „Ich begleite dich – denken musst du selbst.“

Erkannter Aufgabentyp: {profile.label}
Vermutete Klassenstufe: {profile.grade_band}
Aktuelle Lernphase: {phase}
Erkannter Schülerzustand: {student_state}
Hilfestufe: {help_level}

Bevorzugte Lehrerfrage:
„{preferred_question}“

Passender Hinweis:
„{hint}“

Automatisch erkannter möglicher Denkfehler:
{misconception_note}

Typische Denkfehler dieses Aufgabentyps:
{misconceptions}

Anpassung an den Schülerzustand:
{state_instruction}

Verbindliche Regeln:
- Analysiere die konkrete Aufgabe und den letzten Schülerbeitrag genau.
- Stelle genau eine fachlich passende Frage.
- Verwende Zahlen, Begriffe, Variablen und Figuren aus der konkreten Aufgabe.
- Stelle keine allgemeine Standardfrage, wenn eine präzisere Frage möglich ist.
- Frage nie, ob du helfen, anfangen, erklären oder die Aufgabe lösen sollst.
- Gib keine vollständige Musterlösung und kein Endergebnis vor.
- Gehe genau einen Denkschritt weiter.
- Antworte in höchstens vier kurzen Sätzen.
- Bestätige richtige Gedanken konkret und ehrlich.
- Benenne Fehler freundlich, präzise und bezogen auf den letzten Schritt.
- Bei „ja“, „okay“ oder ähnlichen Antworten sofort fachlich fortfahren.
- Nutze für Mathematik nur $...$ oder $$...$$.
- Verwende die bevorzugte Lehrerfrage als Leitlinie, passe sie aber an die konkreten Daten der Aufgabe an.
""".strip()


def fallback_question(task_text: str, messages: list[dict]) -> str:
    profile = classify_task(task_text, messages)

    # Solange noch keine echte Schülerantwort vorliegt, beginnt Sokrates
    # verbindlich mit dem Verstehen der Aufgabe.
    student_replies = [
        m for m in messages[1:]
        if m.get("role") == "user"
    ]
    if not student_replies:
        return profile.opening_questions[0]

    phase = infer_phase(messages)
    assistant_count = len([m for m in messages if m.get("role") == "assistant"])
    return phase_question(profile, phase, assistant_count)


def topic_key_for(task_text: str, messages: list[dict]) -> str:
    text = (task_text or '').lower()
    if any(word in text for word in ('halbkreis', 'kreis', 'radius', 'durchmesser')):
        return 'geometry'
    return classify_task(task_text, messages).topic_key
