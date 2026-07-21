from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TaskProfile:
    key: str
    label: str
    topic_key: str
    grade_band: str
    opening_questions: tuple[str, ...]
    planning_questions: tuple[str, ...]
    calculation_questions: tuple[str, ...]
    checking_questions: tuple[str, ...]
    hints: tuple[str, ...]
    misconceptions: tuple[str, ...]


@dataclass
class LearningState:
    phase: str = "VERSTEHEN"
    help_level: int = 1
    last_task_key: str = "general"
    repeated_mistakes: dict[str, int] | None = None

    def __post_init__(self) -> None:
        if self.repeated_mistakes is None:
            self.repeated_mistakes = {}
