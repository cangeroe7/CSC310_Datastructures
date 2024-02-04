# https://www.sanfoundry.com/python-program-implement-stack-using-linked-list/
# simple node class for a linked list, holding a value which is in this case the room,
# and pointer to the next room
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

# Stack class from sanfoundry.com
# Only addjustment is the while loop in the init function to allow a list to be turned into the linked list stack
class Stack:
    def __init__(self, input: list):
        self.head = None
        while input:
            self.push(input.pop())

    def push(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.val
            self.head = self.head.next
            return popped
