# 4-misol
def two_longest(words):
    if not words:
        return None, None
    if len(words) == 1:
        return words[0], None
    sorted_indices = sorted(range(len(words)), key=lambda i: (-len(words[i]), i))
    first = words[sorted_indices[0]]
    second = words[sorted_indices[1]]
    return first, second

words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]
first, second = two_longest(words)

print("Ro'yxat:", words)
print("1-chi eng uzun so'z:", first)
print("2-chi eng uzun so'z:", second)

tests = [
    [],
    ["salom"],
    ["a", "bb", "ccc", "dd", "eee", "f"],
    ["same", "size", "here", "ok"]
]

for t in tests:
    f, s = two_longest(t)
    print("\nTest:", t)
    print("1:", f, "2:", s)

print("\nUploaded image file path (local): /mnt/data/4323088c-0a1a-4182-bfcd-981e2e1945d2.png")
