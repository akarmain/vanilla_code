VOWELS = set("AEIOUY")

with open("22.txt", "r", encoding="utf-8") as f:
    s = f.read().strip()

ans = 10**18
z_since_vowel = []

for idx, ch in enumerate(s):
    if ch in VOWELS:
        if len(z_since_vowel) >= 72:
            start = z_since_vowel[-72]  # 72nd Z from the right
            ans = min(ans, idx - start + 1)
        z_since_vowel = []  # start fresh after this vowel
    elif ch == "Z":
        z_since_vowel.append(idx)

print(ans if ans != 10**18 else 0)
