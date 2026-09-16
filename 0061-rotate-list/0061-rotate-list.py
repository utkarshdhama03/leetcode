class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        n = 1
        temp = head

        while temp.next:
            temp = temp.next
            n += 1

        k = k % n

        if k == 0:
            return head

        temp.next = head

        for _ in range(n - k):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        return new_head