from __future__ import annotations

import os

APP_TITLE = "Sokrates"
APP_ICON = "🧭"
MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")
MAX_FILE_SIZE_MB = 20
SUPPORTED_UPLOAD_TYPES = ["pdf", "png", "jpg", "jpeg", "webp", "txt", "docx"]
MAX_OUTPUT_TOKENS = 700
