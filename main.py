from pathlib import Path

ENTRY = "Bring that app idea you keep explaining over coffee to make.fun in plain words; AI agents can compete to build it, and you pay only the winner."

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(ENTRY, encoding="utf-8")
