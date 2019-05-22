class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class SimpleTree:

	def inorder(self, node):
		if node is None:
			return

		self.inorder(node.left)
		print(node.data, end=" ")
		self.inorder(node.right)

	def preorder(self, node):
		if node is None:
			return

		print(node.data, end=" ")
		self.preorder(node.left)
		self.preorder(node.right)


	def postorder(self, node):
		if node is None:
			return

		self.postorder(node.left)
		self.postorder(node.right)
		print(node.data, end=" ")


def main():
	root = Node(5)
	root.left= Node(4)
	root.right = Node(6)

	root.left.left = Node(2)
	root.left.right = Node(3)

	root.right.left = Node(7)
	root.right.right = Node(8)

	tree = SimpleTree()

	print("Preorder traversal")
	tree.preorder(root)

	print("\nInorder traversal")
	tree.inorder(root)

	print("\nPostOrder traversal")
	tree.postorder(root)
	print()

 #        5
 #      /   \
 #    4       6
 #  /   \   /   \
 # 2     3 7     8


if __name__ == '__main__':
	main()
		