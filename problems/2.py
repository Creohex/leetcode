
class ListNode:
    def __init__(self, val=0, next=None):
        if 0 <= val <= 9:
            self.val = val
            self.next = next
        else:
            node = n_to_l(val)
            self.val = node.val
            self.next = node.next

def l_to_n(l):
    s = ""
    while l:
        s += str(l.val)
        l = l.next
    return int(s[::-1])

def n_to_l(n):
    l = None
    [l := ListNode(int(c), l) for c in str(n)]
    return l

def add_linked_lists(l1, l2):
    return n_to_l(l_to_n(l1) + l_to_n(l2))


assert l_to_n(add_linked_lists(ListNode(243), ListNode(564))) == 807
assert l_to_n(add_linked_lists(ListNode(0), ListNode(0))) == 0
assert l_to_n(add_linked_lists(ListNode(954), ListNode(56))) == 1010
assert l_to_n(add_linked_lists(ListNode(9999999), ListNode(9999))) == 10009998
