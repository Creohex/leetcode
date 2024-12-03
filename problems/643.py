#!python


def solve(seq, k):
    if len(seq) < k:
        return sum(seq) / len(seq)

    total = sum(seq[:k])
    p = k
    max_avg = total / k

    while p < len(seq):
        total -= seq[p - k]
        total += seq[p]
        if seq[p - k] < seq[p]:
            max_avg = max(max_avg, total / k)
        p += 1

    return max_avg

if __name__ == "__main__":
    assert solve([1,12,-5,-6,50,3], k = 4) == 12.75000
