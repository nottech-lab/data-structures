'''
Data structure for Tree challenge
'''
def inOrder(root):
    #Write your code here

    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

inOrder(tree.root)