from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: Optional[Node] = None

def solve():
    root = Node(0)
    last = root

    for i in range(1, 25):
        node = Node(i)
        last.next = node
        last = node

    def show(node: Node):
        res = []
        while node:
            res.append(node.value)
            node = node.next

        print(res)

    # ---
    show(root)
    last = None
    current = root

    while current:
        t = current.next
        current.next = last
        last = current
        current = t

    show(last)

if __name__ == "__main__":
    solve()
