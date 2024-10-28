def iterative():
    alphabet = "abc"
    ans = [""]

    for c in alphabet:
        new = []
        for s in ans:
            new.append(s + c)
        ans.extend(new)

    print(ans)


def recursive():
    def gen(alphabet, current=""):
        print(current)
        if not alphabet:
            return
        gen(alphabet=alphabet[1:], current=current + alphabet[0])
        gen(alphabet=alphabet[1:], current=alphabet[0] + current)

    gen("abc")


def parenthesis_combos():
    def gen(n, current=""):
        if len(current) > n:
            return
        if len(current) == n and current.count("(") == current.count(")"):
            print(current)

        # print(current)
        if current.count("(") > current.count(")"):
            gen(n, current + ")")
        gen(n, current + "(")

    gen(6)


if __name__ == "__main__":
    iterative()
    recursive()
    parenthesis_combos()
