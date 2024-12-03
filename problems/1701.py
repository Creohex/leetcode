#!python


def solve(customers):
    t = 0
    total_waiting_time = 0

    for arrival, prep in customers:
        if arrival > t:
            t = arrival
        t += prep
        total_waiting_time += t - arrival

    return total_waiting_time / len(customers)


if __name__ == "__main__":
    assert solve([[1, 2], [2, 5], [4, 3]]) == 5.0
    assert solve([[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25
