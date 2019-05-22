'''
Binary Search Tree

		 5
	  /	    \
	3		  8
  /	 \		/   \
 1    4    7	 9
   \
    2

 preorder  = root left right
 inorder   = left root right
 postorser = left right root
'''
class Node:
	"""docstring for Node"""
	def __init__(self, value):
		self.value= value
		self.left = None
		self.right = None

	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True

	def preorder(self):
		if self:
			print(self.value, end=" ")
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()

	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()
			print(self.value,end=" ")
			if self.right:
				self.right.inorder()

	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder()
			print(self.value, end=" ")


class BinaryTree:
	"""docstring for BinaryTree"""
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def preorder(self):
		print("\nPreorder Traversal")
		self.root.preorder()

	def inorder(self):
		print("\nInorder Traversal")
		self.root.inorder()

	def postorder(self):
		print("\nPostorder Traversal")
		self.root.postorder()
		

def main():
	bst = BinaryTree()
	bst.insert(5)
	bst.insert(3)
	bst.insert(1)
	bst.insert(4)
	bst.insert(2)
	bst.insert(8)
	bst.insert(9)
	bst.insert(7)
	bst.preorder()
	bst.postorder()
	bst.inorder()
	print()

if __name__ == '__main__':
	main()