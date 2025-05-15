from difflib import unified_diff

with open("original_text.txt") as f:
    original = f.readlines()

with open("tampered_text.txt") as f:
    tampered = f.readlines()

diff = unified_diff(original, tampered, fromfile='original', tofile='tampered')

print("\n".join(diff))
