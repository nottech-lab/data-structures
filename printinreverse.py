# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    if head:
        reversePrint(head.next)
        print(head.data)

if __name__ == '__main__':