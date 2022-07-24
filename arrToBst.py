# Python code to convert a sorted array (in reverse order) to a balanced BST (Binary Search Tree)

# binary tree node
class Node:
	def __init__(self, d):
		self.data = d
		self.leftChild = None
		self.rightChild = None
		self.leftNeighbor = None
		self.rightNeighbor = None

# convert sorted array to balanced binary search tree with bi-directional links between both closest neighbors
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
	
	if not arr:
		return None

	# find middle index
	mid = (len(arr)) // 2
	
	# make the middle element the root
	root = Node(arr[mid])
	
	# left subtree 
	# since we have a reversed array, this is the right subtree instead
	# root.leftChild = sortedArrayToBST(arr[:mid]) # this would be the normal way
	root.rightChild = sortedArrayToBST(arr[:mid])
	
	# right subtree 
	# since we have a reversed array, this is the left subtree instead
	# root.rightChild = sortedArrayToBST(arr[mid+1:]) # this would be the normal way
	root.leftChild = sortedArrayToBST(arr[mid+1:])

	# Set left and right children to neighbors
	if root.leftChild is not None and root.rightChild is not None:
		print("Setting neighbors for root: ", root.data)
		root.leftChild.rightNeighbor = root.rightChild
		root.rightChild.leftNeighbor = root.leftChild

	# Set 'cousins' as neighbors
	if root.leftChild is not None and root.rightChild is not None:
		if root.leftChild.rightChild is not None and root.rightChild.leftChild is not None:
			print("Setting cousins for root: ", root.data)
			root.leftChild.rightChild.rightNeighbor = root.rightChild.leftChild
			root.rightChild.leftChild.leftNeighbor = root.leftChild.rightChild

	return root


# driver
arr = [1, 2, 3, 4, 5, 6, 7]
arr.reverse()

root = sortedArrayToBST(arr)

