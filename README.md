# Sokrates 1.0

Sokrates 1.0 ist eine vollständige Neustrukturierung des bisherigen Prototyps.

## Kernfunktionen

- mathematische Tastatur bereits bei der ersten Aufgabeneingabe
- mathematische Tastatur auch während des Chats
- Hochzahlen, Wurzeln, griechische Buchstaben und Operatoren
- Formel-Builder für Brüche, Potenzen und Wurzeln
- permanente Formelsammlung in der Seitenleiste
- Teacher Engine mit Aufgabentypen und Lernphasen
- GoodNotes-Zwischenablage
- Datei- und Bildanalyse
- Hilfestufen 1 bis 4

## Struktur

```text
sokrates_1_0/
├── app.py
├── config.py
├── requirements.txt
├── engine/
│   ├── models.py
│   ├── task_classifier.py
│   ├── learning_engine.py
│   └── teacher_engine.py
├── formulas/
│   └── library.py
└── ui/
    ├── chat.py
    ├── formula_sidebar.py
    ├── math_editor.py
    └── theme.py
```

## Installation

Am saubersten ist ein neues GitHub-Repository.

1. Alle Dateien und Ordner aus diesem ZIP hochladen.
2. In Streamlit Community Cloud `app.py` als Startdatei wählen.
3. In den Streamlit Secrets hinterlegen:

```toml
OPENAI_API_KEY="dein-openai-api-key"
```

## Wichtig

Alte Dateien aus 0.x-Versionen werden nicht mehr benötigt.
