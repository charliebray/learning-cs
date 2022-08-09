
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        a_list = []
        current_node = self
        while current_node != None:
            a_list.append(current_node.val)
            current_node = current_node.next
        return str(a_list)

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node_1 = l1
        current_node_2 = l2

        # Establish a node that just points to the start of the list
        head_node = ListNode()

        # Initialise start of new linked list
        current_new_node = head_node
        new_val = 0
        carry_int = 0
        while current_node_1 != None or current_node_2 != None:
            
            current_new_node.next = ListNode()
            current_new_node = current_new_node.next

            # Determine current node value and the amount to carry
            if current_node_1 == None:
                new_val = (current_node_2.val + carry_int) % 10
                carry_int = int(current_node_2.val + carry_int) // 10
                # Move to next node
                current_node_2 = current_node_2.next
            elif current_node_2 == None:
                new_val = (current_node_1.val + carry_int) % 10
                carry_int = int(current_node_1.val + carry_int) // 10
                # Move to next node
                current_node_1 = current_node_1.next
            else:
                new_val = (current_node_1.val + current_node_2.val + carry_int) % 10
                carry_int = int(current_node_1.val + current_node_2.val + carry_int) // 10
                # Move to next nodes
                current_node_1 = current_node_1.next
                current_node_2 = current_node_2.next

            # Apply new_val to current node
            current_new_node.val = new_val

        # If there's any carry left over, add to end
        if carry_int > 0:
            current_new_node.next = ListNode(carry_int)

        return head_node.next

        # Determine current node value and the amount to carry
        #new_val = (current_node_1.val + current_node_2.val + carry_int) % 10
        #carry_int = int(current_node_1.val + current_node_2.val + carry_int) // 10

if __name__ == '__main__':
    node1_1 = ListNode(9)
    node1_2 = ListNode(9)
    node1_3 = ListNode(9)
    node1_4 = ListNode(9)
    node2_1 = ListNode(9)

    node1_1.next = node1_2
    node1_2.next = node1_3
    node1_3.next = node1_4

    solution = Solution()
    print(node1_1, '+', node2_1)
    print(solution.addTwoNumbers(node1_1, node2_1))