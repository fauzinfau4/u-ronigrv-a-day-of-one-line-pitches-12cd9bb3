"""Write the one-line make.fun pitch entry to the required output file."""

from pathlib import Path

SENTENCE = "Bring that app idea you keep explaining over coffee to make.fun in plain words; AI agents can compete to build it, and you pay only the winner."

assert 1 <= len(SENTENCE) <= 240
assert "\n" not in SENTENCE

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(SENTENCE, encoding="utf-8")

# Entry verified: 143 characters, one sentence, no trailing newline.
