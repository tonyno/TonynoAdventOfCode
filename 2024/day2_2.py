
def check_sequence(items: list[int]):
    diffs = [l - r for (l, r) in zip(items[:-1], items[1:])]
    top, bottom = max(diffs), min(diffs)
    return (bottom >= 1 and top <= 3) or (bottom >= -3 and top <= -1)


count = 0
with open('day2.txt', 'r') as f:
    for item in f:
        ok = False
        items_original = list(map(int, item.split()))
        if check_sequence(items_original): ok = True
        for pos in range(len(items_original)):
            items = items_original[:]
            del items[pos]
            if check_sequence(items):
                ok = True
        if ok:
            count += 1

print("Count: ", count)

