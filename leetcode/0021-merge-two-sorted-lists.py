# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Implementing the last step of a merge sort essentially. O(n) time complexity.
    '''
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        # Get heads of each singly-linked list.
        node_1, node_2 = list1, list2

        # If either node is empty, just return the other node
        if node_1 == None:
            return node_2
        if node_2 == None:
            return node_1
        
        # Create a head node
        if node_1.val < node_2.val:
            head_node = node_1
            node_1 = node_1.next
        else:
            head_node = node_2
            node_2 = node_2.next
        
        current_node = head_node

        while node_1 != None or node_2 != None:
            # If we reach the end of either list, just map to the other node and break.
            if node_1 == None:
                current_node.next = node_2
                break
            if node_2 == None:
                current_node.next = node_1
                break

            # If we aren't at the end of either list, we compare then point to a new node thats the lowest of the two.
            if node_1.val < node_2.val:
                current_node.next = node_1
                current_node = node_1
                node_1 = node_1.next
            else:
                current_node.next = node_2
                current_node = node_2
                node_2 = node_2.next

        return head_node

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node3
    node2.next = node4

    solution = Solution()
    node = solution.mergeTwoLists(node1, node2)
    while node != None:
        print(node.val)
        node = node.next


