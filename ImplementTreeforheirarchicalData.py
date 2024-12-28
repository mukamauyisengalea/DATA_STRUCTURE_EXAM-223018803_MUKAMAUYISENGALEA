class TreeNode:
    def __init__(self, category):
        self.category = category
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def display_tree(node, level=0):
    print(" " * level * 4 + node.category)
    for child in node.children:
        display_tree(child, level + 1)

# Example usage
root = TreeNode("Books")
fiction = TreeNode("Fiction")
non_fiction = TreeNode("Non-Fiction")

fiction.add_child(TreeNode("Things Fall Apart"))
fiction.add_child(TreeNode("1984"))
non_fiction.add_child(TreeNode("A Brief History of Time"))

root.add_child(fiction)
root.add_child(non_fiction)

display_tree(root)