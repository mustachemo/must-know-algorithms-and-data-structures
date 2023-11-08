
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def solution(l, k):
    if not l:
        return

    previous = l
    l = l.next

    while l:
        if previous.value == k:
            previous = previous.next
            l = l.next
        else:
            l = l.next
            previous = previous.next

    return previous


if __name__ == '__main__':
    l = ListNode(3)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(4)
    l.next.next.next.next.next = ListNode(5)

    k = 3

    print(solution(l, k))
