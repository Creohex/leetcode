#!python


def solve(s: str, shifts: list[int]) -> str:
    accumulator = 0
    shifts_moved = []
    for i in reversed(range(len(shifts))):
        shifts_moved.insert(0, accumulator + shifts[i])
        accumulator += shifts[i]

    return "".join(
        map(
            lambda v: chr(((v - (123)) % 26) + 97),
            map(sum, zip(map(ord, s.strip()), shifts_moved)),
        )
    )


def solve(s: str, shifts: list[int]) -> str:
    res = []
    start = ord("a")
    end = ord("z") + 1
    alphabet_len = 26

    def shift(c, steps):
        return chr((((ord(c) + steps) - end) % alphabet_len) + start)

    step_accumulator = 0
    for i in reversed(range(len(shifts))):
        step_accumulator += shifts[i]
        res.insert(0, shift(s[i], step_accumulator))

    return "".join(res)


if __name__ == "__main__":
    assert solve("abc", [3, 5, 9]) == "rpl"
    assert solve("z", [1]) == "a"
