class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # If node is not of length one or zero
        if head != None and head.next != None:
            current_node = head
            next_node = current_node.next
            while next_node != None:
                # If next node in sequence has the same value, keep going until distinct
                if current_node.val == next_node.val:
                    next_node = next_node.next
                    continue
                current_node.next = next_node
                current_node = next_node
                next_node = current_node.next
            # Map last node to None (tail)
            current_node.next = None
        return head

if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    print(solution.deleteDuplicates(node1))