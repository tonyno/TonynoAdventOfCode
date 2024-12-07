def check_sequence(items: list[int]):
    diffs = [l - r for (l, r) in zip(items[:-1], items[1:])]
    top, bottom = max(diffs), min(diffs)
    return (bottom >= 1 and top <= 3) or (bottom >= -3 and top <= -1)

with open('day2.txt', 'r') as f:
    print("Count: ", sum(check_sequence(list(map(int, item.split()))) for item in f))



