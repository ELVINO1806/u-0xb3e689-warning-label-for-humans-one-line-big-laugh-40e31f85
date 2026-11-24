import os

TEXT = "WARNING: This human's mouth starts moving three seconds before the brain finishes loading."

out_path = "/output/entry.txt"
os.makedirs("/output", exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(TEXT)
