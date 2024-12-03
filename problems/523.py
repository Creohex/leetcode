#!python

# continuous subarray sum


def solve(seq, k):
    prefix_mod = 0
    mod_seen = {0: -1}

    for i in range(len(seq)):
        prefix_mod = (prefix_mod + seq[i]) % k

        if prefix_mod in mod_seen:
            # ensures that the size of subarray is at least 2
            if i - mod_seen[prefix_mod] > 1:
                return True
        else:
            # mark the value of prefix_mod with the current index.
            mod_seen[prefix_mod] = i

    return False


def solve(seq, k):
    if len(seq) < 2:
        return False
    elif len(seq) == 2 and not sum(seq) % k:
        return True

    base_value = seq[0]

    for r in range(1, len(seq)):
        base_value += seq[r]
        v = base_value
        if not v % k:
            return True
        for l in range(0, r - 1):
            v -= seq[l]
            if not v % k:
                return True

    return False


if __name__ == "__main__":
    assert solve([23, 2, 4, 6, 7], 6) == True
    assert solve([23, 2, 6, 4, 7], 6) == True
    assert solve([23, 2, 6, 4, 7], 13) == False
    assert solve([0, 0], 1) == True
    assert solve([1, 2, 3], 6) == True
